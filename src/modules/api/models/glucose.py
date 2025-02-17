# Part of this code belongs to https://github.com/DarrenRiedlinger/glucose-tracker
# Changes and modifications were made to the technical
# requirements of the UnaHealthAPI coding challenge.


from django.db import models
from .time_stamped_model import TimeStampedModel


class GlucoseManager(models.Manager):
    def by_user(self, user_id, **kwargs):
        """
        Filter objects by the 'user_id' field.
        """
        return self.select_related().filter(user_id=user_id)

    def by_date(self, start_date, end_date, user_id, **kwargs):
        """
        Filter objects by date range.
        """
        resultset = self.by_user(user_id).filter(
            record_date__gte=start_date,
            record_date__lte=end_date,
        )

        return resultset.order_by("-record_date", "-record_time")


class Glucose(TimeStampedModel):
    objects = GlucoseManager()

    user_id = models.CharField("User ID", max_length=40, blank=False, null=False)
    record_date = models.DateField("Date", blank=False, null=False)
    record_time = models.TimeField("Time", blank=False, null=False)
    glucose_value = models.IntegerField("Glucose Value mg/dL", blank=False, null=False)

    def __unicode__(self):
        return str(self.glucose_value)

    class Meta:
        ordering = ["-record_date", "-record_time"]
        app_label = "api"
