class WaveformController:
    def __init__(self, base_freq=272.0):
        self.base_freq = base_freq
        self.supported_waves = ["sine", "square", "triangle", "sawtooth"]

    def configure_output(self, wave_type, frequency=None):
        if wave_type not in self.supported_waves:
            raise ValueError(f"Unsupported waveform: {wave_type}")
        
        target_freq = frequency if frequency else self.base_freq
        print(f"[+] Configuring generator: {wave_type.upper()} wave at {target_freq} Hz")
        return {"waveform": wave_type, "frequency": target_freq, "status": "configured"}

if __name__ == "__main__":
    ctrl = WaveformController()
    ctrl.configure_output("sine", 272.0)
