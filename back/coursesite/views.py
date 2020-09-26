from django.shortcuts import render
from rest_framework import viewsets

from .serializers import CourseSerializer, PostSerializer, CategorySerializer
from .models import Course, Post


class CourseView(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


# def index(request, *args, **kwargs):
# posts = Post.objects.all()[:3]
# courses = Course.objects.all()

# context = {
# "posts": posts,
# "courses": courses,
# }

# return render(request, "site/index.html", context)


# def posts(request, course_slug, *args, **kwargs):
# course = Course.objects.get(slug=course_slug)
# posts = Post.objects.filter(course__id=course.id)
# courses = Course.objects.all()

# context = {
# "posts": posts,
# "courses": courses,
# "course": course,
# }

# return render(request, "site/posts.html", context)


# def post(request, course_slug, post_id, *args, **kwargs):
# post = Post.objects.get(id=post_id)

# context = {
# "post": post,
# }

# return render(request, "site/post.html", context)
