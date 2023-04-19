from rest_framework import serializers
from .models import Pageperformance

class PageperformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pageperformance
        fields = ('id', 'input_url', 'output_data')