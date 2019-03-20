from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer

"""
Stock API Class Base View
"""


class StockList(APIView):

    """
    Will give all records
    """
    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

    """
    will add new record
    URL: stocks/
    """
    def post(self):
        pass
