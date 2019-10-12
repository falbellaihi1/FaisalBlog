from django.urls import include, path, re_path
from lectures.views import (
    home_page,
    UdemyCoursePage,
    YoutubePage,
    YoutubeAnalytics,

    )

urlpatterns = [
    path('',home_page),
    path('home/',home_page),
    path('udemy/', UdemyCoursePage.as_view()),
    path('youtube/', YoutubePage.as_view()),
    path('video/', YoutubeAnalytics.as_view()),



]