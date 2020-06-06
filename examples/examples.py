from avanzapy.avanzapy import Avanza
from avanzapy.constants import InstrumentType, TimePeriod

# Without parameters only allows to use methods
# than don't require log in
avanza = Avanza()

results = avanza.search("Eric", limit=5)
for res in results:
    print(res.type.name, res.name, res.price, res.country, res.id)


inst = avanza.getInstrument(InstrumentType.STOCK, '5240')
print(inst.price)
print(inst.change_percent_1d)


with_historical = avanza.get_instrument_with_historical(
    InstrumentType.STOCK,
    '5240',
    time_period=TimePeriod.this_year)

print(with_historical.historical_data.historical_data)

#with_historical.plot_data()
