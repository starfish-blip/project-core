class HardwareInterface:
    def __init__(self, port=None):
        self.port = port
        self.connected = False

    def connect(self):
        # Placeholder for physical hardware handshake
        self.connected = True
        return self.connected

    def transmit_waveform(self, samples):
        if not self.connected:
            raise ConnectionError('Hardware interface not connected.')
        # Transmission logic placeholder
        return len(samples)
