
from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from datetime import datetime

class Gallery(models.Model):
    creater = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    logo = models.CharField(max_length=1000)
    def __str__(self):
        return self.title

class Photographer(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return "Photographer is" + self.name

class Tag(models.Model):
    text = models.CharField(max_length=100)
    
    def __str__(self):
        return "#" + self.text
    
class Category(models.Model):
    text = models.CharField(max_length=100)
    
    def __str__(self):
        return self.text

class Picture(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    file = models.FileField()
    uploader_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def get_absolute_url(self):
        return reverse('photos:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title + '-' + self.description

    def like(self):
        #this is not working...
        #Like.objects.create(picture=self, member=request.user)
        print("Liking (Class Function)")
        return "Liked"

    def download(self):
        #this is not working...
        print("Downloading (Class Function)")
        return "Downloading"

class Like(models.Model):
    member = models.ForeignKey(User, on_delete = models.CASCADE)
    picture = models.ForeignKey(Picture, on_delete = models.CASCADE)

class Download(models.Model):
    member = models.ForeignKey(User, on_delete = models.CASCADE)
    picture = models.ForeignKey(Picture, on_delete = models.CASCADE)

class member(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    
    def get_absolute_url(self):
        return reverse('photos:detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.title + '-' + self.description

class Invitation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    code = models.CharField(max_length=20)
    sender = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.sender.username + '-' + self.email
    def send(self):
        subject = "Invitation to join ImageX"
        link = 'http://' + settings.SITE_HOST + '/photos/accept/' + self.code + '/'
        template = get_template('invitation_email.txt')
        context ={
            'name': self.name,
            'link': link,
            'sender': self.sender.username,
        }
        message = template.render(context)
        send_mail(
            subject, 
            message,
            settings.DEFAULT_FROM_EMAIL, 
            [self.email],
        )







