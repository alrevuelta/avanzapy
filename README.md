![Python application](https://github.com/alrevuelta/avanzapy/workflows/Python%20application/badge.svg)
![Upload Python Package](https://github.com/alrevuelta/avanzapy/workflows/Upload%20Python%20Package/badge.svg)

# avanzapy
This is a Python wrapper for the unofficial Avanza API. Note that this project is just a prototype, so use at your own risk. Note also that I'm not affiliated with Avanza Bank AB in any way.

This repo is under development, so some features are not yet supported. Featured are splited into two, the ones that require to be logged in and the one that does not.

No log in required. You can use them without providing your Avanza credentials:
* [x] Query data for a given instruments such as stocks, funds, bonds (see supported instruments)
* [x] Query historical data for a given instrument
* [x] Plot historical data
* [x] Search the instruments that matches a given name
* [x] Get inspiration from Avanza

Log in required. Need log in credentials or some sort of cookie:
* [ ] Get account balances
* [ ] Place order
* [ ] Edit order
* [ ] ...more to come

# Supported instruments

* [x] Avanza.STOCK
* [x] Avanza.FUND
* [x] Avanza.BOND
* [x] Avanza.OPTION
* [x] Avanza.FUTURE_FORWARD
* [x] Avanza.CERTIFICATE
* [x] Avanza.WARRANT
* [x] Avanza.EXCHANGE_TRADED_FUND
* [x] Avanza.INDEX
* [ ] Avanza.PREMIUM_BOND
* [ ] Avanza.SUBSCRIPTION_OPTION
* [ ] Avanza.EQUITY_LINKED_BOND
* [ ] Avanza.CONVERTIBLE


# Design rationale
One of the advantages of this API is that it provides an abstraction layer for all instruments, so that they share a common interface. The following attributes are common for all instruments, no matter if its a stock, fund, etc:
     
* name
* id
* type
* isin
* has_fees
* link
* country
* price
* currency
* last_updated
* market
* ticker
* change_percent_1d
* change_percent_1w
* change_percent_1m
* change_percent_1y
* TODO: last updated

Note that the classes that model the instruments, don't have all the attributes. Only the relevant ones are coded. If you want to access a particular attribute not implemented as a property, you can access the raw data that is returned from the API, which is stores as a simple dictionary. Example: stock.raw_data['fieldName']

# Examples
See *examples* for more. The following examples doesn't require to be logged in.

First of all create an `Avanza` object

```python
avanza = Avanza()
```

Now you can query the instruments that match a given name:
```python
results = avanza.search("Eric", limit=5)
for res in results:
    print(res.type.name, res.name, res.price, res.country, res.id)

#Output:
#STOCK Ericsson 9.62 US 3765
#STOCK Ericsson B 88.4 SE 5240
#STOCK Ericsson A 97.3 SE 5239
#STOCK Ericsson B 8.546 FI 61540
#FUTURE_FORWARD ERICB0S  SE 1080243

```

If you already know the `id` of the instrument, you can send a query right away.

```python
inst = avanza.getInstrument(InstrumentType.STOCK, '5240')
print(inst.price)
print(inst.change_percent_1d)
#Output: (or whatever values
#88.4
#-0.72
```

You can also query some historical data, and even plot it

```python
with_historical = avanza.get_instrument_with_historical(
    InstrumentType.STOCK,
    '5240',
    time_period=TimePeriod.this_year)

print(with_historical.historical_data.historical_data)
```

And generate a plot

```python
#with_historical.plot_data()
```

You can also query a bunch of instruments in an asynchronous way. This method is so fast, but note that you might get in trouble, i.e. banned IP. To the best of my knowledge, no one has reported this yet.

```python
instruments = avanza.get_multiple_async_instruments(
                     ["788297", "471756"],
                     [InstrumentType.STOCK, InstrumentType.STOCK])
for i in instruments:
    print(i.name)
        
``` 


# Testing
Incomplete, unorganized, inconsistent. YOLO

# License

# Disclaimer
This is just a prototype and is not meant to be used by anyone. Its also important to note that I'm not affiliated with Avanza Bank AB in any way.

The author of this software is not responsible for any indirect damages (foreseeable or unforeseeable), such as, if necessary, loss or alteration of or fraudulent access to data, accidental transmission of viruses or of any other harmful element, loss of profits or opportunities, the cost of replacement goods and services or the attitude and behavior of a third party.
