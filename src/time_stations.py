"""
Convert the stations CSV to a CSV with time as a column
"""
import pandas as pd


stations = pd.read_csv('real_final_stations.csv')
stations = stations[stations.VERMOGEN_NOMINAAL_CAPACITEIT != 0]
stations = stations[(stations.FORECAST_SOLAR_PEAK_2017 != 0) | (stations.FORECAST_SOLAR_PEAK_2026 != 0)]

result = stations[['STATIONSNUMMER','Gemeente','BOUWJAAR','VERMOGEN_NOMINAAL_CAPACITEIT','LAT','LONG']]

peak_consumption = []
years = []
result_cp = result.copy()
for year in range(2017, 2028):
    peak_consumption.extend(stations[f'FORECAST_SOLAR_PEAK_{year}'].values.tolist())
    years.extend([f'{year}-01-01T00:00:00Z']*len(stations[f'FORECAST_SOLAR_PEAK_{year}']))
    if year != 2027:
        result = result.append(result_cp)

result['PEAK_CONSUMPTION'] = peak_consumption
result['PEAK_LOAD'] = result.PEAK_CONSUMPTION / result.VERMOGEN_NOMINAAL_CAPACITEIT
result['YEAR'] = years

# Add bogus row with min/max value for proper scaling in arcgis
for year in range(2017, 2028):
    for value in [0, 10]:
        row = {
            'YEAR': f'{year}-01-01T00:00:00Z',
            'BOUWJAAR': 2000.0,
            'Gemeente': 'Groningen',
            'LAT': 0,
            'LONG': 0,
            'PEAK_CONSUMPTION': 92.344915214265725,
            'STATIONSNUMMER': 'baselines',
            'VERMOGEN_NOMINAAL_CAPACITEIT': 630,
            'PEAK_LOAD': value
        }
        result = result.append(row, ignore_index=True)
result.to_csv('stations_layer.csv', index=False)
