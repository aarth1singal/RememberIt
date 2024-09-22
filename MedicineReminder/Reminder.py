from gpiozero import PWMOutputDevice
from time import sleep

# Connect your speaker to GPIO 12
speaker = PWMOutputDevice(16)

# Define note frequencies in Hz
notes = {
    'C': 261.63,
    'D': 293.66,
    'E': 329.63,
    'F': 349.23,
    'G': 392.00,
    'A': 440.00,
    'B': 493.88,
    'C2': 523.25,
}
# Fetch data and time from the database

# Define the melody
melody = [
    ('C', 0.5), ('C', 0.5), ('G', 0.5), ('G', 0.5), 
    ('A', 0.5), ('A', 0.5), ('G', 1.0),
    ('F', 0.5), ('F', 0.5), ('E', 0.5), ('E', 0.5), 
    ('D', 0.5), ('D', 0.5), ('C', 1.0)
]

def play_note(note, duration):
    if note in notes:
        frequency = notes[note]
        speaker.value = 0.5  # Set volume (0.0 to 1.0)
        speaker.frequency = frequency
        sleep(duration)
        speaker.value = 0  # Stop the note
        sleep(0.1)  # Short pause between notes

# Main loop to play the song
try:
    while True:
        for note, duration in melody:
            play_note(note, duration)
        sleep(2)  # Pause between loops
except KeyboardInterrupt:
    speaker.value = 0  # Stop the sound





