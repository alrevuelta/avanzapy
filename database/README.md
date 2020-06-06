# database

This database addresses the problem of resolving the mapping between an instrument name (stock, fund, etf,...) with its corresponding id in avanza. With this databases this can be resolved locally without relying on an external query.

Currently the following instruments are supported:
* stocks.txt 9491 stocks. Format: id;ticker;name;market;field
* funds.txt 1295. Format: id;name