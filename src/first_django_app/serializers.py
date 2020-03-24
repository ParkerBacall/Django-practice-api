from rest_framework import serializers
from .models import Pasta

class PastaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasta
        fields = (id, 'sauce', 'spiciness')