import http.client
import json
conn = http.client.HTTPSConnection("weather-api167.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "f3ee422cdamsh75001f0a349e28ap1dd6f1jsn69f495dc850e",
    'x-rapidapi-host': "weather-api167.p.rapidapi.com",
    'Accept': "application/json"
}

conn.request("GET", "/api/weather/forecast?place=Enugu&units=standard&type=three_hour&mode=json&lang=en", headers=headers)

res = conn.getresponse()
data = res.read()

weather_data = json.loads(data.decode("utf-8"))
print= ("lat:", weather[coord][lat]) 