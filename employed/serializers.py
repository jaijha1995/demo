from rest_framework import serializers
from .models import employed


class employedSerializer(serializers.ModelSerializer):
    class Meta:
        model = employed
        fields = '__all__'


