from avanzapy.instrument import Instrument
from avanzapy.constants import InstrumentType


class SubscriptionOption(Instrument):
    def __init__(self, raw_data, historical_data=[]):
        super().__init__(InstrumentType.SUBSCRIPTION_OPTION, raw_data, historical_data)
