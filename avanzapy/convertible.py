from avanzapy.instrument import Instrument
from avanzapy.constants import InstrumentType


class Convertible(Instrument):
    def __init__(self, raw_data, historical_data=[]):
        super().__init__(InstrumentType.CONVERTIBLE, raw_data, historical_data)
