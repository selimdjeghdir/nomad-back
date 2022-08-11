from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.models import FeatureCategory, Feature, User


class FeatureWriteSerializer(serializers.Serializer):
    features = serializers.ListField(child=serializers.IntegerField())

    def create(self, validated_data):
        features = validated_data['features']

        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            try:
                user.features.set(features)
            except IntegrityError:
                raise ValidationError('at least one feature ID is invalid')

        return {'features': [f.pk for f in user.features.all()] }


class FeatureReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ('id', 'description', )


class AllFeaturesSerializer(serializers.ModelSerializer):
    features = FeatureReadSerializer(many=True, read_only=True)

    class Meta:
        model = FeatureCategory
        fields = ('name', 'multiple_choices', 'features', )