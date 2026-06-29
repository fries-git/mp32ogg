from pathlib import Path
from ffprobe import FFProbe as prb
import ffmpeg
from pathlib import Path

validtypes = [
    ".mp3",
    ".webm",
    ".mp4",
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