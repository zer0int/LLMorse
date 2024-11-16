import numpy as np
import wave
import os

# Generates sine tones to test the 'hearing' of your AI. **If** it plays along. 
# But can also be used as example to generate synthetic morse 'beeps'.
# It seems multimodal LLM are attuned to human voice, though.
# GPT-4o Voice didn't 'hear' CB morse code beeps (high frequency).

# Parameters for the sweep
DURATION = 0.5  # Duration of each tone in seconds
SAMPLE_RATE = 44100  # Samples per second
STEPS = 20  # Number of frequency steps
FREQ_START = 20  # Starting frequency (Hz)
FREQ_END = 20000  # Ending frequency (Hz)
OUTPUT_DIR = "frequency_tones"  # Directory to save the .wav files

def generate_tone(frequency, duration, sample_rate):
    """
    Generate a sine wave tone at a given frequency and duration.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    tone = np.sin(2 * np.pi * frequency * t)
    # Normalize to 16-bit PCM range
    tone = (tone * 32767).astype(np.int16)
    return tone

def save_tone_as_wav(tone, frequency, sample_rate, output_dir):
    """
    Save a generated tone to a .wav file with the frequency in the filename.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    filename = f"{int(frequency)}Hz.wav"
    filepath = os.path.join(output_dir, filename)
    with wave.open(filepath, 'w') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(tone.tobytes())
    print(f"Saved: {filepath}")

def frequency_sweep_and_save(f_start, f_end, steps, duration, sample_rate, output_dir):
    """
    Generate and save frequency sweep tones as .wav files.
    """
    frequencies = np.logspace(np.log10(f_start), np.log10(f_end), steps)  # Logarithmic scale
    for freq in frequencies:
        print(f"Generating tone for frequency: {int(freq)} Hz")
        tone = generate_tone(freq, duration, sample_rate)
        save_tone_as_wav(tone, freq, sample_rate, output_dir)

if __name__ == "__main__":
    print("Generating and saving frequency tones...")
    frequency_sweep_and_save(FREQ_START, FREQ_END, STEPS, DURATION, SAMPLE_RATE, OUTPUT_DIR)
    print(f"All tones saved in directory: {OUTPUT_DIR}")
