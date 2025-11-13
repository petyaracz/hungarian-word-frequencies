import urllib.request
import os

if not os.path.exists('frequencies.db'):
    print("Downloading database...")
    urllib.request.urlretrieve(
        "https://huggingface.co/datasets/petyaracz/hungarian-word-frequencies/resolve/main/frequencies.db",
        "frequencies.db"
    )
    print("Download complete")
else:
    print("Database already exists, skipping download")
