import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
WHITE_BG = '\033[107m'
BLACK = '\033[30m'
RESET = '\033[0m'
WHITE = '\033[97m'
RED_BG = '\033[41m'
ORANGE_BG = '\033[48;5;202m'
class NewImageHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        if event.src_path.endswith(".jpg") or event.src_path.endswith(".jpeg"):
            print(WHITE + RED_BG + " [ ◉¯] " + BLACK + WHITE_BG + "Gambar diterima:" + RESET , event.src_path)
            subprocess.run(["python3", "info.py"]) # Menjalankan info.py

def monitor_folder(path):
    event_handler = NewImageHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    folder_path = "captured"  # Ganti dengan path folder "captured" yang sesuai
    monitor_folder(folder_path)
