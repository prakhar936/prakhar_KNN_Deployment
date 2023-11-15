import requests

url = "http://127.0.0.1:5000/predict_api"
r = requests.post(url,json={'battery_power':1021, 'px_height':905, 'px_width':1988, 'ram':2631})

print(r.json())