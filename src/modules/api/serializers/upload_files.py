from rest_framework import serializers
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _


class CSVUploadSerializer(serializers.Serializer):
    csv_file = serializers.FileField(
        validators=[
            FileExtensionValidator(allowed_extensions=["csv"]),
        ],
        label=_("CSV File"),
        help_text=_("Upload a CSV file with a maximum size of 2MB"),
    )

    def validate_csv_file(self, value):
        """
        Validates file size and format
        """

        # Max 2MB
        max_size = 2 * 1024 * 1024
        if value.size > max_size:
            raise serializers.ValidationError(
                _("File exceeds the maximum allowed size of 2MB")
            )

        # MIME Validation
        valid_mime_types = [
            "text/csv",
            "application/csv",
            "text/plain",
            "application/octet-stream",
        ]

        if value.content_type not in valid_mime_types:
            raise serializers.ValidationError(_("Invalid file type"))

        return value

    class Meta:
        fields = ("csv_file", "user")
