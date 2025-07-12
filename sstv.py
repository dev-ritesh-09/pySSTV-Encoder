from pysstv.color import MartinM1
from PIL import Image
import os

# Path to your input image
input_image_path = "input.jpg"
output_audio_path = "output.wav"

# --- Step 1: Load and Resize Image ---
try:
    image = Image.open(input_image_path).convert("RGB")
    # SSTV Martin M1 requires 320x256 resolution
    image = image.resize((320, 256))
except FileNotFoundError:
    print(f"Error: Image file '{input_image_path}' not found.")
    exit(1)

# --- Step 2: Create SSTV Object ---
sstv = MartinM1(image, 44100, 16)

# --- Step 3: Write to WAV File ---
sstv.write_wav(output_audio_path)

print(f"✅ SSTV audio generated: {output_audio_path}")
