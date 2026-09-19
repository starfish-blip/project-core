# AROHA Framework: Acoustic Harmonic Frequency Filter

class AcousticHarmonicFilter:
    def __init__(self, target_fundamental=272.0, tolerance_hz=5.0):
        self.fundamental = target_fundamental
        self.tolerance = tolerance_hz
        print(f"[Acoustic Filter] Initialized. Target: {self.fundamental} Hz (±{self.tolerance} Hz)")

    def evaluate_frequency(self, measured_hz):
        difference = abs(measured_hz - self.fundamental)
        is_resonant = difference <= self.tolerance
        print(f"[Acoustic Filter] Evaluating {measured_hz} Hz -> Resonant: {is_resonant} (Delta: {round(difference, 2)} Hz)")
        return is_resonant

if __name__ == "__main__":
    filt = AcousticHarmonicFilter()
    filt.evaluate_frequency(274.5)
    filt.evaluate_frequency(290.0)