import os
import subprocess

INPUT_DIR = "docs"
OUTPUT_DIR = "converted_md"
MEDIA_DIR = os.path.join(OUTPUT_DIR, "img")

os.makedirs(OUTPUT_DIR, exist_ok=True)

for file in os.listdir(INPUT_DIR):
    if file.lower().endswith(".docx"):
        input_path = os.path.join(INPUT_DIR, file)
        output_md = os.path.splitext(file)[0] + ".md"
        output_path = os.path.join(OUTPUT_DIR, output_md)

        print(f"[+] Converting: {file}")
        subprocess.run([
            "pandoc", input_path,
            "-o", output_path,
            f"--extract-media={MEDIA_DIR}"
        ])

print("[✔] Conversion completed with image extraction.")
