from avanzapy.instrument import Instrument
from avanzapy.constants import InstrumentType


class Warrant(Instrument):
    def __init__(self, raw_data, historical_data=[]):
        super().__init__(InstrumentType.WARRANT, raw_data, historical_data)
