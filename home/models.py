from django.db.models import (
	Model,DateTimeField,UUIDField,CharField,BooleanField,ImageField,ForeignKey,CASCADE,
	IntegerField,ManyToManyField,FileField)
from authentication.models import User
from abc import ABC
import uuid
from django.db import models	
from django.conf import settings
from audiofield.fields import AudioField
import os.path
# from random	import shuffle
# from itertools import chain 

def get_token():
    return str(uuid.uuid4())


class SomeAbstractModel(Model):
    id = UUIDField(default=get_token, editable=False, unique=True,primary_key=True)
    updated = DateTimeField(auto_now=True)
    created = DateTimeField(auto_now_add=True)



class NewsFeeds(SomeAbstractModel):
    picture = ImageField(upload_to="posts/img")
    body = CharField(max_length=255)
    author = ForeignKey(User,on_delete = CASCADE,null=True)
    likes = ManyToManyField(User,default=None,blank=True,related_name="likers")

    def get_likes(self):
        return self.liked.all()

    def like_count(self):
        return self.liked.all().count()


    def get_user_like():
        pass

class Sermons(SomeAbstractModel):
	name = CharField(max_length=255)
	image = ImageField(upload_to="sermon_images",default="11.jpg")
	title = CharField(max_length=255)
	description = CharField(max_length=255)
	video = CharField(max_length=255) #This will be the url to the youtube video

class SermonAttendance(SomeAbstractModel): # The number of people that have attended te service
	male = IntegerField()
	female = IntegerField()
	children = IntegerField()
	count_by = ForeignKey(User,on_delete=CASCADE)

	def total(self):
		total = male+female+children
		return str(total)

class Announcements(SomeAbstractModel):
	title = CharField(max_length=255)
	description = CharField(max_length=255)
	verse = CharField(max_length=255)

class Testimonies(SomeAbstractModel):
	name = CharField(max_length=255)
	testimony = CharField(max_length=255)


class About(SomeAbstractModel):
	Title = CharField(max_length=255)
	description = CharField(max_length=255)

class Feedback(SomeAbstractModel):
	Title = CharField(max_length=255)
	description = CharField(max_length=255)





class Album(Model):
    artist = CharField(max_length=200)
    album_title = CharField(max_length=300)
    album_logo = CharField(max_length=1000)

    def __str__(self):
        return self.album_title + '-' + self.artist

class AudioSermon(Model):
   album = ForeignKey(Album, on_delete=CASCADE)
   file_type = CharField(max_length=10)
   sermon_title = CharField(max_length=250)
   afile = models.FileField(upload_to='musics/')
   audio_file = AudioField(upload_to='your/upload/dir', blank=True,
                        ext_whitelist=(".mp3", ".wav", ".ogg"),
                        help_text=("Allowed type - .mp3, .wav, .ogg"))
   def audio_file_player(self):
    """audio player tag for admin"""
    if self.audio_file:
        file_url = settings.MEDIA_URL + str(self.audio_file)
        player_string = '<audio src="%s" controls>Your browser does not support the audio element.</audio>' % (file_url)
        return player_string

   audio_file_player.allow_tags = True
   audio_file_player.short_description = ('Audio file player')

   def __str__(self):
       return self.sermon_title
