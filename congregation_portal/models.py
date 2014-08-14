from django.db import models
from django.contrib.auth.models import User

from congregation_portal import lists


class Congregation(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L)
    city = models.CharField(max_length=100L)
    state = models.CharField(max_length=2L, choices=lists.states)

    def __unicode__(self):
        return "%s - %s, %s" % (self.name, self.city, self.state)


class Profile(models.Model):
    user = models.OneToOneField(User)
    congregation = models.ForeignKey(Congregation)
    admin = models.BooleanField(default=False)