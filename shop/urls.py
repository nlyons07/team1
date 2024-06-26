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
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
    path('', views.product_list, name='product_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout', views.logout, name='logout'),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list_by_category, name='product_list_by_category'),
    path('products/', views.product_list, name='product-list'),

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',  # Update with your actual template path
        email_template_name='registration/password_reset_email.html',  # Update with your actual template path
        success_url='reset_password_done'
    ), name='reset_password'),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'  # Update with your actual template path
    ), name='reset_password_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',  # Update with your actual template path
        success_url='reset_password_complete'
    ), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'  # Update with your actual template path
    ), name='reset_password_complete'),



    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
