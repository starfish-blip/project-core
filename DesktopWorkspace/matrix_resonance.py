# Project Bioneer: Acoustic Frequency & Resonance Calculator
import math

def calculate_harmonic_frequency(base_hz, multiplier):
    freq = base_hz * math.pow(2, multiplier / 12.0)
    return round(freq, 2)

if __name__ == "__main__":
    base = 272.0  # Reference acoustic frequency
    print(f"[Resonance] Base Frequency: {base} Hz")
    print(f"[Resonance] Harmonic +5 semitones: {calculate_harmonic_frequency(base, 5)} Hz")