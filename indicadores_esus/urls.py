from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path


def trigger_error(request):
    """Sentry testing purpose"""
    division_by_zero = 1 / 0


urlpatterns = [
    path("", include("indicadores_esus.core.urls")),
    #
    path("esus/", include("indicadores_esus.esus.urls")),
    path("indicadores/", include("indicadores_esus.indicator.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("sentry-debug/", trigger_error),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
