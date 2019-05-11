# api/serializers.py
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _
###### IMPORT YOUR USER MODEL ######
from .models import Guest, Party


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'


class PartyGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = '__all__'

# class PostSerializer(serializers.ModelSerializer):
#     posts = serializers.SerializerMethodField()
#     tags = serializers.SerializerMethodField()

#     class Meta:
#         model = Post
#         fields = '__all__'

#     def get_posts(self, obj):
#         qs = obj.post_content.all().order_by('id')
#         return PostTextSerializer(qs, many=True, read_only=True).data

#     def get_tags(self, obj):
#         qs = obj.tag.all().order_by('id')
#         return TagSerializer(qs, many=True, read_only=True).data


# class SampleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sample
#         fields = '__all__'
