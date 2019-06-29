# api/urls.py
from django.urls import include, path, re_path
from django.views.generic import TemplateView
# from django.conf.urls import url

from api import views
# from rest_framework.urlpatterns import format_suffix_patterns

#  Define regular expression for email confirmation view
email_conf_regex = r"[\s\d\w().+-_',:&]+"

# app_name = 'api'
urlpatterns = [
    path('', TemplateView.as_view(
        template_name='base.html'), name='base'),
    path('<uuid:invitation_id>/', views.party_detail),
    path('<uuid:invitation_id>/guests/', views.party_guests),
    path('<uuid:invitation_id>/guests/<int:id>/', views.rsvp_guest),
    path('guests/', views.guest_list),
    path('parties/', views.party_list),
    path('events/', views.events),
    path('locations/', views.locations),
    path('locations/<int:id>/', views.location_detail),
    path('events/<int:id>/', views.event_detail),
]