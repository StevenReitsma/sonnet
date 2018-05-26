import json
import requests


url = 'https://services2.arcgis.com/chCSiGO4ORzXeSGk/ArcGIS/rest/services/{layer_name}/FeatureServer/0/query?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=*&returnGeometry=true&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnDistinctValues=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset={offset}&resultRecordCount={count}&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=json&token='
layer_name = 'groei_zonnepanelen_Groningen'
n = 2880

current_offset = 0
all_data = []
while current_offset < n:
    count = min(1000, n - current_offset)
    req_url = url.format(layer_name=layer_name, offset=current_offset, count=count)
    result = requests.get(req_url)
    data = result.json()['features']
    all_data.extend(data)
    current_offset += 1000

print(f'Found {len(all_data)} datapoints')
with open(layer_name+'.json', 'w') as f:
    json.dump(all_data, f)