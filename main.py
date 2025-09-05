import os
import eel
import platform
import subprocess

eel.init('www')

url = "http://localhost:8000/index.html"

if platform.system() == "Darwin":  # Mac
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    subprocess.Popen([chrome_path, "--app=" + url])
elif platform.system() == "Windows":
    os.system(f'start chrome --args --app="{url}"')

eel.start('index.html', mode=None, host='localhost', port=8000, block=True)