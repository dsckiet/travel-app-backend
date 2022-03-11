from rest_framework import serializers
from blogs import models

class ArticleSerializer(serializers.ModelSerializer):

    # tags = TagSerializer(many = True, read_only = True)
    class Meta:
        model = models.Article
        fields = '__all__'
