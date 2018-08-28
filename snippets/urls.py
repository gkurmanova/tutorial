from django.views.generic.base import RedirectView
from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets/', "website.views.url_redirect", name="url-redirect"),
]
