import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from modules.resonator.waveform import generate_sine_wave
from modules.resonator.logger import log_event
from modules.resonator.hardware_interface import HardwareInterface

if __name__ == '__main__':
    freq = 440.0
    duration = 1.0
    
    # 1. Generate Waveform
    samples = generate_sine_wave(freq, duration_sec=duration)
    log_event('WAVEFORM_GENERATED', {'frequency': freq, 'duration': duration, 'sample_count': len(samples)})
    
    # 2. Transmit via Hardware Interface
    hw = HardwareInterface(port='COM3')
    hw.connect()
    transmitted_count = hw.transmit_waveform(samples)
    log_event('WAVEFORM_TRANSMITTED', {'port': hw.port, 'transmitted_samples': transmitted_count})
    
    print(f'Successfully generated and transmitted {transmitted_count} samples for {freq}Hz.')
