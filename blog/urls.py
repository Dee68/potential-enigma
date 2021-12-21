from django.urls import path
from . views import index, account_page

app_name = 'blog'

urlpatterns = [
    path('', index, name='home'),
    path('account/', account_page, name='account'),
]