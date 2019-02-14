a = {
  "coord": {
    "lon": 127.38,
    "lat": 36.35
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "맑음",
      "icon": "01d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 279.66,
    "pressure": 1029,
    "humidity": 41,
    "temp_min": 279.15,
    "temp_max": 280.15
  },
  "visibility": 10000,
  "wind": {
    "speed": 1,
    "deg": 20
  },
  "clouds": {
    "all": 1
  },
  "dt": 1550128800,
  "sys": {
    "type": 1,
    "id": 5506,
    "message": 0.0045,
    "country": "KR",
    "sunrise": 1550096389,
    "sunset": 1550135399
  },
  "id": 1835235,
  "name": "Daejeon",
  "cod": 200
}
print(a["coord"])