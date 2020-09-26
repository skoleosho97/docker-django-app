from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from core import settings
from core.views import HealthCheckView, hello_world

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("dj_rest_auth.urls"), name="auth"),
    path("api/hello_world/", hello_world, name="hello_world"),
    path("api/accounts/", include("accounts.urls"), name="accounts"),
    path("api/site/", include("coursesite.urls"), name="site"),
    path("health_check/", HealthCheckView.as_view(), name="health_check"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
