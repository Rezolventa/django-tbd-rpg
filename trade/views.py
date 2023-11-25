from django.shortcuts import render
from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView


# class Trade(viewsets.GenericViewSet):
#     def get_serializer_class(self):
#         pass
#
#     def get_queryset(self):
#         pass
#
#     @action(detail=False, methods=['POST'])
#     def buy_items(self, request):
#         pass


class BuyItemView(APIView):
    def post(self, request):
        return Response({'message': 'test'})
