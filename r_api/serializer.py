from rest_framework import serializers
from .models import Artical


class ArticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artical
        fields = ['id', 'title', 'author']












    '''

    def create(self, validated_data):
        return Artical.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

    '''