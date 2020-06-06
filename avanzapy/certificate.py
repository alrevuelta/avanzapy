from avanzapy.instrument import Instrument
from avanzapy.constants import InstrumentType


class Certificate(Instrument):
    # a certificate has an underlying asset? i.e. stock?
    def __init__(self, raw_data, historical_data=[]):
        super().__init__(InstrumentType.CERTIFICATE, raw_data, historical_data)

