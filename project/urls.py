from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

from project import settings

admin.site.site_header = 'Hiroshi'
admin.site.site_title = 'Hiroshi'

if not settings.DEBUG:
    from django_otp.admin import OTPAdminSite

    admin.site.__class__ = OTPAdminSite


def trigger_error(request):
    division_by_zero = 1 / 0
    print(division_by_zero)


def health_check(request):
    return HttpResponse(status=200)


urlpatterns = [
    path('trigger-error/', trigger_error),
    path('health-check/', health_check),
    path('config/', admin.site.urls),
    path('base/', include('base.urls')),
]
