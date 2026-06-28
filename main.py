import tkinter as tk
from tkinter import filedialog
import ffmpeg as ffmpreg
from pathlib import Path

def process(file):
    output = Path(file).with_suffix(".ogg")
    print(f"Processing file: {file}")

    try:
        (
            ffmpreg
            .input(str(file))
            .output(str(output), format="ogg", acodec="libvorbis")
            .overwrite_output()
            .run(quiet=True)
        )

    except ffmpreg.Error as e:
        print(f"Failed with FFMPEG error: {e}")

    except Exception as e:
        print(f"Failed with misc. error: {e}") 

print("Welcome to mp32ogg, I can't think of a clever acronym or name so eat my short.")

root = tk.Tk()
root.withdraw()

directory = Path(filedialog.askdirectory(title="Select a Folder"))
print(f"Converting all files in {directory} to ogg.")

files = [str(f) for f in directory.iterdir() if f.is_file()]

for file in files:
    process(file)

print("Done!")