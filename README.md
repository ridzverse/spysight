```text
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⣴⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⠿⠛⠋⠉⠁⠀⠀⠀⠈⠙⠻⢷⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣤⣾⡿⠋⠁⠀⣠⣶⣿⡿⢿⣷⣦⡀⠀⠀⠀⠙⠿⣦⣀⠀⠀⠀⠀
⠀⠀⢀⣴⣿⡿⠋⠀⠀⢀⣼⣿⣿⣿⣶⣿⣾⣽⣿⡆⠀⠀⠀⠀⢻⣿⣷⣶⣄⠀  
⠀⣴⣿⣿⠋⠀⠀⠀⠀⠸⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⠀⠀⠀⠐⡄⡌⢻⣿⣿⡷  © 2023 by @SpySight
⢸⣿⣿⠃⢂⡋⠄⠀⠀⠀⢿⣿⣿⣿⣿⣿⣯⣿⣿⠏⠀⠀⠀⠀⢦⣷⣿⠿⠛⠁  supported by openai.com
⠀⠙⠿⢾⣤⡈⠙⠂⢤⢀⠀⠙⠿⢿⣿⣿⡿⠟⠁⠀⣀⣀⣤⣶⠟⠋⠁⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠿⣾⣠⣆⣅⣀⣠⣄⣤⣴⣶⣾⣽⢿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠙⠋⠉⠉

```
<img title="INSTAHACK" src="https://img.shields.io/badge/CODENAME%20-SPYSIGHT-SCRIPT?colorA=dove&colorB=cyan&style=for-the-badge"> <img title="SPYSIGHT" src="https://img.shields.io/badge/VERSION%20-1.0.0-SCRIPT?colorA=dove&colorB=cyan&style=for-the-badge"> 

SpySight is a CLI-based tool with complete Spying Method
This tool can create Backdoor in jpg format, which will later request permission of camera, microphone, location and get all the informations directly in your terminal

This tool is available for Termux Android, Kali linux and Python 3.11

### installation
Quick installation for Termux Android
````bash
pkg update -y && pkg upgrade -y && pkg install git python3 cloudflared php ffmpeg && git clone https://github.com/spysight/spysight && cd spysight && git pull && pip install -r requirements.txt && python3 start.py
````

Quick installation for kali linux or WSL
````bash
pkg update -y && pkg upgrade -y && pkg install git python3 php ffmpeg wget dpkg && wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb && chmod +x cloudflared-linux-amd64.deb && sudo dpkg -i cloudflared-linux-amd64.deb && git clone https://github.com/ridzverse/spysight && cd spysight && git pull && pip install -r requirements.txt && python3 start.py
````
you can choose other compatible [Cloudflared](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/) files for your kali linux

### authentication 
Require A Key Code From Author [@ridzwanirawan](https://instagram.com/ridzwanirawan)

### features
- Image Backdoor Customization
- Webcam Snap
- Webcam Stream
- Microphone Sniffing

### what's new ?
Latest update instahack ```v1.0.0```
- Microphone Sniffing
- Watchdog Inspired UI

### contributes
- code by [@ridzwanirawan](https://instagram.com/ridzwanirawan)

### license
```text
MIT License

Copyright (c) 2023 SpySight©

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
