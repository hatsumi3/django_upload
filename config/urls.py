from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ai_image.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]