from django.contrib import admin
from django.urls import path, include

# To customize the headings of admin site
admin.site.site_header = "Storefront Admin"
admin.site.index_title = "Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('store/', include('store.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
