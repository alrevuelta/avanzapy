from avanzapy.instrument import Instrument
from avanzapy.constants import InstrumentType


class Index(Instrument):
    def __init__(self, raw_data, historical_data=[]):
        super().__init__(InstrumentType.INDEX, raw_data, historical_data)
