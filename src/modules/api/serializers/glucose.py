from rest_framework import serializers
from ..models.glucose import Glucose


class GlucoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Glucose
        fields = "__all__"
