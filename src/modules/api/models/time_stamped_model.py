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
