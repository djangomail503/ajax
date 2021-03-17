from django.shortcuts import render
from django.http import HttpResponse
from ajax_app import forms, models
from django.core import serializers
from django.http import JsonResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1 style='font: italic small-caps bold 148px/130px Georgia';>Welcome</h1>")


def indexView(request):
    form = FriendForm()
    friends = Friend.objects.all()
    return render(request, "index.html", {"form": form, "friends": friends})

def myuser(request):
    
    if request.is_ajax and request.method == "POST":
        form = forms.MyUserForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    else:
        form = forms.MyUserForm()
        users = models.MyUser.objects.all()
        return render(request, "ajax_app/base.html", {"form": form, "users": users}) 