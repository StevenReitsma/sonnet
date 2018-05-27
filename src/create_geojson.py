"""
Convert deep learning model predictions to geojson
"""
import pickle
import json
import os
import matplotlib.pyplot as plt
import numpy as np
from scrape_image import RDWGSConverter


def main():
    with open('predictions_wijchen.pkl', 'rb') as f:
        predictions = pickle.load(f)

    geojson = {}
    geojson['type'] = 'FeatureCollection'
    geojson['features'] = []
    predictions = sorted(predictions, key=lambda p: int(os.path.basename(p[0]).split('.')[0]))

    min_x, min_y, max_x, max_y = 178579, 426001, 179180, 426379
    stride = 15
    i = 0
    for x in np.arange(min_x, max_x, stride):
        for y in np.arange(min_y, max_y, stride):
            if predictions[i][1] > 0.96:
                coords = RDWGSConverter().fromRdToWgs((x, y))
                geojson['features'].append({
                    'type': 'Feature',
                    'geometry': {
                        'type': 'Point',
                        'coordinates': coords[::-1]
                    },
                    'properties': {
                        'id': i,
                        'solar_llh': f'{predictions[i][1]:.2f}'
                    }
                })
            i += 1
    
    with open('solar_llh_wijchen.json', 'w') as f:
        json.dump(geojson, f)


if __name__ == '__main__':
    main()
