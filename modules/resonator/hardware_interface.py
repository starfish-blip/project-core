import time

try:
    import serial
    SERIAL_AVAILABLE = True
except ImportError:
    SERIAL_AVAILABLE = False

class SignalGeneratorInterface:
    def __init__(self, port="COM3", baudrate=9600):
        self.port = port
        self.baudrate = baudrate
        self.connection = None

    def connect(self):
        if not SERIAL_AVAILABLE:
            print("[-] PySerial not installed. Running in simulation mode.")
            return False
        try:
            self.connection = serial.Serial(self.port, self.baudrate, timeout=1)
            time.sleep(2)
            print(f"[+] Connected to signal generator on {self.port}")
            return True
        except Exception as e:
            print(f"[-] Connection failed on {self.port}: {e}")
            return False

    def send_frequency_command(self, frequency, waveform="sine"):
        # Standard command formatting for frequency generators
        command = f"FREQ:{frequency};WAVE:{waveform}\n"
        if self.connection and self.connection.is_open:
            self.connection.write(command.encode('utf-8'))
            print(f"[+] Sent hardware command: {command.strip()}")
        else:
            print(f"[simulated] Hardware command -> {command.strip()}")

if __name__ == "__main__":
    interface = SignalGeneratorInterface()
    if interface.connect():
        interface.send_frequency_command(272.0, "sine")
    else:
        interface.send_frequency_command(272.0, "sine")
