import requests
import json


jma_url = "https://www.jma.go.jp/bosai/forecast/data/forecast/220000.json"
jma_json = requests.get(jma_url).json()

jma_data = jma_json[0]["timeSeries"][0]["timeDefines"][0]
jma_area = jma_json[0]["timeSeries"][0]["areas"][1]["area"]["name"]
jma_weather = jma_json[0]["timeSeries"][0]["areas"][1]["weathers"][0]
jma_rainfall = jma_json[0]["timeSeries"][1]["areas"][1]["pops"]

jma_weather = jma_weather.replace(' ' ,'')

print(jma_data)
print(f'静岡県{jma_area}')
print(f'今日の天気:{jma_weather}')
print(f'降水確率:{jma_rainfall}')