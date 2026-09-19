from modules.resonator.core import ResonatorCore
from modules.resonator.logger import ResonatorLogger
from modules.resonator.waveform import WaveformController
from modules.resonator.hardware_interface import SignalGeneratorInterface

def execute_resonator_cycle():
    print("=== COSMIC RESONATOR MASTER CYCLE ===")
    
    # 1. Initialize Core & Parameters
    core = ResonatorCore(base_freq=272.0)
    logger = ResonatorLogger()
    waveform = WaveformController(base_freq=core.base_freq)
    hardware = SignalGeneratorInterface(port="COM3")

    # 2. Configure Waveform & Target Frequency
    target_freq = core.calculate_harmonic(1.0)
    waveform.configure_output("sine", target_freq)

    # 3. Send Hardware Signal & Log Telemetry
    hardware.connect()
    hardware.send_frequency_command(target_freq, "sine")
    
    logger.record_frequency(core.base_freq, 1.0, "Master cycle execution nominal")
    print("=====================================")

if __name__ == "__main__":
    execute_resonator_cycle()
