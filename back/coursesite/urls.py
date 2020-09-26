from django.urls import include, path
from rest_framework.routers import DefaultRouter

from coursesite.views import CourseView

router = DefaultRouter()
router.register(r"courses", CourseView)

# app_name = "coursesite"

urlpatterns = [
    path("", include(router.urls)),
    # url(r"^$", views.index, name="index"),
    # url(r"^site/posts/(?P<course_slug>[a-z]{4}-[0-9]{3})$", views.posts, name="posts"),
    # url(
    # r"^site/post/(?P<course_slug>[a-z]{4}-[0-9]{3})/(?P<post_id>[0-9])$",
    # views.post,
    # name="post",
    # ),
]
