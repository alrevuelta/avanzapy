import unittest
from avanzapy.avanzapy import Avanza
from avanzapy.constants import InstrumentType


class GetInstrumentTest(unittest.TestCase):
    avanza = Avanza()

    def test_stock(self):
        # https://www.avanza.se/aktier/om-aktien.html/5240
        stock = self.avanza.getInstrument(InstrumentType.STOCK, '5240')

        print("\nParameters")
        print("name              ", stock.name)
        print("id                ", stock.id)
        print("type              ", stock.type)
        print("isin              ", stock.isin)
        print("has_fees          ", stock.has_fees)
        print("link              ", stock.link)
        print("country           ", stock.country)
        print("price             ", stock.price)
        print("currency          ", stock.currency)
        print("last_updated      ", stock.last_updated)
        print("market            ", stock.market)
        print("ticker            ", stock.ticker)
        print("change_percent_1d ", stock.change_percent_1d)
        print("change_percent_1w ", stock.change_percent_1w)
        print("change_percent_1m ", stock.change_percent_1m)
        print("change_percent_1y ", stock.change_percent_1y)

        self.assertEqual(stock.name, 'Ericsson B')
        self.assertEqual(stock.id, '5240')
        self.assertEqual(stock.type, InstrumentType.STOCK)

    def test_fund(self):
        # https://www.avanza.se/aktier/om-aktien.html/573
        fund = self.avanza.getInstrument(InstrumentType.FUND, '573')

        print("\nParameters")
        print("name              ", fund.name)
        print("id                ", fund.id)
        print("type              ", fund.type)
        print("isin              ", fund.isin)
        print("has_fees          ", fund.has_fees)
        print("link              ", fund.link)
        print("country           ", fund.country)
        print("price             ", fund.price)
        print("currency          ", fund.currency)
        print("last_updated      ", fund.last_updated)
        print("market            ", fund.market)
        print("ticker            ", fund.ticker)
        print("change_percent_1d ", fund.change_percent_1d)
        print("change_percent_1w ", fund.change_percent_1w)
        print("change_percent_1m ", fund.change_percent_1m)
        print("change_percent_1y ", fund.change_percent_1y)

        self.assertEqual(fund.name, 'Länsförsäkringar Europa Aktiv A')
        self.assertEqual(fund.id, '573')
        self.assertEqual(fund.type, InstrumentType.FUND)

    def test_bond(self):
        # https://www.avanza.se/obligationer/om-obligationen.html/572908/estea-kapbevis3
        bond = self.avanza.getInstrument(InstrumentType.BOND, '572908')

        print("\nParameters")
        print("name              ", bond.name)
        print("id                ", bond.id)
        print("type              ", bond.type)
        print("isin              ", bond.isin)
        print("has_fees          ", bond.has_fees)
        print("link              ", bond.link)
        print("country           ", bond.country)
        print("price             ", bond.price)
        print("currency          ", bond.currency)
        print("last_updated      ", bond.last_updated)
        print("market            ", bond.market)
        print("ticker            ", bond.ticker)
        print("change_percent_1d ", bond.change_percent_1d)
        print("change_percent_1w ", bond.change_percent_1w)
        print("change_percent_1m ", bond.change_percent_1m)
        print("change_percent_1y ", bond.change_percent_1y)

        self.assertEqual(bond.name, 'ESTEA KAPBEVIS3')
        self.assertEqual(bond.id, '572908')
        self.assertEqual(bond.type, InstrumentType.BOND)

    def test_option(self):
        # https://www.avanza.se/optioner/om-optionen.html/1101810/omxs300f12y1830

        option = self.avanza.getInstrument(InstrumentType.OPTION, '1101810')

        print("\nParameters")
        print("name              ", option.name)
        print("id                ", option.id)
        print("type              ", option.type)
        print("isin              ", option.isin)
        print("has_fees          ", option.has_fees)
        print("link              ", option.link)
        print("country           ", option.country)
        print("price             ", option.price)
        print("currency          ", option.currency)
        print("last_updated      ", option.last_updated)
        print("market            ", option.market)
        print("ticker            ", option.ticker)
        print("change_percent_1d ", option.change_percent_1d) #this is wrong
        print("change_percent_1w ", option.change_percent_1w)
        print("change_percent_1m ", option.change_percent_1m)
        print("change_percent_1y ", option.change_percent_1y)

        self.assertEqual(option.name, 'OMXS300F12Y1830')
        self.assertEqual(option.id, '1101810')
        self.assertEqual(option.type, InstrumentType.OPTION)

    def test_future_forward(self):
        # https://www.avanza.se/terminer/om-terminen.html/914880/omxs300f
        forward = self.avanza.getInstrument(InstrumentType.FUTURE_FORWARD, '914880')

        print("\nParameters")
        print("name              ", forward.name)
        print("id                ", forward.id)
        print("type              ", forward.type)
        print("isin              ", forward.isin)
        print("has_fees          ", forward.has_fees)
        print("link              ", forward.link)
        print("country           ", forward.country)
        print("price             ", forward.price)
        print("currency          ", forward.currency)
        print("last_updated      ", forward.last_updated)
        print("market            ", forward.market)
        print("ticker            ", forward.ticker)
        print("change_percent_1d ", forward.change_percent_1d)
        print("change_percent_1w ", forward.change_percent_1w)
        print("change_percent_1m ", forward.change_percent_1m)
        print("change_percent_1y ", forward.change_percent_1y)

        self.assertEqual(forward.name, 'OMXS300F')
        self.assertEqual(forward.id, '914880')
        self.assertEqual(forward.type, InstrumentType.FUTURE_FORWARD)

    def test_certificate(self):
        #https://www.avanza.se/aktier/om-aktien.html/804912
        certificate = self.avanza.getInstrument(InstrumentType.CERTIFICATE, '804912')

        print("\nParameters")
        print("name              ", certificate.name)
        print("id                ", certificate.id)
        print("type              ", certificate.type)
        print("isin              ", certificate.isin)
        print("has_fees          ", certificate.has_fees)
        print("link              ", certificate.link)
        print("country           ", certificate.country)
        print("price             ", certificate.price)
        print("currency          ", certificate.currency)
        print("last_updated      ", certificate.last_updated)
        print("market            ", certificate.market)
        print("ticker            ", certificate.ticker)
        print("change_percent_1d ", certificate.change_percent_1d)
        print("change_percent_1w ", certificate.change_percent_1w)
        print("change_percent_1m ", certificate.change_percent_1m)
        print("change_percent_1y ", certificate.change_percent_1y)

        self.assertEqual(certificate.name, 'BEAR AIRBUS X5 AVA 1')
        self.assertEqual(certificate.id, '804912')
        self.assertEqual(certificate.type, InstrumentType.CERTIFICATE)


    def test_warrant(self):
        #https://www.avanza.se/aktier/om-aktien.html/718858
        warrant = self.avanza.getInstrument(InstrumentType.WARRANT, '718858')

        print("\nParameters")
        print("name              ", warrant.name)
        print("id                ", warrant.id)
        print("type              ", warrant.type)
        print("isin              ", warrant.isin)
        print("has_fees          ", warrant.has_fees)
        print("link              ", warrant.link)
        print("country           ", warrant.country)
        print("price             ", warrant.price)
        print("currency          ", warrant.currency)
        print("last_updated      ", warrant.last_updated)
        print("market            ", warrant.market)
        print("ticker            ", warrant.ticker)
        print("change_percent_1d ", warrant.change_percent_1d)
        print("change_percent_1w ", warrant.change_percent_1w)
        print("change_percent_1m ", warrant.change_percent_1m)
        print("change_percent_1y ", warrant.change_percent_1y)

        self.assertEqual(warrant.name, 'MINI L AMAZON AVA 17')
        self.assertEqual(warrant.id, '718858')
        self.assertEqual(warrant.type, InstrumentType.WARRANT)

    def test_etf(self):
        #https://www.avanza.se/aktier/om-aktien.html/924016

        etf = self.avanza.getInstrument(InstrumentType.EXCHANGE_TRADED_FUND, '924016')

        print("\nParameters")
        print("name              ", etf.name)
        print("id                ", etf.id)
        print("type              ", etf.type)
        print("isin              ", etf.isin)
        print("has_fees          ", etf.has_fees)
        print("link              ", etf.link)
        print("country           ", etf.country)
        print("price             ", etf.price)
        print("currency          ", etf.currency)
        print("last_updated      ", etf.last_updated)
        print("market            ", etf.market)
        print("ticker            ", etf.ticker)
        print("change_percent_1d ", etf.change_percent_1d)
        print("change_percent_1w ", etf.change_percent_1w)
        print("change_percent_1m ", etf.change_percent_1m)
        print("change_percent_1y ", etf.change_percent_1y)

        self.assertEqual(etf.name, 'LYX ETF Green Bond (DR) ACC')
        self.assertEqual(etf.id, '924016')
        self.assertEqual(etf.type, InstrumentType.EXCHANGE_TRADED_FUND)

    def test_index(self):
        #https://www.avanza.se/aktier/om-aktien.html/961717
        index = self.avanza.getInstrument(InstrumentType.INDEX, '961717')

        print("\nParameters")
        print("name              ", index.name)
        print("id                ", index.id)
        print("type              ", index.type)
        print("isin              ", index.isin)
        print("has_fees          ", index.has_fees)
        print("link              ", index.link)
        print("country           ", index.country)
        print("price             ", index.price)
        print("currency          ", index.currency)
        print("last_updated      ", index.last_updated)
        print("market            ", index.market)
        print("ticker            ", index.ticker)
        print("change_percent_1d ", index.change_percent_1d)
        print("change_percent_1w ", index.change_percent_1w)
        print("change_percent_1m ", index.change_percent_1m)
        print("change_percent_1y ", index.change_percent_1y)

        self.assertEqual(index.name, 'OMX Stockholm 30 ESG Responsible Index')
        self.assertEqual(index.id, '961717')
        self.assertEqual(index.type, InstrumentType.INDEX)


if __name__ == '__main__':
    unittest.main()
