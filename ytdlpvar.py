import yt_dlp
from pathlib import Path
from functions import process

music_dir = Path("music")
music_dir.mkdir(exist_ok=True)
cookies = False # Leave as false for now while I figure out 18+ video downloading. If on, stuff like N.W.A should download but it just breaks.

def get_ydl():
    base_opts = {
        "outtmpl": str(music_dir / "%(title)s.%(ext)s"),

        # safer format selection (prevents "format not available")
        "format": "bestaudio/best",

        # IMPORTANT: modern YouTube fix
        "extractor_args": {
            "youtube": {
                "player_client": ["android", "web"],
            }
        },

        # stability improvements
        "retries": 10,
        "fragment_retries": 10,
        "noplaylist": False,
    }

    browsers = ["firefox", "chrome", "edge", "brave", "vivaldi", "opera"]

    if cookies is True:
        for browser in browsers:
            try:
                opts = {
                    **base_opts,
                    "cookiesfrombrowser": (browser,),
                }

                ydl = yt_dlp.YoutubeDL(opts)

                # safer check than touching cookiejar
                ydl.cookiejar  # triggers load attempt

                print(f"Using cookies from {browser}")
                return ydl

            except Exception:
                continue

        print("No browser cookies found.")
    return yt_dlp.YoutubeDL(base_opts)


def download(link):
    with get_ydl() as ydl:
        try:
            ydl.download([link])
        except Exception as e:
            print(e)

    # process only audio outputs safely
    for file in music_dir.iterdir():
        if file.is_file():
            process(file)


    for file in music_dir.iterdir():
        if file.is_file() and file.suffix.lower() != ".ogg":
            file.unlink()


link = input("Link to YouTube video/playist: ")
download(link)