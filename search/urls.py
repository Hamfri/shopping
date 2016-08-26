from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^results/$', views.results, name='search_results'),
]

    