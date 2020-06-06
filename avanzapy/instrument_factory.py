from avanzapy.constants import InstrumentType

from avanzapy.stock import Stock
from avanzapy.fund import Fund
from avanzapy.bond import Bond
from avanzapy.option import Option
from avanzapy.futureforward import FutureForward
from avanzapy.certificate import Certificate
from avanzapy.warrant import Warrant
from avanzapy.etf import Etf
from avanzapy.index import Index
from avanzapy.premiumbond import PremiumBond
from avanzapy.subscriptionoption import SubscriptionOption
from avanzapy.equitylinkedbond import EquityLinkedBond
from avanzapy.convertible import Convertible


"""
Instrument factory, creates a particular instrument
with some given data.
TODO: Ugly
"""
def instrument_factory(instrument_type, raw_data, historical_data=[]):
    if instrument_type == InstrumentType.STOCK:
        return Stock(raw_data, historical_data)
    elif instrument_type == InstrumentType.FUND:
        return Fund(raw_data, historical_data)
    elif instrument_type == InstrumentType.BOND:
        return Bond(raw_data, historical_data)
    elif instrument_type == InstrumentType.OPTION:
        return Option(raw_data, historical_data)
    elif instrument_type == InstrumentType.FUTURE_FORWARD:
        return FutureForward(raw_data, historical_data)
    elif instrument_type == InstrumentType.CERTIFICATE:
        return Certificate(raw_data, historical_data)
    elif instrument_type == InstrumentType.WARRANT:
        return Warrant(raw_data, historical_data)
    elif instrument_type == InstrumentType.EXCHANGE_TRADED_FUND:
        return Etf(raw_data, historical_data)
    elif instrument_type == InstrumentType.INDEX:
        return Index(raw_data, historical_data)
    elif instrument_type == InstrumentType.PREMIUM_BOND:
        return PremiumBond(raw_data, historical_data)
    elif instrument_type == InstrumentType.SUBSCRIPTION_OPTION:
        return SubscriptionOption(raw_data, historical_data)
    elif instrument_type == InstrumentType.EQUITY_LINKED_BOND:
        return EquityLinkedBond(raw_data, historical_data)
    elif instrument_type == InstrumentType.CONVERTIBLE:
        return Convertible(raw_data, historical_data)
    else:
        print("cry")