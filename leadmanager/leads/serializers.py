from rest_framework import serializers
from .models import Lead


# Lead Serialzer


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = "__all__"