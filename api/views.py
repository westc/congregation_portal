from rest_framework import viewsets, status
from rest_framework.response import Response

from territory import models as territory_models
from congregation_portal import models as shared_models
from api import serializers


class CongregationViewSet(viewsets.ModelViewSet):
    model = shared_models.Congregation
    serializer_class = serializers.CongregationSerializer


class TerritoryViewSet(viewsets.ModelViewSet):
    model = territory_models.Territory
    serializer_class = serializers.TerritorySerializer

    def list(self, request, *args, **kwargs):
        congregation = request.session['congregation']
        queryset = territory_models.Territory.objects.filter(congregation=congregation)

        serializer = serializers.TerritorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        congregation = request.session['congregation']
        pk = self.kwargs.get('pk', None)

        queryset = territory_models.Territory.objects.get(pk=pk,
                                                          congregation=congregation)

        serializer = serializers.TerritorySerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def pre_save(self, obj):
        congregation = self.request.session['congregation']
        obj.congregation = shared_models.Congregation.objects.get(pk=congregation)


class TerritoryItemViewSet(viewsets.ModelViewSet):
    model = territory_models.TerritoryItem
    serializer_class = serializers.TerritoryItemSerializer

    def list(self, request, *args, **kwargs):
        congregation = request.session['congregation']
        territory_id = self.kwargs.get('territory_id', None)

        queryset = territory_models.TerritoryItem.objects.filter(territory=territory_id,
                                                                 territory__congregation=congregation)

        serializer = serializers.TerritoryItemSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        congregation = request.session['congregation']
        territory_id = self.kwargs.get('territory_id', None)
        pk = self.kwargs.get('pk', None)

        queryset = territory_models.TerritoryItem.objects.filter(territory=territory_id,
                                                                 pk=pk,
                                                                 territory__congregation=congregation)

        serializer = serializers.TerritorySerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
