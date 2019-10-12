from django.db import models
from pyudemy import Udemy
# Create your models here.

class Lectures(models.Model):

	title = models.CharField(max_length=120) #max_len = 120
	content = models.TextField()
	# let me define here my attributes as a user in udemy
	udemy_number_subscribed_courses = models.TextField(default="until i figure a way to get it, this is default value")
	udemy_name = models.TextField(default="falbellaihi")
	udemy_completion_ratio = models.IntegerField(default=0)


	udemy_course_id = models.IntegerField(default=0)
	udemy_course_title = models.TextField(default="course title")
	category = models.TextField(default="course category")
	udemy_course_price = models.TextField(default= 0)
	udemy_course_instructor = models.TextField(default="UKNOWN")
	udemy_course_url = models.TextField(default = "UKNOWN")
	udemy_course_thum = models.TextField(default="thum url")
	updated = models.DateTimeField(auto_now = True, auto_now_add= False)
	timestamp = models.DateTimeField(auto_now = False, auto_now_add = True)



	def __unicode__(self):
		return self.title
	def __str__(self):
		return self.title


class Youtube(models.Model):
	
	youtube_video_title = models.CharField(default="title",max_length=300)
	youtube_video_url = models.TextField(default="url")
	yotube_video_id = models.TextField(default="id")
	youtube_video_thum_url = models.TextField(default="thum url")
	yotube_video_length = models.IntegerField(default=0)
	youtube_minuts_watched = models.IntegerField(default=0)
	youtube_video_description = models.TextField(default="UNKNWN")
	youtube_percentage_completed = models.IntegerField(default=0)


