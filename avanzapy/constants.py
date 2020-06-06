from enum import Enum


class InstrumentType(Enum):
    STOCK = 1
    FUND = 2
    BOND = 3
    OPTION = 4
    FUTURE_FORWARD = 5
    CERTIFICATE = 6
    WARRANT = 7
    EXCHANGE_TRADED_FUND = 8
    INDEX = 9
    PREMIUM_BOND = 10
    SUBSCRIPTION_OPTION = 11
    EQUITY_LINKED_BOND = 12
    CONVERTIBLE = 13
    NOT_SELECTED = 14


class TransactionType(Enum):
    OPTIONS = 1
    FOREX = 2
    DEPOSIT_WITHDRAW = 3
    BUY_SELL = 4
    DIVIDEND = 5
    INTEREST = 6
    FOREIGN_TAX = 7


class OrderType(Enum):
    BUY = 1
    SELL = 2


class ChartType(Enum):
    AREA = 1
    CANDLESTICK = 2
    OHLC = 3


class ChartResoluton(Enum):
    TEN_MINUTES = 1
    THIRTY_MINUTES = 2
    HOUR = 3
    DAY = 4
    MONTH = 5


class TimePeriod(Enum):
    today = 1
    week = 2
    month = 3
    three_months = 4
    this_year = 5
    year = 6
    three_years = 7
    five_years = 8
