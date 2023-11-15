import requests
WHITE_BG = '\033[107m'
BLACK = '\033[30m'
RESET = '\033[0m'
WHITE = '\033[97m'
RED_BG = '\033[41m'
ORANGE_BG = '\033[48;5;202m'
# Membuka file lokasi.txt
with open("snap/location.txt") as f:
    # Membaca isi file dan memisahkan latitude dan longitude
    lat, lng = f.readline().strip().split(",")

# Membuat URL untuk Google Maps API
url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key=AIzaSyDBhP8uo2vGsmHBm0rYwstuZtncB8STEPY&result_type=street_address"

# Mengirim permintaan ke Google Maps API
response = requests.get(url)

# Mengekstrak informasi alamat dari respons JSON
if "results" in response.json() and len(response.json()["results"]) > 0:
    address = response.json()["results"][0]["formatted_address"]
    # Mencetak informasi koordinat dan alamat
    print(f"Koordinat: {lat}, {lng}")
    print(f"Alamat: {address}")
else:
    # Menggunakan API alternatif jika tidak berhasil dengan Google Maps API
    # Anda perlu memperoleh API key terlebih dahulu dari provider alternatif
    url = f"https://api.opencagedata.com/geocode/v1/json?key=2a6cd6c7d2364fe89c7c8439f90627d2&q={lat}+{lng}"
    response = requests.get(url)

    if "results" in response.json() and len(response.json()["results"]) > 0:
        address = response.json()["results"][0]["formatted"]
        # Mencetak informasi koordinat dan alamat
        print(f"Koordinat: {lat}, {lng}")
        print(f"Alamat: {address}")
    else:
        print("Tidak dapat menemukan alamat untuk koordinat tersebut.")
