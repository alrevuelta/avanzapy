from avanzapy.instrument import Instrument
from avanzapy.constants import InstrumentType


class Etf(Instrument):
    def __init__(self, raw_data, historical_data=[]): # TODO dont do this [] crap
        super().__init__(InstrumentType.EXCHANGE_TRADED_FUND, raw_data, historical_data)
