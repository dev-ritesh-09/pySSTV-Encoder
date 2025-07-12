import subprocess
import sys
import os

input_audio = "output.wav"
output_image = "decoded.png"
docker_image = "ghcr.io/8cH9azbsFifZ/sstv-decoder:latest"

# Ensure input file exists
if not os.path.exists(input_audio):
    print(f"❌ Input audio file '{input_audio}' not found.")
    sys.exit(1)

# Build the docker command
cmd = [
    "docker", "run", "--rm",
    "-v", f"{os.getcwd()}:/data",
    docker_image,
    f"/data/{input_audio}",
    f"/data/{output_image}"
]

try:
    print("⏳ Decoding SSTV audio using Docker...")
    subprocess.run(cmd, check=True)
    print(f"✅ Decoded image saved as {output_image}")
except subprocess.CalledProcessError as e:
    print("❌ Decoding failed:", e)
    sys.exit(1) 