from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as rest_views

from .views import *

# API endpoints
urlpatterns = format_suffix_patterns([

  url(r'^accounts$',
      AccountListViewHandler.as_view(),
      name='account-list'),

  url(r'^accounts/create$',
      AccountCreateViewHandler.as_view(),
      name='account-create'),

  url(r'^accounts/(?P<pk>[0-9]+)$',
        AccountDetailViewHandler.as_view(),
        name='account-detail'),

])

# Get the auth token for the user
urlpatterns += [
    url(r'^api-token-auth/', rest_views.obtain_auth_token)
]
# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                                namespace='rest_framework')),
]