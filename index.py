import argparse
import speech_recognition as sr

r = sr.Recognizer()

parser = argparse.ArgumentParser()
parser.add_argument('source_path', help="Path to the video or audio file to subtitle", nargs='?')
args = parser.parse_args()



harvard = sr.AudioFile(args.source_path)

with harvard as source:
     r.adjust_for_ambient_noise(source)
     audio = r.record(source)

print(r.recognize_google(audio,language='vi-VN'))
