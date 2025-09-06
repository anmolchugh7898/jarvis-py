from pydub import AudioSegment
from pydub.playback import play

def play_assistant_sound():
    music_dir = 'www/assets/audio/start_sound.mp3'
    sound = AudioSegment.from_mp3(music_dir)
    play(sound)
    print(f"Playing sound from: {music_dir}")
