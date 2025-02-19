from rest_framework import serializers
from ..models.glucose import Glucose


class GlucoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Glucose
        fields = "__all__"


class ExportGlucoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Glucose
        fields = ["user_id", "glucose_value", "record_date", "record_time"]
