# api/urls.py
from django.urls import include, path, re_path
from django.views.generic import TemplateView
# from django.conf.urls import url

from api import views
# from allauth.account.views import ConfirmEmailView

# from rest_framework.urlpatterns import format_suffix_patterns

#  Define regular expression for email confirmation view
email_conf_regex = r"[\s\d\w().+-_',:&]+"

# app_name = 'api'
urlpatterns = [
    path('', TemplateView.as_view(
        template_name='api_instructions.html'), name='api_instructions'),
    # path('users/<str:username>/', views.user_detail),
    path('guests/', views.guest_list),
    path('<uuid:invitation_id>', views.party_detail),
    path('<uuid:invitation_id>/guests/', views.party_guests),
    path('<uuid:invitation_id>/guests/<int:id>/', views.rsvp_guest)

    # TEST URLS BELOW
    # path('example/', views.ExampleView.as_view()),
    # path('token-auth/', views.SFObtainAuthToken.as_view()),
    # path('get-token/', views.get_or_create_csrf_token),
    # path('accounts/', include('allauth.urls')),

    # path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login')
]

# urlpatterns = format_suffix_patterns(urlpatterns)
