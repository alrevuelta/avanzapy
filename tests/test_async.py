import unittest
from avanzapy.avanzapy import Avanza
from avanzapy.constants import InstrumentType
import time
import asyncio


id_list = ['5240','5447', '98412', '5364', '625616']
type_list = [InstrumentType.STOCK,
                 InstrumentType.STOCK,
                 InstrumentType.STOCK,
                 InstrumentType.STOCK,
                 InstrumentType.STOCK]


id_list2 = [
"732421",
"732399",
"732428",
"732446",
"732286",
"732310",
"732288",
"732335",
"732333",
"732359",
"732311",
"732442",
"732336",
"732423",
"732320",
"732424",
"732317",
"732393",
"732416",
"732339",
"756438",
"732443",
"732330",
"732400",
"732325",
"732283",
"717413",
"732382",
"732350",
"732358",
"732349",
"227369",
"379860",
"924555",
"108628",
"926378",
"680476",
"220088",
"303275",
"141208",
"767745",
"924661",
"982015",
"317056",
"739894",
"464896",
"700614",
"806934",
"507519",
"304859",
"122366",
"924677",
"719073",
"927435",
"269065",
"813316",
"806983",
"719919",
"270610",
"921678",
"808421",
"247170",
"263929",
"961634",
"329758",
"806757",
"116868",
"702374",
"973535",
"254568",
"807525",
"233768",
"935735",
"451422",
"924391",
"924388",
"788297",
"471756",
"499461"]

type_list2 = [InstrumentType.STOCK] * len(id_list2)

class AsyncOperationsTest(unittest.TestCase):
    avanza = Avanza()

    def test_get_async_instrument(self):
        tic = time.time()
        instruments = self.avanza.get_multiple_async_instruments(type_list2, id_list2)
        for i in instruments:
            print(i.name)
        print("async test took", time.time()-tic)

    def test_get_nonasync_instrument(self):
        #Since there is not a function to query multiple instruments, just call the method as many times
        #as needed
        tic = time.time()
        instruments = [self.avanza.getInstrument(type, id) for id, type in zip(id_list, type_list)]
        for i in instruments:
            print(i.name)
        print("non async test took", time.time() - tic)
