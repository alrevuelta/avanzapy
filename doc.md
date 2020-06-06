Can't find documentation for the avanza "_mobile" API so lots of stuff are reverse engineered.
See https://github.com/fhqvst/avanza

# Random Doc

# Instrument types

* Avanza.STOCK [x]
* Avanza.FUND [x]
* Avanza.BOND [x]
* Avanza.OPTION [x]
* Avanza.FUTURE_FORWARD	[x]
* Avanza.CERTIFICATE [x]
* Avanza.WARRANT [x]
* Avanza.EXCHANGE_TRADED_FUND [x]
* Avanza.INDEX [x]
* Avanza.PREMIUM_BOND TODO:
* Avanza.SUBSCRIPTION_OPTION	TODO:
* Avanza.EQUITY_LINKED_BOND TODO:
* Avanza.CONVERTIBLE TODO:

# Query STOCK
https://avanza.se/_mobile/market/stock/5240
{
   "priceOneWeekAgo":83.88,
   "priceOneMonthAgo":83.10,
   "priceSixMonthsAgo":86.96,
   "priceAtStartOfYear":81.56,
   "priceOneYearAgo":95.28,
   "priceThreeYearsAgo":61.25,
   "priceFiveYearsAgo":94.00,
   "priceThreeMonthsAgo":80.00,
   "marketPlace":"Stockholmsbörsen",
   "marketList":"Large Cap Stockholm",
   "hasInvestmentFees":false,
   "morningStarFactSheetUrl":"http://lt.morningstar.com/gj8uge2g9k/custom/simplepage1/default.aspx?isin=SE0000108656&exchange=XSTO&curr=BAS",
   "currency":"SEK",
   "shortSellable":true,
   "lowestPrice":83.38,
   "highestPrice":85.68,
   "totalVolumeTraded":10288610,
   "tradable":true,
   "isin":"SE0000108656",
   "lastPrice":84.12,
   "lastPriceUpdated":"2020-05-27T17:29:30.000+0200",
   "change":-1.32,
   "changePercent":-1.54,
   "totalValueTraded":867974109.87,
   "tickerSymbol":"ERIC B",
   "loanFactor":70.00,
   "flagCode":"SE",
   "quoteUpdated":"2020-05-27T17:29:30.555+0200",
   "name":"Ericsson B",
   "id":"5240",
   "country":"Sverige",
   "keyRatios":{
      "volatility":41.95,
      "priceEarningsRatio":165.91,
      "directYield":1.76
   },
   "numberOfOwners":47635,
   "superLoan":true,
   "pushPermitted":true,
   "dividends":[
      {
         "amountPerShare":0.75,
         "paymentDate":"2020-10-07",
         "currency":"SEK",
         "exDate":"2020-10-01"
      },
      {
         "amountPerShare":0.75,
         "paymentDate":"2020-04-07",
         "currency":"SEK",
         "exDate":"2020-04-01"
      }
   ],
   "relatedStocks":[
      {
         "priceOneYearAgo":4.5505,
         "lastPrice":3.5370,
         "flagCode":"FI",
         "name":"Nokia Oyj",
         "id":"52784"
      },
      {
         "priceOneYearAgo":151.85,
         "lastPrice":169.35,
         "flagCode":"SE",
         "name":"SKF B",
         "id":"5259"
      },
      {
         "priceOneYearAgo":27.40,
         "lastPrice":18.85,
         "flagCode":"SE",
         "name":"Alcadon Group",
         "id":"690158"
      },
      {
         "lastPrice":34.67,
         "flagCode":"SE",
         "name":"Electrolux Professional B",
         "id":"1072320"
      },
      {
         "priceOneYearAgo":106.75,
         "lastPrice":104.20,
         "flagCode":"SE",
         "name":"Elekta B",
         "id":"5280"
      }
   ],
   "company":{
      "sector":"Teknik",
      "stocks":[
         {
            "totalNumberOfShares":3072395752,
            "name":"Ericsson"
         },
         {
            "totalNumberOfShares":261755983,
            "name":"Ericsson A"
         },
         {
            "totalNumberOfShares":3072395752,
            "name":"Ericsson B"
         }
      ],
      "description":"Ericsson är verksamma inom kommunikationsteknik. Idag är bolaget en utvecklare av mjukvara och IT-infrastrukturlösningar för mobil, bredband och molntjänster, samt tillhörande tekniska tjänster. Kunderna återfinns huvudsakligen inom E-handeln, informationsteknologi samt inom kommunikationsbranschen. Ericsson grundades ursprungligen 1876 och har sitt huvudkontor i Stockholm.",
      "marketCapital":286691745880,
      "marketCapitalCurrency":"SEK",
      "totalNumberOfShares":6406547487,
      "chairman":"Ronnie Leten",
      "name":"Ericsson",
      "id":"125",
      "CEO":"Börje Ekholm"
   },
   "orderDepthLevels":[

   ],
   "marketMakerExpected":false,
   "orderDepthReceivedTime":"2020-05-27T17:29:30.555+0200",
   "latestTrades":[
      {
         "matchedOnMarket":true,
         "cancelled":false,
         "volume":1799634,
         "price":84.12,
         "dealTime":"2020-05-27T17:29:30.000+0200"
      },
      {
         "matchedOnMarket":true,
         "cancelled":false,
         "volume":2120,
         "price":83.96,
         "dealTime":"2020-05-27T17:24:47.000+0200"
      },
      {
         "matchedOnMarket":true,
         "cancelled":false,
         "volume":19,
         "price":84.00,
         "dealTime":"2020-05-27T17:24:41.000+0200"
      },
      {
         "matchedOnMarket":true,
         "cancelled":false,
         "volume":1121,
         "price":84.00,
         "dealTime":"2020-05-27T17:24:41.000+0200"
      },
      {
         "matchedOnMarket":true,
         "cancelled":false,
         "volume":276,
         "price":84.00,
         "dealTime":"2020-05-27T17:24:41.000+0200"
      },
      {
         "matchedOnMarket":true,
         "cancelled":false,
         "volume":262,
         "price":84.00,
         "dealTime":"2020-05-27T17:24:41.000+0200"
      },
      {
         "matchedOnMarket":true,
         "cancelled":false,
         "volume":691,
         "price":84.00,
         "dealTime":"2020-05-27T17:24:41.000+0200"
      },
      {
         "matchedOnMarket":true,
         "cancelled":false,
         "volume":16,
         "price":83.98,
         "dealTime":"2020-05-27T17:24:38.000+0200"
      },
      {
         "matchedOnMarket":true,
         "cancelled":false,
         "volume":2078,
         "price":84.00,
         "dealTime":"2020-05-27T17:24:26.000+0200"
      },
      {
         "matchedOnMarket":true,
         "cancelled":false,
         "volume":114,
         "price":84.00,
         "dealTime":"2020-05-27T17:24:26.000+0200"
      },
      {
         "matchedOnMarket":true,
         "cancelled":false,
         "volume":1072,
         "price":84.00,
         "dealTime":"2020-05-27T17:24:26.000+0200"
      },
      {
         "matchedOnMarket":true,
         "cancelled":false,
         "volume":1245,
         "price":84.00,
         "dealTime":"2020-05-27T17:24:26.000+0200"
      },
      {
         "matchedOnMarket":true,
         "cancelled":false,
         "volume":1049,
         "price":84.00,
         "dealTime":"2020-05-27T17:24:26.000+0200"
      },
      {
         "matchedOnMarket":true,
         "cancelled":false,
         "volume":938,
         "price":84.00,
         "dealTime":"2020-05-27T17:24:26.000+0200"
      },
      {
         "matchedOnMarket":true,
         "cancelled":false,
         "volume":414,
         "price":84.00,
         "dealTime":"2020-05-27T17:24:26.000+0200"
      }
   ],
   "marketTrades":true,
   "annualMeetings":[
      {
         "extra":false,
         "eventDate":"2020-03-31"
      }
   ],
   "companyReports":[
      {
         "reportType":"ANNUAL",
         "eventDate":"2020-01-24"
      },
      {
         "reportType":"INTERIM",
         "eventDate":"2020-04-22"
      },
      {
         "reportType":"INTERIM",
         "eventDate":"2020-07-17"
      },
      {
         "reportType":"INTERIM",
         "eventDate":"2020-10-21"
      }
   ],
   "brokerTradeSummary":{
      "orderbookId":"5240",
      "items":[
         {
            "buyVolume":802865,
            "sellVolume":641686,
            "brokerCode":"AVA",
            "netBuyVolume":161179
         },
         {
            "buyVolume":9334659,
            "sellVolume":9495838,
            "brokerCode":"ANON",
            "netBuyVolume":-161179
         }
      ]
   },
   "companyOwners":{
      "list":[
         {
            "name":"Cevian Capital",
            "capital":9.10,
            "votes":5.40
         },
         {
            "name":"Investor",
            "capital":7.20,
            "votes":22.50
         },
         {
            "name":"PRIMECAP Management Company",
            "capital":4.00,
            "votes":2.30
         },
         {
            "name":"Swedbank Robur Fonder AB",
            "capital":4.00,
            "votes":2.40
         },
         {
            "name":"BlackRock Fund Advisors",
            "capital":3.60,
            "votes":2.10
         },
         {
            "name":"AB Industrivärden",
            "capital":2.60,
            "votes":15.10
         },
         {
            "name":"AMF Pensionsförsäkring AB",
            "capital":2.50,
            "votes":2.80
         },
         {
            "name":"Vanguard Group",
            "capital":2.50,
            "votes":1.60
         },
         {
            "name":"Handelsbankens Pensionsstiftelse",
            "capital":0.70,
            "votes":4.10
         },
         {
            "name":"AFA Försäkring AB",
            "capital":0.50,
            "votes":2.00
         }
      ],
      "updated":"2019-12-31"
   }
}

# Avanza.FUND
https://avanza.se/_mobile/market/fund/2253

{
   "hasInvestmentFees":true,
   "buyable":true,
   "administrators":"Geir Lode",
   "sellable":true,
   "description":"Fonden är en aktivt förvaltad aktiefond som placerar i företag i olika branscher på de globala aktiemarknaderna. Urvalet av aktier i fonden baseras på en kombination av finansiell analys och hållbarhetsanalys som analyserar hur bolagen hanterar risker och möjligheter när det gäller miljö, sociala frågor samt affärsetik.",
   "isin":"SE0000837205",
   "risk":5,
   "domicile":"Sverige",
   "riskLevel":"MIDDLE",
   "sharpeRatio":0.58,
   "startDate":"1990-11-27",
   "tradingCurrency":"SEK",
   "managementFee":1.50,
   "prospectus":"http://doc.morningstar.com/document/b0561a999b9778b191cebc624ae21db9.msdoc/?clientid=avanza&key=3728b8f503435715",
   "buyFee":0.00,
   "capital":14352222014.00,
   "normanAmount":0.00,
   "rating":4,
   "sellFee":0.00,
   "standardDeviation":15.97,
   "loanFactor":70.00,
   "name":"Länsförsäkringar Global Hållbar A",
   "id":"2253",
   "NAV":50.54,
   "NAVLastUpdated":"2020-05-28T00:00:00.000+0200",
   "changeSinceOneDay":0.77,
   "changeSinceOneWeek":2.45,
   "changeSinceOneMonth":1.31,
   "changeSinceThreeMonths":1.59,
   "changeSinceSixMonths":-4.71,
   "changeSinceTurnOfTheYear":-5.17,
   "changeSinceOneYear":3.96,
   "changeSinceThreeYears":26.76,
   "changeSinceFiveYears":35.66,
   "changeSinceTenYears":130.39,
   "relatedFunds":[
      {
         "changeSinceOneYear":7.03,
         "name":"Länsförsäkringar Fossilsmart",
         "id":"827673"
      },
      {
         "changeSinceOneYear":7.88,
         "name":"Länsförsäkringar Sverige Aktiv A",
         "id":"1910"
      },
      {
         "changeSinceOneYear":-1.73,
         "name":"SEB Hållbarhetsfond Global",
         "id":"2254"
      },
      {
         "changeSinceOneYear":10.82,
         "name":"SEB Hållbarhetsfond Sverige C SEK - Lux",
         "id":"1907"
      },
      {
         "changeSinceOneYear":14.78,
         "name":"Länsförsäkringar Småbolag Sverige A",
         "id":"2011"
      }
   ],
   "fundCompany":{
      "homePage":"",
      "name":"Länsförsäkringar"
   },
   "numberOfOwners":2191,
   "autoPortfolio":false,
   "otherFees":"",
   "subCategory":"Global, mix bolag",
   "type":"Aktiefond"
}


# Avanza.BOND
(Obligation)
https://avanza.se/_mobile/market/bond/572908

{
   "loanFactor":30.00,
   "marketPlace":"NGM",
   "pushPermitted":true,
   "hasInvestmentFees":false,
   "priipDocumentUrl":"https://www.avanza.se/avanzabank/hem/konton/blanketter/allmanna/priip_kid_obligationer.pdf",
   "currency":"SEK",
   "lowestPrice":79.40,
   "highestPrice":83.00,
   "totalVolumeTraded":70000,
   "tradable":true,
   "lastPrice":83.00,
   "lastPriceUpdated":"2020-05-27T15:22:39.000+0200",
   "change":3.50,
   "changePercent":4.40,
   "totalValueTraded":56990.00,
   "isin":"SE0007131883",
   "tickerSymbol":"ESTEA KAPBEVIS3",
   "flagCode":"SE",
   "quoteUpdated":"2020-05-27T17:29:42.017+0200",
   "name":"ESTEA KAPBEVIS3",
   "id":"572908",
   "priceOneWeekAgo":77.00,
   "priceOneMonthAgo":79.00,
   "priceSixMonthsAgo":102.80,
   "priceAtStartOfYear":103.20,
   "priceOneYearAgo":98.40,
   "priceThreeYearsAgo":99.00,
   "priceThreeMonthsAgo":100.70,
   "tradingUnit":10000
}


# Avanza.OPTION
https://avanza.se/_mobile/market/option/1087813
{
   "marketPlace":"Stockholmsbörsen",
   "pushPermitted":false,
   "quoteUpdated":"2020-05-27T18:00:00.738+0200",
   "name":"OMXS300R05Y1460",
   "id":"1087813",
   "currency":"SEK",
   "totalVolumeTraded":0,
   "tradable":true,
   "change":0.00,
   "changePercent":0.00,
   "totalValueTraded":0.00,
   "isin":"SE0014289088",
   "priipDocumentUrl":"http://www.nasdaqomx.com/transactions/markets/optionsfutures/europe/product-information/kid",
   "hasInvestmentFees":false,
   "tickerSymbol":"OMXS300R05Y1460",
   "flagCode":"SE",
   "priceOneWeekAgo":44.00,
   "underlyingOrderbook":{
      "name":"OMX Stockholm 30",
      "id":"19002",
      "type":"INDEX",
      "currency":"SEK",
      "lowestPrice":1606.56,
      "highestPrice":1633.79,
      "totalVolumeTraded":116627050,
      "lastPrice":1623.39,
      "lastPriceUpdated":"2020-05-27T17:30:00.165+0200",
      "change":16.74,
      "changePercent":1.04,
      "updated":"2020-05-27T17:30:00.165+0200",
      "tickerSymbol":"OMXS30",
      "flagCode":"SE"
   },
   "endDate":"2020-06-05",
   "callIndicator":"PUT",
   "contractSize":100,
   "exerciseType":"EUROPEAN",
   "strikePrice":1460.00,
   "underlyingCurrency":"SEK"
}


# Avanza.FUTURE_FORWARD
https://avanza.se/_mobile/market/future_forward/914880

{
   "marketPlace":"Stockholmsbörsen",
   "pushPermitted":false,
   "currency":"SEK",
   "tradable":true,
   "lowestPrice":1602.75,
   "highestPrice":1630.50,
   "totalVolumeTraded":139237,
   "isin":"SE0012062594",
   "buyPrice":1616.75,
   "sellPrice":1619.25,
   "lastPrice":1618.50,
   "lastPriceUpdated":"2020-05-27T17:58:06.000+0200",
   "change":18.50,
   "changePercent":1.16,
   "totalValueTraded":2147476579.00,
   "tickerSymbol":"OMXS300F",
   "flagCode":"SE",
   "quoteUpdated":"2020-05-27T17:59:59.535+0200",
   "priipDocumentUrl":"http://www.nasdaqomx.com/transactions/markets/optionsfutures/europe/product-information/kid",
   "hasInvestmentFees":false,
   "name":"OMXS300F",
   "id":"914880",
   "priceOneWeekAgo":1552.25,
   "priceOneMonthAgo":1536.20,
   "priceSixMonthsAgo":1602.50,
   "priceAtStartOfYear":1602.50,
   "priceThreeMonthsAgo":1847.50,
   "underlyingOrderbook":{
      "currency":"SEK",
      "lowestPrice":1606.56,
      "highestPrice":1633.79,
      "totalVolumeTraded":116627050,
      "lastPrice":1623.39,
      "lastPriceUpdated":"2020-05-27T17:30:00.165+0200",
      "change":16.74,
      "changePercent":1.04,
      "updated":"2020-05-27T17:30:00.165+0200",
      "tickerSymbol":"OMXS30",
      "flagCode":"SE",
      "name":"OMX Stockholm 30",
      "id":"19002",
      "type":"INDEX"
   },
   "endDate":"2020-06-18",
   "contractSize":100,
   "underlyingCurrency":"SEK"
}


# Query CERTIFICATE
https://avanza.se/_mobile/market/certificate/804912

{
   "marketPlace":"First North Stockholm",
   "pushPermitted":true,
   "quoteUpdated":"2020-05-27T19:47:17.003+0200",
   "priipDocumentUrl":"https://api.priiphub.com/hub/kid-portal/kid/identifier/GB00BW6Q2219?documentType=pdf&jurisdiction=SE&language=SV",
   "hasInvestmentFees":true,
   "name":"BEAR AIRBUS X5 AVA 1",
   "id":"804912",
   "currency":"SEK",
   "isin":"GB00BW6Q2219",
   "tradable":true,
   "totalVolumeTraded":0,
   "lastPrice":0.967,
   "lastPriceUpdated":"2020-05-26T20:30:00.000+0200",
   "change":0.000,
   "changePercent":0.00,
   "totalValueTraded":0.00,
   "tickerSymbol":"BEAR AIRBUS X5 AVA 1",
   "flagCode":"SE",
   "priceThreeMonthsAgo":0.987,
   "priceOneWeekAgo":0.967,
   "priceOneMonthAgo":1.15,
   "priceSixMonthsAgo":1.06,
   "priceAtStartOfYear":1.08,
   "priceOneYearAgo":5.44,
   "underlyingOrderbook":{
      "name":"Airbus SE",
      "id":"745811",
      "type":"STOCK",
      "currency":"EUR",
      "lowestPrice":60.72,
      "highestPrice":64.29,
      "totalVolumeTraded":5266681,
      "lastPrice":61.13,
      "lastPriceUpdated":"2020-05-27T17:40:00.375+0200",
      "change":-1.68,
      "changePercent":-2.67,
      "updated":"2020-05-27T17:40:00.375+0200",
      "buyPrice":61.22,
      "sellPrice":61.45,
      "tickerSymbol":"AIRp",
      "flagCode":"FR"
   },
   "assetRootCategory":"Aktier",
   "assetSubCategory":"Enskild aktie",
   "assetSubSubCategory":"Airbus",
   "issuerName":"Morgan Stanley",
   "direction":"SHORT",
   "shortName":"BEAR AIRBUS X5 AVA 1",
   "leverage":5.00,
   "prospectus":"https://www.morganstanley.com/ied/etp-server/webapp/svc/document/finalTermsheetVersion?isin=GB00BW6Q2219&version=1",
   "administrationFee":0.00,
   "underlyingCurrency":"EUR"
}


# Avanza.WARRANT
https://avanza.se/_mobile/market/warrant/718858

{
   "marketPlace":"First North Stockholm",
   "pushPermitted":true,
   "name":"MINI L AMAZON AVA 17",
   "id":"718858",
   "currency":"SEK",
   "highestPrice":1539.00,
   "lowestPrice":1539.00,
   "lastPrice":1539.00,
   "lastPriceUpdated":"2020-05-27T15:34:53.000+0200",
   "change":-39.76,
   "changePercent":-2.52,
   "totalVolumeTraded":2,
   "totalValueTraded":3078.00,
   "tradable":true,
   "isin":"GB00BVZZ8M45",
   "tickerSymbol":"MINI L AMAZON AVA 17",
   "flagCode":"SE",
   "priipDocumentUrl":"https://api.priiphub.com/hub/kid-portal/kid/identifier/GB00BVZZ8M45?documentType=pdf&jurisdiction=SE&language=SV",
   "hasInvestmentFees":true,
   "quoteUpdated":"2020-05-27T20:00:00.100+0200",
   "priceOneWeekAgo":1541.59,
   "priceOneMonthAgo":1631.04,
   "priceSixMonthsAgo":926.22,
   "priceAtStartOfYear":1021.88,
   "priceOneYearAgo":1027.40,
   "priceThreeYearsAgo":222.34,
   "priceThreeMonthsAgo":1136.41,
   "underlyingOrderbook":{
      "name":"Amazon.com Inc",
      "id":"3986",
      "type":"STOCK",
      "currency":"USD",
      "buyPrice":2412.00,
      "sellPrice":2412.99,
      "highestPrice":2413.58,
      "lowestPrice":2330.00,
      "lastPrice":2410.39,
      "lastPriceUpdated":"2020-05-27T22:00:02.267+0200",
      "change":-11.47,
      "changePercent":-0.47,
      "updated":"2020-05-27T22:00:57.145+0200",
      "totalVolumeTraded":4981045,
      "tickerSymbol":"AMZN",
      "flagCode":"US"
   },
   "issuerName":"Morgan Stanley",
   "direction":"LONG",
   "callIndicator":"CALL",
   "strikePrice":674.97,
   "barrierPrice":833.77,
   "finalTerms":"https://www.morganstanley.com/ied/etp-server/webapp/svc/document/finalTermsheetVersion?isin=GB00BVZZ8M45&version=1",
   "financingLevel":794.125577,
   "parity":10.0000,
   "warrantType":"MINI_FUTURE",
   "underlyingCurrency":"USD"
}

# Avanza.EXCHANGE_TRADED_FUND
https://avanza.se/_mobile/market/exchange_traded_fund/924016

{
   "loanFactor":0.00,
   "marketPlace":"Stockholmsbörsen",
   "pushPermitted":true,
   "hasInvestmentFees":true,
   "priipDocumentUrl":"https://www.lyxoretf.com/pdfDocuments/KIID/KIID_LU1563454310_SE_20190219_SWE.pdf",
   "currency":"SEK",
   "lowestPrice":573.50,
   "highestPrice":573.50,
   "totalVolumeTraded":2,
   "tradable":true,
   "lastPrice":573.50,
   "lastPriceUpdated":"2020-05-27T11:59:06.000+0200",
   "change":0.00,
   "changePercent":0.00,
   "totalValueTraded":1147.00,
   "isin":"LU1563454310",
   "tickerSymbol":"LYXGREENBOND",
   "flagCode":"SE",
   "quoteUpdated":"2020-05-27T17:25:00.031+0200",
   "name":"LYX ETF Green Bond (DR) ACC",
   "id":"924016",
   "priceOneWeekAgo":572.50,
   "priceOneMonthAgo":584.80,
   "priceSixMonthsAgo":572.50,
   "priceAtStartOfYear":561.80,
   "priceOneYearAgo":557.20,
   "priceThreeMonthsAgo":588.00,
   "assetRootCategory":"Räntor",
   "assetSubCategory":"Sustainability",
   "issuerName":"Lyxor",
   "direction":"LONG",
   "leverage":1.00,
   "managementFee":0.25
}

# Avanza.INDEX
https://avanza.se/_mobile/market/index/961717

{
   "priceOneWeekAgo":1522.96,
   "priceOneMonthAgo":1503.05,
   "priceSixMonthsAgo":1713.86,
   "priceAtStartOfYear":1746.39,
   "priceOneYearAgo":1543.06,
   "priceThreeMonthsAgo":1687.80,
   "pushPermitted":true,
   "currency":"SEK",
   "lowestPrice":1567.93,
   "highestPrice":1595.69,
   "lastPrice":1585.40,
   "lastPriceUpdated":"2020-05-27T17:29:58.166+0200",
   "change":17.38,
   "changePercent":1.11,
   "flagCode":"SE",
   "quoteUpdated":"2020-05-27T17:29:58.166+0200",
   "name":"OMX Stockholm 30 ESG Responsible Index",
   "id":"961717"
}




# Avanza.PREMIUM_BOND
TODO: Find example

# Avanza.SUBSCRIPTION_OPTION
TODO: Find example

This shoudl be
https://www.avanza.se/aktier/om-aktien.html/938148/addvise-group-to-1

THis returns SUBSCRIPTION_OPTION
https://www.avanza.se/_mobile/market/search?query=addvise-group-to-1&limit=5

But not found ??
https://avanza.se/_mobile/market/subscription_option/938148

Same for 995642.

# Avanza.EQUITY_LINKED_BOND
TODO: Find example

# Avanza.CONVERTIBLE
TODO: Find example


instrumentType: RIGHT. PAPI BTA??
https://www.avanza.se/_mobile/market/search?query=Papilly%20BTA&limit=5


# Search examples

* Option 1. Search among all. https://www.avanza.se/_mobile/market/search?query=airbus&limit=5
* Option 2. Search only within a given instrument. https://www.avanza.se/_mobile/market/search/INDEX?query=omx&limit=5


