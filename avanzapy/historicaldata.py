class HistoricalData:
    def __init__(self,
                 historical_data,
                 chart_type,
                 chart_resolution,
                 time_period):
        #self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})
        self.historical_data = historical_data
        self.chart_type = chart_type
        self.chart_resolution = chart_resolution
        self.time_period = time_period

        # TODO Add first date? last date?
        # max/min variation?
