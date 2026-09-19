import math

def validate_frequency(freq):
    return isinstance(freq, (int, float)) and 20.0 <= freq <= 20000.0

def generate_sine_wave(freq, duration_sec=1.0, sample_rate=44100, amplitude=1.0):
    if not validate_frequency(freq):
        raise ValueError('Invalid frequency')
    num_samples = int(sample_rate * duration_sec)
    return [amplitude * math.sin(2 * math.pi * freq * i / sample_rate) for i in range(num_samples)]

def generate_frequency_sweep(start_freq, end_freq, duration_sec=1.0, sample_rate=44100):
    if not (validate_frequency(start_freq) and validate_frequency(end_freq)):
        raise ValueError('Invalid sweep frequencies')
    num_samples = int(sample_rate * duration_sec)
    samples = []
    for i in range(num_samples):
        t = i / sample_rate
        # Linear frequency interpolation over time
        current_freq = start_freq + (end_freq - start_freq) * (i / num_samples)
        samples.append(math.sin(2 * math.pi * current_freq * t))
    return samples
