import requests

# URL de la API (asegúrate de que Flask esté corriendo)
URL = "https://metodo-euller-production.up.railway.app/euler/"

# Datos de la ecuación diferencial
data = {
    "x0": 1,
    "y0": 1,
    "xf": 1.5,
    "n": 5,
    "edo": "0.2 - x - y"
}

# Enviar petición POST
response = requests.post(URL, json=data)

# Mostrar respuesta
if response.status_code == 200:
    print("📡 Respuesta de la API:")
    print(response.json())
else:
    print("❌ Error:", response.status_code, response.text)
