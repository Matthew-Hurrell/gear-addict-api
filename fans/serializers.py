from django.db import IntegrityError
from rest_framework import serializers
from .models import Fan


class FanSerializer(serializers.ModelSerializer):
    """
    Serializer for the Fan model
    Create method handles the unique constraint on 'fan' and 'idol'
    """
    fan = serializers.ReadOnlyField(source='fan.username')
    idol_name = serializers.ReadOnlyField(source='idol.username')

    class Meta:
        model = Fan
        fields = [
            'id', 'fan', 'created_at', 'idol', 'idol_name'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
