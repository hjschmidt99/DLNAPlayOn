import sys
import os
import json
import clipboard
import subprocess
import traceback
import socket

pyscript = sys.argv[0]

if __name__ == "__main__":
    try:
        argv = sys.argv
        #argv = ["", r"D:\Download\Media\temp\q1.ts", r"D:\Download\Media\temp\q2.ts"]
        if len(argv) == 1:
            argv = ["", clipboard.paste().strip()]

        fname = pyscript + ".m3u8"
        with open(fname, 'w', encoding="utf-8") as f:
            f.write("\n".join(argv[1:]))

        tv = "[TV] Samsung 5 Series (40)"
        #intf = "192.168.0.124"
        # find local ip
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        intf = s.getsockname()[0]
        s.close()

        # start minimized
        cmd = f'cmd.exe /c start /min python.exe PlayOn.py c -v 2  -n "{tv}" -j "{intf}" -o "{fname}"'
        print(cmd)
        subprocess.Popen(cmd)
    except:
        traceback.print_exc()
        input("...")

    #input("...")
