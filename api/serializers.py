from rest_framework import serializers

from congregation_portal import models as shared_models
from territory import models as territory_models


class CongregationSerializer(serializers.ModelSerializer):
    class Meta:
        model = shared_models.Congregation


class TerritorySerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField('get_items')
    congregation = serializers.PrimaryKeyRelatedField()

    def get_items(self, obj):
        if obj is None:
            return None

        return obj.get_item_count()

    class Meta:
        model = territory_models.Territory
        fields = ('id', 'number', 'name', 'type', 'items', 'congregation')

class TerritoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = territory_models.TerritoryItem
