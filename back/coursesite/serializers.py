from rest_framework import serializers

from coursesite.models import Course, Post, Category


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("title", "slug", "semester")


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "title",
            "slug",
            "course",
            "author",
            "created_on",
            "updated_on",
            "content",
            "categories",
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "title"
