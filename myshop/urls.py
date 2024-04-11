from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('', include('shop.urls', namespace='shop')),
    path('accounts/', include('django.contrib.auth.urls')),


    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='your_app/password_reset_form.html',
        email_template_name='your_app/password_reset_email.html',
        success_url='reset_password_done'
    ), name='reset_password'),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='your_app/password_reset_done.html'
    ), name='reset_password_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='your_app/password_reset_confirm.html',
        success_url='reset_password_complete'
    ), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='your_app/password_reset_complete.html'
    ), name='reset_password_complete'),


    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),  # serve media files when deployed
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root':
    settings.STATIC_ROOT}),  # serve static files when deployed

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
