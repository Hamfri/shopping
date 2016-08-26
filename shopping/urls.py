from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from catalog import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('catalog.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^checkout/', include('checkout.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^search/', include('search.urls')),
]
handler404 = 'catalog.views.file_not_found_404'
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    