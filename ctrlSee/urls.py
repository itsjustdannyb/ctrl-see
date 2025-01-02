from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static, serve

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('base.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

