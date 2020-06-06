from avanzapy.instrument import Instrument
from avanzapy.constants import InstrumentType


class PremiumBond(Instrument):
    def __init__(self, raw_data, historical_data=[]):
        super().__init__(InstrumentType.PREMIUM_BOND, raw_data, historical_data)
