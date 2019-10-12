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

from django.views.generic import TemplateView

# Create your views here.


class YoutubeAnalytics(TemplateView):
	template_name = "youtube_video_page.html"
	template_404 = "404.html"

	def post(self,request): 
		if request.method =='POST':
			video_obj = self.get_video_object(request.POST['video_id'])
			#print(request.POST)
			if  'value' in request.POST:
				video_remining = request.POST['value']
				video_obj.youtube_minuts_watched = video_remining
				video_obj.save()
				#TODO COMPLETION PERCENTAGE VARIABLE
				#DIVES THE DUR OF VIDEO WITH THE MIN WATCHED 
				# TURNS IT INTO PERCANTAGE AND THEN PROGRESS BAR CHANGES FOR EACH VIDEO

			context = {'video': video_obj}
			return render(request, self.template_name, context)
		else:
			return render(request, self.template_404)

	def get_video_object(self,video_id):
		video_obj = get_object_or_404(Youtube,id=video_id)
		return video_obj


class YoutubePage(TemplateView):
	#there will be more controls and functions in this class
	template_name = "youtube_page.html"
	def get(self, request):
		#self.request_youtube()
		videos = Youtube.objects.all()
		context = {'videos':videos}
		return render(request, self.template_name, context)



	def request_youtube(self):
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
			#print(result)
			if Youtube.objects.filter(youtube_video_title=result['snippet']['title']).exists():
				print("already exists")
			else :
				youtube_search = Youtube.objects.create(
					youtube_video_title = result['snippet']['title'],
					youtube_video_url = f'https://www.youtube.com/embed/{ result["id"]}',
					yotube_video_length = int(parse_duration(result['contentDetails']['duration']).total_seconds()//60)
					,youtube_video_thum_url =  result['snippet']['thumbnails']['high']['url']
					)



class UdemyCoursePage(TemplateView):
	template_name ="udemy_page.html"
	def get(self, request):
		self.udemy_courses()
		qs = Lectures.objects.all() # query list of obj
		context = {'object_list':qs}
		return render(request, self.template_name,context)
	#request Udemy courses from courses page
	def udemy_courses(self):
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

# REQUEST VIDEO FROM YOUTUBE


