from pytrends.request import TrendReq

pytrends = TrendReq()
realtime_india = pytrends.realtime_trending_searches(pn='IN')
print(realtime_india)
realtime_india_top10 = realtime_india.head(10)
print(realtime_india_top10)