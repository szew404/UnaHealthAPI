# Part of this code belongs to https://github.com/DarrenRiedlinger/glucose-tracker
# Changes and modifications were made to the technical
# requirements of the UnaHealthAPI coding challenge.

from django.db import models


class TimeStampedModel(models.Model):
    """
    Abstract base class that provides self-updating 'loaded' and 'modified'
    fields.
    """

    loaded = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
