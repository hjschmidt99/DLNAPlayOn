import sys
import os
import json
import clipboard
import subprocess
import traceback
import socket

pyscript = sys.argv[0]

def isPortOpen(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((ip, port))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False
    finally:
        sock.close()

def localIp():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = "127.0.0.1"
    try:
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
    finally:
        sock.close()
    return ip

if __name__ == "__main__":
    try:
        argv = sys.argv
        #argv = ["", r"D:\Download\Media\temp\q1.ts", r"D:\Download\Media\temp\q2.ts"]
        if len(argv) == 1:
            argv = ["", clipboard.paste().strip()]

        port = 8000
        tv = "[TV] Samsung 5 Series (40)"

        ip = localIp()
        running = isPortOpen(ip, port)

        # write playlist
        fname = pyscript + ".m3u8"
        with open(fname, 'a' if running else 'w', encoding="utf-8") as f:
            f.write("\n".join(argv[1:]) + "\n")

        if not running:
            # start minimized
            cmd = f'cmd.exe /c start /min python.exe PlayOn.py c -v 2 -p {port} -n "{tv}" -j "{ip}" -o "{fname}"'
            print(cmd)
            subprocess.Popen(cmd)

    except:
        traceback.print_exc()
        input("...")

    #input("...")
