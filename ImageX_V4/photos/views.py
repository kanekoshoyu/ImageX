from django.http import HttpResponse, Http404
from .models import Picture, Tag, Category, Invitation
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from photos.forms import RegForm, EditProfileForm, FriendInviteForm
from django.views import generic
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import get_object_or_404
#forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def index(request):
    
    query = request.GET.get("q")
    if 'categorySearch' in request.GET:
        try:
            requiredCategory = Category.objects.all().get(text=query)
            requiredPicture = requiredCategory.picture_set.all().distinct()
        except Category.DoesNotExist:
            requiredCategory = None
            requiredPicture = None
    elif 'tagSearch' in request.GET:
        try:
            requiredTag = Tag.objects.all().get(text=query)
            requiredPicture = requiredTag.picture_set.all().distinct()
        except Tag.DoesNotExist:
            requiredTag = None
            requiredPicture = None
    elif 'photographerSearch' in request.GET:
        try:
            requiredPicture = Picture.objects.all().filter(uploader_name=query).distinct()
        except Picture.DoesNotExist:
            requiredPicture = None
    else:
        requiredPicture = Picture.objects.all()
    return render(request, 'index.html', {'pictures': requiredPicture})
        
        


class DetailView(generic.DetailView):
    model = Picture
    template_name ='detail.html'


class PictureCreate(CreateView):
    model = Picture
    fields = ['title', 'description', 'category', 'tag', 'file', 'uploader_name']
    #also create/add to a Tag
    def form_valid(self, form):
        my_picture_uploader = form.instance.uploader_name
        pictures = Picture.objects.all()
        num = pictures.filter(uploader_name=my_picture_uploader).count()
        if num < 3:
            success = True
        else:
            success = False
        if success:
            return super(PictureCreate, self).form_valid(form)
        else:
            return HttpResponse("User Can't Upload too many Photos")

def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/photos')
    else:
        form = RegForm()
    return render(request,'photos/registration_form.html',{'form': form})

def view_profile(request):
    args = {'user':request.user}
    return render(request, 'photos/profile.html',args)

def edit_profile(request):
    if request.method == 'POST':
        form=EditProfileForm(request.POST,instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/photos/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args={'form':form}
        return render(request, 'photos/edit_profile.html',args)

def change_password(request):
    if request.method =='POST':
        form = PasswordChangeForm(data=request.POST,user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/photos/profile')
        else:
            return redirect('/photos/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'photos/change_password.html', args)


def friend_invite(request):
    if request.method == 'POST':
        form = FriendInviteForm(request.POST)
        if form.is_valid():
            invitation = Invitation(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                code=User.objects.make_random_password(20),
                sender=request.user
            )
            invitation.save()
            invitation.send()
            return redirect('/photos/')
    else:
        form = FriendInviteForm()
    return render(request, 'friend_invite.html', {'form': form})


def friend_accept(request, code):
    invitation = get_object_or_404(Invitation, code__exact=code)
    request.session['invitation'] = invitation.id
    return redirect('/photos/register/')

