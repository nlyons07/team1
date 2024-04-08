from django.conf import settings
from django.template.defaulttags import url
from django.urls import path
from . import views
from django.urls import re_path
from django.views.static import serve
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'shop'


urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
    path('', views.product_list, name='product_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout', views.logout, name='logout'),


    ]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()