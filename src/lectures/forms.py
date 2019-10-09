from django import forms

# NONE FOR NOW

class VideoForm(forms.Form):
	# THIS WILL HANDLE THE VIDEO REMINING TIME TO WATCH 
	video_id = forms.IntegerField()
	remining = forms.IntegerField()

