from io import BytesIO
import requests
from PIL import Image

url = "https://" + input("URL'yi Giriniz: ")

endpoint = "https://api.qrserver.com/v1/create-qr-code/"

orn = f"?data={url}&amp;size=500x500"
color = "&color=556B2F"

response = requests.get(endpoint + orn + color)

img = Image.open(BytesIO(response.content))

img.save("qr.png")