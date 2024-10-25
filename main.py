# Disable the built-in speaker and use pin 0 for audio output
music.set_built_in_speaker_enabled(False)

def play_extended_original_theme():
    melody = (
        # Part 1: Original theme
        "C4:4 E4:4 G4:4 F4:4 A4:8 G4:4 E4:4 C4:8 " +
        "D4:4 F4:4 A4:4 G4:4 B4:8 A4:4 F4:4 D4:8 " +
        "E4:4 G4:4 C5:4 B4:4 D5:8 C5:4 G4:4 E4:8 " +
        "C4:4 E4:4 G4:4 F4:4 A4:8 G4:4 E4:4 C4:8 " +

        # Part 2: Variation with higher notes
        "E4:4 G4:4 C5:4 A4:4 C5:8 B4:4 G4:4 E4:8 " +
        "F4:4 A4:4 C5:4 B4:4 D5:8 C5:4 A4:4 F4:8 " +
        "G4:4 B4:4 D5:4 C5:4 E5:8 D5:4 B4:4 G4:8 " +
        "E4:4 G4:4 C5:4 A4:4 C5:8 B4:4 G4:4 E4:8 " +

        # Part 3: Lower register variation
        "A3:4 C4:4 E4:4 D4:4 F4:8 E4:4 C4:4 A3:8 " +
        "B3:4 D4:4 F4:4 E4:4 G4:8 F4:4 D4:4 B3:8 " +
        "C4:4 E4:4 G4:4 F4:4 A4:8 G4:4 E4:4 C4:8 " +
        "A3:4 C4:4 E4:4 D4:4 F4:8 E4:4 C4:4 A3:8 " +

        # Part 4: Rhythmic variation
        "C4:2 E4:2 G4:2 F4:2 A4:4 G4:2 E4:2 C4:4 " +
        "D4:2 F4:2 A4:2 G4:2 B4:4 A4:2 F4:2 D4:4 " +
        "E4:2 G4:2 C5:2 B4:2 D5:4 C5:2 G4:2 E4:4 " +
        "C4:2 E4:2 G4:2 F4:2 A4:4 G4:2 E4:2 C4:4 " +

        # Part 5: Grand finale
        "C4:4 E4:4 G4:4 C5:4 E5:8 D5:4 B4:4 G4:8 " +
        "A4:4 C5:4 E5:4 D5:4 F5:8 E5:4 C5:4 A4:8 " +
        "G4:4 B4:4 D5:4 C5:4 E5:8 D5:4 B4:4 G4:8 " +
        "C5:4 G4:4 E4:4 C4:4 G4:8 E4:4 C4:4 C4:8"
    )
    
    music.play(music.string_playable(melody, 80), music.PlaybackMode.UNTIL_DONE)

def on_button_pressed_ab():
    play_extended_original_theme()

input.on_button_pressed(Button.AB, on_button_pressed_ab)

# Set the volume (0-255)
music.set_volume(127)