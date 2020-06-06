from avanzapy.instrument import Instrument
from avanzapy.constants import InstrumentType


class Fund(Instrument):
    def __init__(self, raw_data, historical_data=[]):
        super().__init__(InstrumentType.FUND, raw_data, historical_data)

    @property
    def price(self):
        # not sure if this is the price
        return self.get('NAV')

    @property
    def country(self):
        # TODO. This is the name in Swedish i.e. Sverige
        # In the rest of instruments im using the code, i.e. SE, US,...
        return self.get('domicile')

    @property
    def currency(self):
        return self.get('tradingCurrency')

    @property
    def last_updated(self):
        return self.get('NAVLastUpdated')

    @property
    def change_percent_1d(self):
        return self.get('changeSinceOneDay')

    @property
    def change_percent_1w(self):
        return self.get('changeSinceOneWeek')

    @property
    def change_percent_1m(self):
        return self.get('changeSinceOneMonth')

    @property
    def change_percent_1y(self):
        return self.get('changeSinceOneYear')

