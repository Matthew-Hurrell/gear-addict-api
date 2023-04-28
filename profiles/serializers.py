from rest_framework import serializers
from .models import Profile
from fans.models import Fan


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    fan_id = serializers.SerializerMethodField()
    rigs_count = serializers.ReadOnlyField()
    fans_count = serializers.ReadOnlyField()
    idols_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_fan_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            fanboy = Fan.objects.filter(
               fan=user, idol=obj.owner 
            ).first()
            return fanboy.id if fanboy else None
        return None
        

    class Meta: 
        model = Profile 
        fields = [
            'id', 'owner', 'created_at', 'updated_at',
            'name', 'bio', 'image', 'header_image',
            'location', 'instruments', 'genres',
            'expertise', 'is_owner', 'fan_id',
            'rigs_count', 'fans_count', 'idols_count',
        ]
