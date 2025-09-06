import os
import eel
import platform
import subprocess

from engine.features import play_assistant_sound
from engine.command import take_command, speak_text

eel.init('www')

play_assistant_sound()

url = "http://localhost:8000/index.html"

if platform.system() == "Darwin":  # Mac
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    subprocess.Popen([chrome_path, "--app=" + url])
elif platform.system() == "Windows":
    os.system(f'start chrome --args --app="{url}"')

eel.start('index.html', mode=None, host='localhost', port=8000, block=True)