import pytest
from modules.resonator.hardware_interface import HardwareInterface

def test_hardware_connection():
    hw = HardwareInterface(port='COM3')
    assert hw.connected is False
    assert hw.connect() is True
    assert hw.connected is True

def test_hardware_transmission():
    hw = HardwareInterface()
    with pytest.raises(ConnectionError):
        hw.transmit_waveform([0.0, 1.0, 0.0])
    
    hw.connect()
    samples = [0.1, 0.2, 0.3]
    assert hw.transmit_waveform(samples) == 3
