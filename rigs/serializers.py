from rest_framework import serializers
from .models import Rig
from likes.models import Like
from stars.models import Star


class RigSerializer(serializers.ModelSerializer):
    """
    Serializer for the Rig model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    star_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()
    stars_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, rig=obj
            ).first()
            return like.id if like else None
        return None

    def get_star_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            star = Star.objects.filter(
                owner=user, rig=obj
            ).first()
            return star.id if star else None
        return None

    class Meta:
        model = Rig
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'name', 'category', 'description', 'gear_list',
            'featured_image', 'image_2', 'image_3', 'image_4',
            'attribute_1', 'attribute_2', 'budget', 'genre_1',
            'genre_2', 'like_id', 'star_id', 'comments_count',
            'likes_count', 'stars_count', 'featured'
        ]
