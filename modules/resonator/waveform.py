def validate_frequency(freq):
    return isinstance(freq, (int, float)) and 20.0 <= freq <= 20000.0

def generate_sine_wave(freq, duration_sec=1.0, sample_rate=44100):
    if not validate_frequency(freq):
        raise ValueError('Invalid frequency')
    return []
