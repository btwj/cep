from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from my_social_network.models import User, UserLink

def index(request):
    users = User.objects.all();
    return render_to_response('my_social_network/users.html',
                              context_instance = RequestContext(request, {'users': users}))

def followers(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404
    userlinks = UserLink.objects.filter(to_user=user)
    return render_to_response('my_social_network/followers.html',
                              context_instance = RequestContext(request, {'main_user': user,
                                                                          'userlinks': userlinks}))

def following(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404
    userlinks = UserLink.objects.filter(from_user=user)
    return render_to_response('my_social_network/following.html',
                              context_instance = RequestContext(request, {'main_user': user,
                                                                          'userlinks': userlinks}))
