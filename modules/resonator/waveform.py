def validate_frequency(freq):
    return isinstance(freq, (int, float)) and freq > 0

def generate_sine_wave(freq, duration=1.0):
    if not validate_frequency(freq):
        raise ValueError('Invalid frequency')
    return []
