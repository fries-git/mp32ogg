import tkinter as tk
from tkinter import filedialog
from functions import process
from ffprobe import FFProbe as prb
import ffmpeg
from pathlib import Path

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