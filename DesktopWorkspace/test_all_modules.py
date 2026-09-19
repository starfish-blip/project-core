# AROHA & Bioneer: Master Integration Test Script
import os
import sys

def run_integration_tests():
    print("=" * 50)
    print("[Master Test] Starting AROHA & Bioneer Local Integration Test...")
    print("=" * 50)

    # Test 1: Duodecimal Engine
    try:
        from duodecimal_engine import DuodecimalEngine
        engine = DuodecimalEngine()
        angle = engine.compute_resonance_angle(3)
        print(f"[Test 1 PASSED] Duodecimal Engine node angle (3): {angle}°")
    except Exception as e:
        print(f"[Test 1 FAILED] Duodecimal Engine: {e}")

    # Test 2: Epistemic Translator
    try:
        from epistemic_translator import EpistemicTranslator
        translator = EpistemicTranslator()
        result = translator.translate_vector("Test Stream", "Zone-Alpha")
        print(f"[Test 2 PASSED] Epistemic Translator: {result}")
    except Exception as e:
        print(f"[Test 2 FAILED] Epistemic Translator: {e}")

    # Test 3: Matrix Resonance
    try:
        from matrix_resonance import calculate_harmonic_frequency
        freq = calculate_harmonic_frequency(272.0, 5)
        print(f"[Test 3 PASSED] Acoustic Resonance calculation: {freq} Hz")
    except Exception as e:
        print(f"[Test 3 FAILED] Matrix Resonance: {e}")

    print("=" * 50)
    print("[Master Test] All local module integration tests completed.")
    print("=" * 50)

if __name__ == "__main__":
    run_integration_tests()