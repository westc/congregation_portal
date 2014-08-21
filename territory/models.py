from django.db import models

from congregation_portal import lists
from congregation_portal import models as shared_models


TERRITORY_TYPE = (
    ('H', 'Home'),
    ('P', 'Phone'),
)


class Territory(models.Model):
    number = models.CharField(max_length=5L)
    name = models.CharField(max_length=100L)
    type = models.CharField(max_length=1, choices=TERRITORY_TYPE)
    congregation = models.ForeignKey(shared_models.Congregation)

    def get_items(self):
        """
        Return all territory items
        """
        return self.territoryitem_set.all()

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.type)


class TerritoryTag(models.Model):
    tag = models.CharField(max_length=30L)


class TerritoryItem(models.Model):
    territory = models.ForeignKey(Territory)
    phone_number = models.CharField(max_length=10L, blank=True)
    address1 = models.CharField(max_length=100L, blank=True)
    address2 = models.CharField(max_length=100L, blank=True)
    city = models.CharField(max_length=100L)
    state = models.CharField(max_length=2L, choices=lists.states)
    notes = models.TextField(blank=True)
    sort = models.PositiveIntegerField()


class TerritoryTaggedItem(models.Model):
    tag = models.ForeignKey(TerritoryTag)
    item = models.ForeignKey(TerritoryItem)
