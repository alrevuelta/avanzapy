from avanzapy.instrument import Instrument
from avanzapy.constants import InstrumentType


class Bond(Instrument):
    def __init__(self, raw_data, historical_data=[]):
        super().__init__(InstrumentType.BOND, raw_data, historical_data)
