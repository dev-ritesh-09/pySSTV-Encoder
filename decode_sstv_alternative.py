import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal
import os
import sys

def analyze_sstv_audio(audio_file, output_image="decoded_analysis.png"):
    """
    Analyze SSTV audio and create a basic visualization
    This is not a full SSTV decoder, but shows the signal structure
    """
    try:
        # Read the audio file
        sample_rate, audio_data = wavfile.read(audio_file)
        
        # Convert to mono if stereo
        if len(audio_data.shape) > 1:
            audio_data = audio_data.mean(axis=1)
        
        # Normalize audio
        audio_data = audio_data / np.max(np.abs(audio_data))
        
        # Create time axis
        duration = len(audio_data) / sample_rate
        time = np.linspace(0, duration, len(audio_data))
        
        # Create spectrogram
        f, t, Sxx = signal.spectrogram(audio_data, sample_rate, nperseg=1024, noverlap=512)
        
        # Create the plot
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
        
        # Plot waveform
        ax1.plot(time, audio_data, linewidth=0.5)
        ax1.set_title('SSTV Audio Waveform')
        ax1.set_xlabel('Time (seconds)')
        ax1.set_ylabel('Amplitude')
        ax1.grid(True, alpha=0.3)
        
        # Plot spectrogram
        im = ax2.pcolormesh(t, f, 10 * np.log10(Sxx), shading='gouraud')
        ax2.set_title('SSTV Audio Spectrogram')
        ax2.set_xlabel('Time (seconds)')
        ax2.set_ylabel('Frequency (Hz)')
        ax2.set_ylim([0, 3000])  # SSTV typically uses 1500-2300 Hz
        fig.colorbar(im, ax=ax2, label='Power (dB)')
        
        plt.tight_layout()
        plt.savefig(output_image, dpi=150, bbox_inches='tight')
        plt.close()
        
        print(f"✅ Audio analysis saved as {output_image}")
        print(f"📊 Audio duration: {duration:.2f} seconds")
        print(f"📊 Sample rate: {sample_rate} Hz")
        print(f"📊 Frequency range: {f.min():.0f} - {f.max():.0f} Hz")
        
    except Exception as e:
        print(f"❌ Error analyzing audio: {e}")
        sys.exit(1)

if __name__ == "__main__":
    input_audio = "output.wav"
    
    if not os.path.exists(input_audio):
        print(f"❌ Input audio file '{input_audio}' not found.")
        print("💡 Make sure you've run sstv.py first to generate output.wav")
        sys.exit(1)
    
    print("🔍 Analyzing SSTV audio signal...")
    analyze_sstv_audio(input_audio)
    print("\n💡 Note: This is a signal analysis, not a full SSTV decoder.")
    print("💡 For full decoding, install Docker and use decode_sstv.py") 