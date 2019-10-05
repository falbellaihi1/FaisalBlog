from django.contrib import admin
from .models import Lectures, Youtube

# Register your models here.

class LectureAdmin(admin.ModelAdmin):
	list_display = ["title", "timestamp", "content","id", "updated"
	 , "udemy_course_id", "udemy_course_title","category"
	 ,"udemy_course_price","udemy_course_instructor","udemy_course_thum"]
	list_display_links = ["updated", "title", "content"]
	list_filter = ["updated", "timestamp"]
	search_fields = ["title","content","id"]
	class Meta:
		model = Lectures

class YotubeAdmin(admin.ModelAdmin):
	#list_display = ["title"]
	class Meta:
		model = Youtube

admin.site.register(Lectures, LectureAdmin)


admin.site.register(Youtube, YotubeAdmin)