from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import base64
from pyudemy import Udemy
from .models import Lectures, Youtube
from django import forms
import json
import os
from django.conf import settings
from isodate import parse_duration
import datetime
from datetime import time
from django.shortcuts import get_object_or_404
# Create your views here.


def greet_user():
	# just for fun!
	now = time(hour = 11)

	if now <= time(hour = 11) :
		print( "MORNING!")
	elif now > time(hour = 11) :
		print( "AFTERNOON!")




def home_page(request):
	#obj = Lectures.objects.get(id=50)
	template_name = 'home_page.html'
	context = {"title": " "}
	return render(request, template_name,context)

def about_page(request):
	about_title = "About Page"
	return render(request, "about.html", {"title": about_title})

def contact_page(request):
	contact_title = "contact Page"
	return render(request, "contact.html", {"title": about_title})


def example_page(request):
	context = {"title":"Example"}
	template_name = "home_page.html"
	return render(context)



def list_view(request):
	udemy_courses()
	qs = Lectures.objects.all() # query list of obj
	template_name ="udemy_page.html"
	context = {'object_list':qs}
	return render(request, template_name,context)
def retrieve_view(request):
	template_name ="Udemy_page.html"
	context = {'object_list':[]}
	return render(request, template_name,context)

def update_view(request):
	template_name ="Udemy_page.html"
	context = {'object_list':[]}
	return render(request, template_name,context)

def create_view(request): #TODO
	return
def delete_view(request):#TODO
	return


#request Udemy courses from courses page
def udemy_courses():
	#TODO PASS SEARCH QR TO FIND SERTAIN VIDS
	UDEMY_AUTH = settings.UDEMY_CLIENT_ID + ":" + settings.UDEMY_CLIENT_SECRET
	DATA_BYTES = UDEMY_AUTH.encode("utf-8")
	url = "https://www.udemy.com/api-2.0/courses/"
	encode_data = base64.b64encode(DATA_BYTES)
	json_data = requests.get(url,auth= HTTPBasicAuth(settings.UDEMY_CLIENT_ID	, settings.UDEMY_CLIENT_SECRET)).json()
	if json_data == 404: # wont do any thing handle errors later TODO
		print("JSON STATUS : " + json_data)

	course_list = json_data['results']
	for course in course_list:
		if Lectures.objects.filter(udemy_course_title=course['title']).exists():
			print("course already exists")
		else :
			udemy_course = Lectures.objects.create(
			udemy_course_thum = course['image_480x270'],
			udemy_course_title = course['title'],
			udemy_course_url =  f'https://www.udemy.com{course["url"]}'	,
			udemy_course_price = course['price'],
			udemy_course_id  = course['id'],
			udemy_course_instructor = course['visible_instructors'][0]['title']
			)





### DISPLAY THE LIST OF YOUTUBE VIDEOS 
def youtube_test(request):
	#request_youtube()
	videos = Youtube.objects.all()
	template_name = "youtube_page.html"
	context = {'videos':videos}
	return render(request, template_name, context)


def youtube_video_page(request):
	template_name = "youtube_video_page.html"
	video_id  = request.POST['video_id']
	video_obj = get_object_or_404(Youtube, id=video_id)
	context = {'video': video_obj}
	return render(request, template_name, context)

def update_seconds_watched():
	#TODO 
	print("seconds watched :" + 0)


# REQUEST VIDEO FROM YOUTUBE
def request_youtube():
	#TODO Search query
	video_id =[]
	search_url ="https://www.googleapis.com/youtube/v3/search"
	video_url = "https://www.googleapis.com/youtube/v3/videos"
	search_params ={ 'part' : 'snippet',
			'q':'c++',
			'maxResults':9,
			'key':settings.YOUTUBE_API_KEY,
			'type':'video'
	}
	data_json = requests.get(search_url, params=search_params)

	results = data_json.json()['items']
	for video in results:
		video_id.append(video['id']['videoId'])

	video_params = {
	'key':settings.YOUTUBE_API_KEY,
	'part' : 'snippet, contentDetails',
	'id' :','.join(video_id),
	'maxResults':9,
	}
	video_json = requests.get(video_url,params=video_params)
	results = video_json.json()['items']
	for result in results:
		print(result)
		if Youtube.objects.filter(youtube_video_title=result['snippet']['title']).exists():
			print("already exists")
		else :
			youtube_search = Youtube.objects.create(
				youtube_video_title = result['snippet']['title'],
				youtube_video_url = f'https://www.youtube.com/embed/{ result["id"]}',
				yotube_video_length = int(parse_duration(result['contentDetails']['duration']).total_seconds()//60)
				,youtube_video_thum_url =  result['snippet']['thumbnails']['high']['url']
				)

