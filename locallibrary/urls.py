from django.contrib import admin
from django.urls import path
from django.urls import include
import os
from django.contrib.auth import views as auth_views
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
     path('catalog/', include('catalog.urls')),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
]


from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
