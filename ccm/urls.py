from ccm.views import *
from django.urls import path

urlpatterns = [
    path('get-mikoa/', GetMikoa.as_view(), name='get-mikoa'),
]