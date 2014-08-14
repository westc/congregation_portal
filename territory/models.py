from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

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


class Tag(models.Model):
    tag = models.CharField(max_length=30L)


class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')


class Phone(models.Model):
    territory = models.ForeignKey(Territory)
    number = models.CharField(max_length=10L)
    city = models.CharField(max_length=100L)
    state = models.CharField(max_length=2L, choices=lists.states)
    notes = models.TextField()


class Home(models.Model):
    territory = models.ForeignKey(Territory)
    number = models.CharField(max_length=10L)
    address1 = models.CharField(max_length=100L)
    address2 = models.CharField(max_length=100L)
    city = models.CharField(max_length=100L)
    state = models.CharField(max_length=2L, choices=lists.states)
    notes = models.TextField()
    tags = generic.GenericRelation(TaggedItem)
