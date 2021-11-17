from django.contrib import admin
from django.urls import path
from task1.views import ReviewEmailView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('reviews/',ReviewEmailView.as_view(),name = "reviews"),
]
