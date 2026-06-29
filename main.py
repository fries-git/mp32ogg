import tkinter as tk
from tkinter import filedialog

from ffprobe import FFProbe as prb
import ffmpeg
from pathlib import Path

validtypes = [
    ".mp3",
    ".wav",
    ".flac",
    ".aac",
    ".m4a",
    ".wma",
    ".aiff",
    ".ogg",
    ".aif",
    ".opus",
    ".oga",
    ".ac3",
    ".eac3",
    ".amr",
    ".ape",
    ".alac",
    ".au",
    ".caf",
    ".dts",
    ".mka",
    ".mp2",
    ".mp1",
    ".ra",
    ".rm",
    ".tta",
    ".voc",
    ".wv",
    ".8svx",
    ".snd"
]

def process(file):
    output = Path(file).with_suffix(".ogg")
    if Path(file).suffix in validtypes: 
        if not Path(file).suffix == ".ogg":
            try:
                print(f"Processing file: {Path(file).name}")
                probe = prb(file)
                for stream in probe.streams:
                    print(f"Duration: {stream.duration}")
                (
                    ffmpeg
                    .input(str(file))
                    .output(str(output), format="ogg", acodec="libvorbis")
                    .overwrite_output()
                    .run(quiet=True)
                )

            except ffmpeg.Error as e:
                print(f"Failed with FFMPEG error: {e}")
            except Exception as e:
                print(f"Failed with misc. error: {e}")

        else:
            print(f"File: {Path(file).name} is already ogg!")

    else:
        print(f"File: {Path(file).name} is not of supported type.")

print("Welcome to mp32ogg, I can't think of a clever acronym or name so eat my short.")

root = tk.Tk()
root.withdraw()

directory = Path(filedialog.askdirectory(title="Select folder to convert"))
confirm = input(f"Do you want to convert all files in {directory} to ogg? y/n: ")
if confirm.lower() == "y":
    print(f"Converting all files in {directory} to ogg.")

    files = [str(f) for f in directory.iterdir() if f.is_file()]

    for file in files:
        process(file)

    print("Done!")
else:
    print("Canceled.")

print("Thanks for using MP32OGG!")