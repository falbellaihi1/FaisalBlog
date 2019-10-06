from django.urls import include, path, re_path
from lectures.views import (
    home_page,
    about_page ,
    contact_page,
    list_view,
    youtube_test
    )
urlpatterns = [
    path('',home_page),
    path('home/',home_page),
    path('about/',about_page),
    path('contact/',contact_page),
    path('udemy/', list_view),
    path('youtube/', youtube_test),

]
