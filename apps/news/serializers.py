from rest_framework import serializers
from .models import NewsCategory, News, Comment, Banners
from apps.xfzauth.serializers import UserSerializers


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ('id', 'name')


class NewsSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    author = UserSerializers()

    class Meta:
        model = News
        fields = ('id', 'title', 'desc', 'thumbnail', 'pub_time', 'category', 'author')


class CommentSerializers(serializers.ModelSerializer):
    author = UserSerializers()

    class Meta:
        model = Comment
        fields = ('id', 'content', 'author')


class BannersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banners
        fields = ('id', 'priority', 'image_url', 'link_to')

