from avanzapy.instrument_factory import instrument_factory
import requests
from avanzapy.constants import InstrumentType,\
                               ChartType,\
                               ChartResoluton, \
                               TimePeriod
from avanzapy.instrument import Instrument
import json
from datetime import datetime as dt
import pandas
from avanzapy.historicaldata import HistoricalData
import aiohttp
import asyncio
from aiohttp import ClientSession
import json

class Avanza:
    URL_SEARCH = 'https://www.avanza.se/_mobile/market/search/{instrument}?query={query}&limit={limit}'
    URL_INSTRUMENTS = 'https://avanza.se/_mobile/market/{instrumentType}/{id}'
    URL_INSPIRATION = 'https://avanza.se/_mobile/marketing/inspirationlist'
    URL_HISTORICAL = 'https://www.avanza.se/ab/component/highstockchart/getchart/orderbook'

    def __init__(self):
        # login optional

        self.__session = requests.Session()

        # All the async stuff is very very experimental
        self.__async_session = aiohttp.ClientSession()

    # Methods borrowed from JS implementation fhqvst/avanza
    def authenticate(self):
        pass

    def disconnect(self):
        pass

    def getPositions(self):
        pass

    def getOverview(self):
        pass

    def getAccountOverview(self):
        pass

    def getDealsAndOrders(self):
        pass

    def getTransactions(self):
        pass

    def getWatchlists(self):
        pass

    def addToWatchlist(self):
        pass

    def removeFromWatchlist(self):
        pass

    def getInstrument(self,
                      instrument_type: 'InstrumentType',
                      instrument_id: 'str')-> 'Instrument':
        url = self.URL_INSTRUMENTS.replace('{instrumentType}', instrument_type.name.lower())\
                                  .replace('{id}', instrument_id)
        response = self.__request_get_no_login(url)

        return instrument_factory(instrument_type, response)

    def getOrderbook(self):
        pass

    def getOrderbooks(self):
        pass

    def getChartdata(self):
        pass

    def getInspirationLists(self):
        pass

    def getInspirationList(self):
        pass

    def subscribe(self):
        pass

    def placeOrder(self):
        pass

    def getOrder(self):
        pass

    def editOrder(self):
        pass

    def deleteOrder(self):
        pass

    def search(self,
               query: 'str',
               instrument: 'InstrumentType'=InstrumentType.NOT_SELECTED,
               limit: 'int'=5,
               local: 'bool'=False)-> '[]':   #TODO local maybe doesnt make sense. Remove?
        # local means to search in a local database without connecting to avanza
        if not local:
            # TODO This could be nicer
            url = Avanza.URL_SEARCH.replace('{query}', query)\
                                   .replace('{limit}', str(limit))
            if instrument == InstrumentType.NOT_SELECTED:
                url = url.replace('/{instrument}', '')
            else:
                url = url.replace('{instrument}', instrument.name)
            response = self.__request_get_no_login(url)
            hits = []
            if response.get('totalNumberOfHits', 0) == 0:
                return []
            else:
                for instrument_hit in response['hits']:
                    for hit in instrument_hit.get('topHits', ''):
                        print(InstrumentType[instrument_hit['instrumentType']])
                        hits.append(instrument_factory(InstrumentType[instrument_hit['instrumentType']], hit))
        else:
            print("TODO")

        return hits

    def call(self):
        pass


    #Mest ägda aktierna
    #Dagens vinnare Stockholmsbörsen
    #Dagens förlorare Stockholmsbörsen
    #Aktierna med högst direktavkastning
    #Mest ägda utländska aktierna
    #Bäst i år på Stockholmsbörsen
    #Flest nya ägare senaste mån
    #Aktierna med lägst P/E-tal
    #Populärast i USA
    #Flest nya ägare USA
    #Mest ägda fonderna
    #Fonderna med högst rating
    #Fonderna med bäst avkastning (3 mån)
    #Indexfonderna med lägst avgift
    def get_inspiration_list(self):
        response = self.__request_get_no_login(self.URL_INSPIRATION)
        """print(response)
        for i in response:
            print(i['name'], i['id'])
            for j in i['orderbooks']:
                print(j)
        print(response)
        """
        # TODO Process the response a bit
        return response

    """
    Find best match for a given name
    TODO: accept also limit, default=1
    """
    def get_by_name(self, instrument_name):
        instrument = None
        matches = self.search(instrument_name, limit=1)
        if matches:
            instrument = self.getInstrument(instrument_type=matches[0].type,
                                            instrument_id=matches[0].id)
        return instrument

    """
    Resolves the mapping between an instrument name (stock, fund,...) and its avanza
    id. This is done locally without relying in the external API. See /database
    """
    def resolve_id_locally(self, instrument_name):
        # Use data in /database. Not complete though.
        pass

    """
    Get historical data for a given instrument
    """
    def get_historical(self,
                       instrument_id,
                       chart_type=ChartType.AREA,
                       chart_resolution=ChartResoluton.TEN_MINUTES,
                       time_period=TimePeriod.this_year): # caps are important
        p = {
            "orderbookId": instrument_id,
            "chartType": chart_type.name,
            "chartResolution": chart_resolution.name,
            "timePeriod": time_period.name
        }

        r = self.__request_post_no_login(self.URL_HISTORICAL, params=p)
        print(r)

        """
        TODO:
        dataPoints is not always used.
        i.e. CERTIFICATE uses 'marketMakerBidPoints'
        """
        data_series = r['dataPoints']
        for x in data_series:
            x[0] = dt.fromtimestamp(x[0] / 1000)
        if chart_type == ChartType.AREA:
            df = pandas.DataFrame(data_series, columns=['time', 'value'])
        else:
            df = pandas.DataFrame(data_series, columns=['time', 'opens', 'highs', 'lows', 'closes'])

        # remove NaN
        df = df.dropna()
        print(df)
        return df

    """TODO this method should be part of the get_instrument.
    Just have an option like: download_historical = True"""
    def get_instrument_with_historical(self,
                                       instrument_type: 'InstrumentType',
                                       instrument_id: 'str',
                                       chart_type=ChartType.AREA,
                                       chart_resolution=ChartResoluton.TEN_MINUTES,
                                       time_period=TimePeriod.this_year
                                       )-> 'Instrument':
        url = self.URL_INSTRUMENTS.replace('{instrumentType}', instrument_type.name.lower())\
                                  .replace('{id}', instrument_id)
        response = self.__request_get_no_login(url)

        hist_data = self.get_historical(instrument_id,
                                        chart_type=chart_type,
                                        chart_resolution=chart_resolution,
                                        time_period=time_period)

        historical = HistoricalData(hist_data, chart_type, chart_resolution, time_period)

        return instrument_factory(instrument_type, response, historical)


    """
    Experimental.
    Not ment to be used outside
    """
    async def __get_single_async_instrument(self, session, instrument_type, instrument_id):
        url = self.URL_INSTRUMENTS.replace('{instrumentType}', instrument_type.name.lower())\
                                  .replace('{id}', instrument_id)
        print(url)
        resp = await session.request(method="GET", url=url)
        resp.raise_for_status()
        html = await resp.text()

        #todo is there a way to directly get the dict without having to convert it?
        x = instrument_factory(instrument_type, json.loads(html))
        return x

    """
       Experimental.
       Not ment to be used outside
       """
    async def __get_multiple_async_instruments(self, type_list, id_list):
        async_inst = []
        return_this = []
        # TODO verify_ssl is Off because I had some problems with mac. Quick fix while prototyping
        async with ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            for type, id, in zip(type_list, id_list):
                async_inst.append(self.__get_single_async_instrument(session, type, id))
            instruments = await asyncio.gather(*async_inst)
        return instruments

    """
    
    """
    def get_multiple_async_instruments(self,
                                       type_list: '[str]',
                                       id_list: '[InstrumentType]')->'[Instrument]':
        loop = asyncio.get_event_loop()
        instruments = loop.run_until_complete(self.__get_multiple_async_instruments(type_list, id_list))
        return instruments

    """
    """
    def __request_post_no_login(self, url, params):
        print(json.dumps(params))
        h = {"Content-Type": "application/json"}
        r = self.__session.post(url, data=json.dumps(params), headers=h).json()

        # TODO some error checking

        return r

    """
    request data that doesn't need require log in. no headers/cookies
    we are looking for the fastest response here.
    """
    def __request_get_no_login(self, url):
        print(url)
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        else:
            raise Exception("Error in request, status code not 200")
            # do something
        # check also for other errors in the json