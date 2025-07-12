# SSTV (Slow Scan Television) Encoder and Decoder

This project provides tools to encode images into SSTV audio signals and analyze/visualize SSTV audio files. SSTV is a method for transmitting still images via radio frequencies, commonly used in amateur radio.

## 📁 Project Structure

```
sstv/
├── sstv.py                    # Main encoder script
├── decode_sstv.py            # Docker-based decoder (requires Docker)
├── decode_sstv_alternative.py # Audio analysis and visualization
├── input.jpg                 # Input image to encode
├── output.wav                # Generated SSTV audio
├── decoded_analysis.png      # Audio signal analysis
└── README.md                 # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.13 or higher
- pip (Python package manager)

### Installation

1. **Clone or download this project**
2. **Install required Python packages:**
   ```bash
   pip install pysstv Pillow scipy matplotlib numpy
   ```

### Basic Usage

1. **Place your image** as `input.jpg` in the project directory
2. **Encode image to SSTV audio:**
   ```bash
   python3.13 sstv.py
   ```
3. **Analyze the generated audio:**
   ```bash
   python3.13 decode_sstv_alternative.py
   ```

## 📋 Detailed Usage

### 1. Image Encoding (`sstv.py`)

**Purpose:** Converts an image to SSTV audio format using the Martin M1 protocol.

**Features:**
- Automatically resizes images to 320x256 pixels (Martin M1 requirement)
- Converts to RGB color space
- Generates 44.1kHz, 16-bit mono WAV audio
- Uses Martin M1 SSTV mode (color, 114 seconds transmission time)

**Usage:**
```bash
python3.13 sstv.py
```

**Input:** `input.jpg` (any image format supported by PIL)
**Output:** `output.wav` (SSTV audio file)

**Technical Details:**
- **SSTV Mode:** Martin M1
- **Resolution:** 320x256 pixels
- **Sample Rate:** 44,100 Hz
- **Bit Depth:** 16-bit
- **Channels:** Mono
- **Transmission Time:** ~114 seconds

### 2. Audio Analysis (`decode_sstv_alternative.py`)

**Purpose:** Analyzes SSTV audio signals and creates visualizations.

**Features:**
- Waveform visualization
- Spectrogram analysis
- Frequency range analysis (0-3000 Hz focus)
- Audio duration and sample rate reporting

**Usage:**
```bash
python3.13 decode_sstv_alternative.py
```

**Input:** `output.wav` (SSTV audio file)
**Output:** `decoded_analysis.png` (analysis visualization)

**What the analysis shows:**
- **Waveform:** Audio amplitude over time
- **Spectrogram:** Frequency content over time
- **SSTV Frequency Range:** 1500-2300 Hz (typical SSTV frequencies)

### 3. Full Decoding (`decode_sstv.py`)

**Purpose:** Decodes SSTV audio back to images using Docker.

**Requirements:**
- Docker Desktop installed and running
- Internet connection (to download Docker image)

**Usage:**
```bash
python3.13 decode_sstv.py
```

**Input:** `output.wav` (SSTV audio file)
**Output:** `decoded.png` (reconstructed image)

## 🔧 Installation Guide

### Step 1: Install Python Dependencies

```bash
# Install all required packages
pip install pysstv Pillow scipy matplotlib numpy
```

### Step 2: Verify Installation

```bash
# Test Python imports
python3.13 -c "import pysstv, PIL, scipy, matplotlib, numpy; print('✅ All packages installed successfully!')"
```

### Step 3: Prepare Your Image

1. Place your image file as `input.jpg` in the project directory
2. Supported formats: JPEG, PNG, BMP, TIFF, etc.
3. The script will automatically resize it to 320x256 pixels

## 📊 Understanding SSTV

### What is SSTV?

Slow Scan Television (SSTV) is a method for transmitting still images via radio frequencies. It's commonly used in:
- Amateur radio communications
- Space missions (ISS, satellites)
- Emergency communications
- Educational demonstrations

### SSTV Modes

This project uses **Martin M1** mode:
- **Type:** Color SSTV
- **Resolution:** 320x256 pixels
- **Transmission Time:** ~114 seconds
- **Frequency Range:** 1500-2300 Hz
- **Color Encoding:** RGB

### Signal Structure

SSTV signals consist of:
1. **Vis Header:** Identifies the SSTV mode
2. **Image Data:** Pixel information encoded as audio frequencies
3. **Sync Pulses:** Timing synchronization signals

## 🛠️ Troubleshooting

### Common Issues

#### 1. "No module named 'pysstv'"
```bash
# Solution: Install pysstv
pip install pysstv
```

#### 2. "No module named 'numpy'"
```bash
# Solution: Install numpy and other dependencies
pip install numpy scipy matplotlib
```

#### 3. "Image file not found"
- Ensure `input.jpg` exists in the project directory
- Check file permissions
- Verify the image file is not corrupted

#### 4. "Docker not found" (for decode_sstv.py)
- Install Docker Desktop for Mac: https://www.docker.com/products/docker-desktop/
- Start Docker Desktop
- Ensure Docker is running before executing the script

#### 5. Python Version Issues
- Use `python3.13` instead of `python3` if you have multiple Python versions
- Verify your Python version: `python3.13 --version`

### Performance Tips

1. **Image Optimization:**
   - Use JPEG format for photos
   - Use PNG format for graphics/text
   - Keep file sizes reasonable (< 1MB)

2. **Audio Quality:**
   - The generated WAV file will be ~10-15MB for a 114-second transmission
   - Ensure sufficient disk space

3. **Processing Time:**
   - Encoding: ~1-2 seconds
   - Analysis: ~5-10 seconds
   - Full decoding (with Docker): ~30-60 seconds

## 🔬 Advanced Usage

### Customizing SSTV Parameters

Edit `sstv.py` to modify:
- **SSTV Mode:** Change `MartinM1` to other modes (Scottie1, Robot36, etc.)
- **Sample Rate:** Modify the `44100` parameter
- **Bit Depth:** Change the `16` parameter

### Batch Processing

Create a script to process multiple images:

```python
import os
from sstv import encode_image

for image_file in os.listdir('images/'):
    if image_file.endswith(('.jpg', '.png')):
        encode_image(f'images/{image_file}', f'output_{image_file}.wav')
```

### Audio Playback

To play the generated SSTV audio:
```bash
# Using afplay (macOS)
afplay output.wav

# Using ffplay (if FFmpeg is installed)
ffplay output.wav
```

## 📚 Technical Details

### File Formats

- **Input Images:** JPEG, PNG, BMP, TIFF, etc. (PIL supported)
- **Output Audio:** WAV format, 44.1kHz, 16-bit, mono
- **Analysis Output:** PNG format, high-resolution plots

### Audio Specifications

- **Sample Rate:** 44,100 Hz
- **Bit Depth:** 16-bit
- **Channels:** Mono
- **Format:** WAV (uncompressed)

### Image Specifications

- **Resolution:** 320x256 pixels (Martin M1 requirement)
- **Color Space:** RGB
- **Aspect Ratio:** 5:4

## 🤝 Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source. Feel free to use, modify, and distribute.

## 🔗 Useful Links

- [PySSTV Documentation](https://pypi.org/project/pysstv/)
- [SSTV Modes Reference](https://en.wikipedia.org/wiki/Slow-scan_television)
- [Amateur Radio SSTV](https://www.arrl.org/sstv)
- [Docker Documentation](https://docs.docker.com/)

## 📞 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Verify all dependencies are installed
3. Ensure you're using the correct Python version
4. Check file permissions and disk space

For additional help, please provide:
- Error messages
- Python version (`python3.13 --version`)
- Operating system details
- Steps to reproduce the issue # pySSTV-Encoder
