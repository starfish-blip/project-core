import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from modules.resonator.waveform import generate_sine_wave, generate_frequency_sweep
from modules.resonator.logger import log_event
from modules.resonator.hardware_interface import HardwareInterface

if __name__ == '__main__':
    hw = HardwareInterface(port='COM3')
    hw.connect()

    # Batch test frequencies and sweep
    test_frequencies = [110.0, 220.0, 440.0, 880.0]
    
    for freq in test_frequencies:
        samples = generate_sine_wave(freq, duration_sec=0.5, amplitude=0.8)
        log_event('WAVEFORM_GENERATED', {'type': 'sine', 'frequency': freq, 'sample_count': len(samples)})
        transmitted = hw.transmit_waveform(samples)
        log_event('WAVEFORM_TRANSMITTED', {'type': 'sine', 'frequency': freq, 'transmitted_samples': transmitted})

    # Run frequency sweep loop
    sweep_samples = generate_frequency_sweep(200.0, 2000.0, duration_sec=1.0)
    log_event('SWEEP_GENERATED', {'start': 200.0, 'end': 2000.0, 'sample_count': len(sweep_samples)})
    sweep_transmitted = hw.transmit_waveform(sweep_samples)
    log_event('SWEEP_TRANSMITTED', {'transmitted_samples': sweep_transmitted})

    print(f'Completed automated batch loop: 4 sine tones and 1 sweep transmitted successfully.')
