from pyproj import Proj, transform
import requests
import shutil
import json
import tqdm
import random
import numpy as np


class RDWGSConverter:
    # variables for both
    X0 = 155000
    Y0 = 463000
    phi0 = 52.15517440
    lam0 = 5.38720621

    # variables for fromRdToWgs
    Kp = [0, 2, 0, 2, 0, 2, 1, 4, 2, 4, 1]
    Kq = [1, 0, 2, 1, 3, 2, 0, 0, 3, 1, 1]
    Kpq = [3235.65389, -32.58297, -0.24750, -0.84978, -0.06550, -0.01709, -0.00738, 0.00530, -0.00039, 0.00033,
           -0.00012]

    Lp = [1, 1, 1, 3, 1, 3, 0, 3, 1, 0, 2, 5]
    Lq = [0, 1, 2, 0, 3, 1, 1, 2, 4, 2, 0, 0]
    Lpq = [5260.52916, 105.94684, 2.45656, -0.81885, 0.05594, -0.05607, 0.01199, -0.00256, 0.00128, 0.00022,
           -0.00022, 0.00026]

    # Variables for fromWgstoRd

    Rp = [0, 1, 2, 0, 1, 3, 1, 0, 2]
    Rq = [1, 1, 1, 3, 0, 1, 3, 2, 3]
    Rpq = [190094.945, -11832.228, -114.221, -32.391, -0.705, -2.340, -0.608, -0.008, 0.148]

    Sp = [1, 0, 2, 1, 3, 0, 2, 1, 0, 1]
    Sq = [0, 2, 0, 2, 0, 1, 2, 1, 4, 4]
    Spq = [309056.544, 3638.893, 73.077, -157.984, 59.788, 0.433, -6.439, -0.032, 0.092, -0.054]

    def fromRdToWgs(self, coords):

        dX = 1E-5 * (coords[0] - self.X0)
        dY = 1E-5 * (coords[1] - self.Y0)

        phi = self.phi0 + sum(
            [(self.Kpq[k] * dX ** self.Kp[k] * dY ** self.Kq[k]) for k in range(len(self.Kpq))]) / 3600
        lam = self.lam0 + sum(
            [(self.Lpq[l] * dX ** self.Lp[l] * dY ** self.Lq[l]) for l in range(len(self.Lpq))]) / 3600

        return [phi, lam]

    def fromWgsToRd(self, coords):
        dPhi = 0.36 * (coords[0] - self.phi0)
        dLam = 0.36 * (coords[1] - self.lam0)

        X = self.X0 + sum([(self.Rpq[r] * dPhi ** self.Rp[r] * dLam ** self.Rq[r]) for r in range(len(self.Rpq))])
        Y = self.Y0 + sum([self.Spq[s] * dPhi ** self.Sp[s] * dLam ** self.Sq[s] for s in range(len(self.Spq))])

        return [X, Y]


# Usage:
# coords = [258226.571, 480433.175]
# conv = RDWGSConverter()
# wgsCoords = conv.fromRdToWgs( coords )

# WIDTH=1425&HEIGHT=568
# BBOX=732541.68115603,7023210.685730154,732967.1607078778,7023380.280386609
URL = 'https://geodata.nationaalgeoregister.nl/luchtfoto/rgb/wms?SERVICE=WMS&REQUEST=GetMap&FORMAT=image/png&TRANSPARENT=TRUE&STYLES=&VERSION=1.3.0&LAYERS={year}_ortho25&WIDTH=256&HEIGHT=256&CRS=EPSG:3857&BBOX={bbox}'
def scrape(coords, object_id, **kwargs):
    x, y = coords[0], coords[1]
    folder = kwargs.pop('folder', 'positives')
    year = kwargs.pop('year', 2017)
    is_rd = kwargs.pop('is_rd', True)
    SIZE = 76
    conv = RDWGSConverter()
    if is_rd:
        wgs_x, wgs_y = conv.fromRdToWgs([x, y])
    else:
        wgs_x, wgs_y = x, y
    epsg_coords = transform(Proj(init='epsg:4326'), Proj(init='epsg:3857'), wgs_y, wgs_x)
    bbox = (epsg_coords[0]-SIZE//2, epsg_coords[1]-SIZE//2, epsg_coords[0]+SIZE//2, epsg_coords[1]+SIZE//2)
    response = requests.get(URL.format(year=year, bbox=','.join(list(map(str, bbox)))), stream=True)
    with open(f'{folder}/{object_id}.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)


def fetch_positives():
    print('getting positives...')
    with open('groei_zonnepanelen_Groningen.json') as f:
        solar_panels = json.load(f)

    for panel in tqdm.tqdm(solar_panels):
        scrape((panel['geometry']['x'], panel['geometry']['y']), panel['attributes']['OBJECTID'])


def fetch_negatives(min_coord, max_coord):
    n = 2880
    print('getting negatives')
    for i in tqdm.tqdm(range(10000, 10000+n)):
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)
        scrape((x, y), i, folder='satdata/train/negatives')


def get_exhaustive_patches(coords, stride=15):
    min_x, min_y, max_x, max_y = coords
    i = 0
    for x in tqdm.tqdm(np.arange(min_x, max_x, stride)):
        for y in np.arange(min_y, max_y, stride):
            scrape((x, y), i, 'test', year=2017)
            i += 1


def amsterdam_positives():
    print('getting amsterdam positives')
    with open('/home/joris/Downloads/ZONNEPANELEN2017.json') as f:
        amsterdam_zp = json.load(f)['features']
    
    for panel in tqdm.tqdm(amsterdam_zp):
        scrape(reversed(panel['geometry']['coordinates']), 'ams'+str(panel['id']), year=2017, is_rd=False, folder='amsterdam_positives')




def main():
    # fetch_positives()
    # fetch_negatives(228100, 577600, 239200, 586500)
    get_exhaustive_patches([230780, 581974, 231211, 582298])
    # amsterdam_positives()
    # fetch_negatives(118594, 484144, 123860, 487248)


if __name__ == '__main__':
    main()
