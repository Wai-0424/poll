from django.shortcuts import render,render_to_response
from django.views.generic import ListView,DetailView
from .models import *

def poll_list(req):
    polls = poll.objects.all()
    return render_to_response('poll_list.html',{'polls':polls})


class PollList(ListView):
    model = poll
class PollDetail(DetailView):
    model = poll