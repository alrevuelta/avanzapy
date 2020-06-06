from avanzapy.instrument import Instrument
from avanzapy.constants import InstrumentType


class FutureForward(Instrument):
    def __init__(self, raw_data, historical_data=[]):
        super().__init__(InstrumentType.FUTURE_FORWARD, raw_data, historical_data)

    #futures don't have 1 year change?
    @property
    def change_percent_1y(self):
        return ""
