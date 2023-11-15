import subprocess
from flask import Flask, request, send_from_directory
WHITE_BG = '\033[107m'
BLACK = '\033[30m'
RESET = '\033[0m'
WHITE = '\033[97m'
RED_BG = '\033[41m'
ORANGE_BG = '\033[48;5;202m'

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/status', methods=['POST'])
def status():
    data = request.get_json()
    status = data.get('status')
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    print('Status:', status)
    print('Latitude:', latitude)
    print('Longitude:', longitude)

    # Lakukan operasi lainnya dengan informasi geolokasi yang diterima

    return 'OK'

@app.route('/<path:filename>')
def serve_static(filename):
    root_dir = '.'
    return send_from_directory(root_dir, filename)

if __name__ == '__main__':
    port = input(BLACK + WHITE_BG + "Masukkan nomor port: " + RESET)
    subprocess.run(["python3", "stream/streamlink.py", port])  # Menjalankan streamlink.py sebagai subprocess dengan port sebagai argumen
    app.run(port=port, debug=False)  # Nonaktifkan mode debug Flask
