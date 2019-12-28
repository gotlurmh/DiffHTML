
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from diff_app.views import api, form

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'form', form),
    path('api', api, name='api'),
]
