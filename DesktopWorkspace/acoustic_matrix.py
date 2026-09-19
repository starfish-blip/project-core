# AROHA Framework: Acoustic Frequency & Resonance Handler
import math

class AcousticMatrix:
    def __init__(self, fundamental_hz=272.0):
        self.fundamental = fundamental_hz
        print(f"[Acoustic Matrix] Initialized with fundamental frequency: {self.fundamental} Hz")

    def generate_harmonic_scale(self):
        scale = {}
        notes = ["Root", "Semitone-2", "Semitone-4", "Semitone-5", "Octave"]
        for i, note in enumerate(notes):
            freq = self.fundamental * math.pow(2, i / 12.0)
            scale[note] = round(freq, 2)
        return scale

if __name__ == "__main__":
    matrix = AcousticMatrix()
    print("Harmonic Scale:", matrix.generate_harmonic_scale())