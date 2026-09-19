import pytest
from modules.resonator.waveform import validate_frequency, generate_sine_wave

def test_validate_frequency():
    assert validate_frequency(440.0) is True
    assert validate_frequency(20.0) is True
    assert validate_frequency(20000.0) is True
    assert validate_frequency(10.0) is False
    assert validate_frequency(25000.0) is False

def test_generate_sine_wave():
    buffer = generate_sine_wave(440.0, duration_sec=0.1, sample_rate=1000)
    assert len(buffer) == 100
    assert all(-1.0 <= sample <= 1.0 for sample in buffer)
