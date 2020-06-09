from avanzapy.constants import InstrumentType
import matplotlib.pyplot as plt
import uuid
from avanzapy.historicaldata import HistoricalData

class Instrument:
    # Generic class of an instrument (see Instrument Type)
    # if you just want to access avanza json dict, just uso ['xx'] with the class.

    def __init__(self,
                 instrument_type,
                 raw_data=None,
                 historical_data: 'HistoricalData'=[]):  # TODO dont do this [] crap
        self.instrument_type = instrument_type
        self.__raw_data = raw_data
        self.__historical_data = historical_data

    def __str__(self):
        return f"{self.name} is a {self.type} registered in {self.country} " \
               f"with a price of {self.price} {self.currency}, " \
               f"a 1 day change of {self.change_percent_1d}% and a 1 week " \
               f"change of {self.change_percent_1w}%"

    #to access the data as if it were a normal dict.
    # better to use get.
    def __getitem__(self, i):
        # check that is not empty
        return self.__raw_data[i]

    def get(self, key):
        return self.__raw_data.get(key, '')

    @property
    def raw_data(self):
        return self.__raw_data

    @property
    def historical_data(self):
        return self.__historical_data

    # TODO
    #An instrument can have multiple historical
    # charts (i.e. different temporal stamp)
    def add_historical_data(self, historical_data):
        pass
        # add to historical data list


    #prototyping this.
    #TODO accept as input which plot to select?
    #Move to HistoricalData class?
    def plot_data(self):
        # currently just supportnig normal plots, no OHLC

        lazy_dict = {'today': '1 Day',
        'week': '1 Week',
        'month': '1 Month',
        'three_months': 'Three Months',
        'this_year': 'This Year',
        'year': '1 Year',
        'three_years': '3 Years',
        'five_years': '5 Years'}

        # | {self.price} {self.currency} | One day {self.change_percent_1d}% | One year {self.change_percent_1y}%
        title = f'{self.name} ({self.ticker})'
        data = self.__historical_data.historical_data
        ax = data.plot(kind='line',
                       x='time',
                       y='value',
                       title=f'{self.name} {lazy_dict[self.__historical_data.time_period.name]}',
                       grid=True,
                       label=self.name,
                       color='green')
        ax.set_xlabel("")
        ax.set_ylabel("")
        limits = ax.dataLim
        ax.grid(color='black', linestyle='-', linewidth=0.2)
        plt.fill_between(data['time'], data['value'],
                         y2=limits.y0, # fill until lowest value
                         facecolor='green', alpha=0.3, interpolate=True)
        ax.tick_params(axis='x', labelsize=10)
        ax.tick_params(axis='y', labelsize=12)

        plt.margins(0.005)
        plt.tight_layout()

        # TODO have a root path somerhwre
        f_name = str(uuid.uuid1()) + '.png'
        plt.savefig(f_name)
        # error checking?
        return f_name

    """
    TODO This is part of avanzapy. Doest it make more
    sense to have it here? Maybe not
    """
    def get_historical_data(self):
        pass

    """
    - Common Properties -
    All instruments have the following properties stores using exactly the same key, so
    the inherited classes shall not override these methods.
    """

    @property
    def name(self):
        return self.__raw_data.get('name')

    @property
    def id(self):
        return self.__raw_data.get('id')

    @property
    def type(self):
        return self.instrument_type

    @property
    def isin(self):
        return self.__raw_data.get('isin')

    @property
    def has_fees(self):
        return self.__raw_data.get('hasInvestmentFees')

    @property
    def link(self):
        return f'https://www.avanza.se/aktier/om-aktien.html/{self.id}'

    """
    - General Properties -
    Almost all instruments have the following properties, but some of them might slightly
    different hence they will need to override it.
    """

    @property
    def country(self):
        return self.get('flagCode')

    @property
    def price(self):
        return self.get('lastPrice')

    @property
    def currency(self):
        return self.get('currency')

    @property
    def last_updated(self):
        return self.get('lastPriceUpdated')

    @property
    def market(self):
        return self.get('marketPlace')

    @property
    def ticker(self):
        return self.get('tickerSymbol')

    @property
    def change_percent_1d(self):
        return self.get('changePercent')

    "Looks like this field is not always present. Quick fix"
    @property
    def change_percent_1w(self):
        try:
            return round(((self.price / self.get('priceOneWeekAgo')) - 1) * 100, 2)
        except:
            return ""

    @property
    def change_percent_1m(self):
        try:
            return round(((self.price / self.get('priceOneMonthAgo')) - 1) * 100, 2)
        except:
            return ""

    @property
    def change_percent_1y(self):
        try:
            return round(((self.price / self.get('priceOneYearAgo')) - 1) * 100, 2)
        except:
            return ""