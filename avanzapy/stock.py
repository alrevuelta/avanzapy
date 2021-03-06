from avanzapy.instrument import Instrument
from avanzapy.constants import InstrumentType


class Stock(Instrument):
    def __init__(self, raw_data, historical_data=[]):
        super().__init__(InstrumentType.STOCK, raw_data, historical_data)
