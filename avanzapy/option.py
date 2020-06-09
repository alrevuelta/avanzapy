from avanzapy.instrument import Instrument
from avanzapy.constants import InstrumentType


class Option(Instrument):
    def __init__(self, raw_data, historical_data=[]):
        super().__init__(InstrumentType.OPTION, raw_data, historical_data)

    @property
    def price(self):
        return self.raw_data['underlyingOrderbook']['lastPrice']

    #TODO Not sure about this
    def change_percent_1w(self):
        return ""

    @property
    def change_percent_1m(self):
        return ""

    @property
    def change_percent_1y(self):
        return ""

