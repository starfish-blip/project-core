# AROHA Framework: Advanced Acoustic Resonance Analyzer
import math

class AcousticAnalyzer:
    def __init__(self, reference_hz=272.0):
        self.reference = reference_hz
        print(f"[Acoustic Analyzer] Initialized with reference: {self.reference} Hz")

    def analyze_spectrum_deviation(self, measured_frequencies):
        report = {}
        for idx, freq in enumerate(measured_frequencies, start=1):
            deviation = freq - self.reference
            report[f"Node-{idx}"] = {
                "measured": freq,
                "deviation": round(deviation, 2),
                "aligned": abs(deviation) <= 2.0
            }
        return report

if __name__ == "__main__":
    analyzer = AcousticAnalyzer()
    samples = [271.5, 273.0, 280.2, 272.1]
    for node, data in analyzer.analyze_spectrum_deviation(samples).items():
        print(f"  {node} -> Measured: {data['measured']} Hz | Deviation: {data['deviation']} Hz | Aligned: {data['aligned']}")