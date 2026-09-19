import math

def validate_frequency(freq):
    return isinstance(freq, (int, float)) and 20.0 <= freq <= 20000.0

def generate_sine_wave(freq, duration_sec=1.0, sample_rate=44100):
    if not validate_frequency(freq):
        raise ValueError('Invalid frequency')
    num_samples = int(sample_rate * duration_sec)
    return [math.sin(2 * math.pi * freq * i / sample_rate) for i in range(num_samples)]
