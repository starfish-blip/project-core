import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from modules.resonator.waveform import generate_sine_wave
from modules.resonator.logger import log_event

if __name__ == '__main__':
    freq = 440.0
    duration = 1.0
    samples = generate_sine_wave(freq, duration_sec=duration)
    log_event('WAVEFORM_GENERATED', {'frequency': freq, 'duration': duration, 'sample_count': len(samples)})
    print(f'Successfully generated {len(samples)} samples for {freq}Hz and logged telemetry.')
