import debug_toolbar
from django.contrib import admin
from django.urls import path,include
from . import settings
from django.urls.conf import re_path
from django.views.static import serve
from django.conf.urls.static import static
from django.urls import include, path


admin.site.site_header = "Bespoke Administration"
admin.site.site_title = "Bespoke Administration"
admin.site.index_title = "Bespoke Admin"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("dashboard.urls")),
    path("users/", include("users.urls")),
    path("accounting/", include("accounting.urls")),
    path("items/", include("item.urls")),
    path("sales/", include("sales.urls")),
    path("masters/", include("masters.urls")),
    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$',serve,{'document_root':settings.STATIC_ROOT}),
    path('__debug__/',include(debug_toolbar.urls)),

]
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    
