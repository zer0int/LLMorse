import os
import time
from pydub import AudioSegment
from simpleaudio import play_buffer

# Load short and long Morse code sounds
SHORT_PATH = "short.wav"
LONG_PATH = "long.wav"

# Morse code timing and mapping
DIT_DURATION = 0.08  # Short signal duration (seconds)
DAH_DURATION = 0.18  # Long signal duration (seconds)
PAUSE_BETWEEN_LETTERS = 0.25  # Pause between letters (seconds)
PAUSE_BETWEEN_WORDS = 0.45  # Pause between words (seconds)

# Morse code dictionary
MORSE_CODE = {
    'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".", 
    'F': "..-.", 'G': "--.", 'H': "....", 'I': "..", 'J': ".---", 
    'K': "-.-", 'L': ".-..", 'M': "--", 'N': "-.", 'O': "---", 
    'P': ".--.", 'Q': "--.-", 'R': ".-.", 'S': "...", 'T': "-", 
    'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-", 'Y': "-.--", 
    'Z': "--..", '1': ".----", '2': "..---", '3': "...--", '4': "....-", 
    '5': ".....", '6': "-....", '7': "--...", '8': "---..", '9': "----.", 
    '0': "-----", ' ': " "  # Space between words
}

# Cache loaded audio for fast playback
short_signal = AudioSegment.from_file(SHORT_PATH)
long_signal = AudioSegment.from_file(LONG_PATH)

# Playback function
def play_audio(segment):
    # Convert audio to raw data for playback
    playback = play_buffer(
        segment.raw_data,
        num_channels=segment.channels,
        bytes_per_sample=segment.sample_width,
        sample_rate=segment.frame_rate
    )
    playback.wait_done()

# Generate Morse code for a character
def morse_to_audio(morse_char):
    audio_sequence = []
    for symbol in morse_char:
        if symbol == '.':
            audio_sequence.append(short_signal)
        elif symbol == '-':
            audio_sequence.append(long_signal)
        audio_sequence.append(AudioSegment.silent(duration=DIT_DURATION * 1000))  # Pause between signals
    return sum(audio_sequence[:-1])  # Remove last unnecessary pause

# Main function
def text_to_morse_audio(input_text):
    for word in input_text.upper().split(" "):  # Split text into words
        for letter in word:  # Process each letter
            morse_char = MORSE_CODE.get(letter, "")
            if morse_char:
                audio_sequence = morse_to_audio(morse_char)
                play_audio(audio_sequence)
                time.sleep(PAUSE_BETWEEN_LETTERS)  # Pause between letters
        time.sleep(PAUSE_BETWEEN_WORDS)  # Pause between words

if __name__ == "__main__":
    while True:
        user_input = input("Enter Text (or type 'exit' to quit): ")
        if user_input.strip().lower() == 'exit':
            print("Exiting program.")
            break
        text_to_morse_audio(user_input)
