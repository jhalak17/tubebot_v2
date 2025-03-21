from trendspy import Trends
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TrendingWordsView(APIView):
    def get(self, request):
        print("************** COMING *************")
        try:
            tr = Trends()
            trends = tr.trending_now(geo="IN")
            top10_trending_list = [trend.keyword.capitalize() for trend in trends[0:15]]
            return Response({'keywords':top10_trending_list}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Failed to fetch data'}, status=status.HTTP_400_BAD_REQUEST)