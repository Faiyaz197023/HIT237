from django.contrib import admin
from django.urls import re_path,path
from .views import home_view, PestsView, PestDetailView,ProtectView,ProtectDetailView, DiseasesView, DiseaseDetailView,DiseaseProtectDetailView, DiseaseProtectionView,about_us

urlpatterns = [
    re_path(r'^$', home_view, name='home'),  # Matches root URL
    re_path(r'^pests/$', PestsView.as_view(), name='pests'),  # Matches /pests/
    re_path(r'^pest_detail/(?P<key>[a-zA-Z0-9_-]+)/$', PestDetailView.as_view(), name='pest_detail'),  # Matches e.g. /pest_detail/p1/
    re_path(r'^protect/$', ProtectView.as_view(), name="protect"),
    re_path(r'^protect_detail/(?P<key>[a-zA-Z0-9_-]+)/$', ProtectDetailView.as_view(), name="protect_detail"),
    re_path(r'^diseases/$', DiseasesView.as_view(), name='diseases'),
    re_path(r'^disease_detail/(?P<key>[a-zA-Z0-9_-]+)/$', DiseaseDetailView.as_view(), name='disease_detail'),
    re_path(r'^disease_protection/$', DiseaseProtectionView.as_view(), name='disease_protection'),
    re_path(r'^disease_protection/(?P<key>[\w-]+)/$', DiseaseProtectDetailView.as_view(), name='disease_protect_detail'),

    path('about/', about_us, name='aboutus'),
    re_path(r'^admin/', admin.site.urls),
]