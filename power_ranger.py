from pathlib import Path

dirs = {".png": "Images",
        ".jpeg": "Images",
        ".jpg": "Images",
        ".gif": "Images",
        ".mp4": "Videos",
        ".mov": "Videos",
        ".zip": "Archives",
        ".pdf": "Documents",
        ".txt": "Documents",
        "j.son": "Documents",
        ".mp3": "Musiques",
        ".wav": "Musiques"}

tri_dir = Path.home() / "Tri"
files = [f for f in tri_dir.iterdir() if f.is_file()]
for f in files:
	output_dir = tri_dir / dirs.get(f.suffix, "Autres")
	output_dir.mkdir(exist_ok=True)
	f.rename(output_dir / f.name)
