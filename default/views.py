from django.shortcuts import render,render_to_response
from django.views.generic import ListView,DetailView, RedirectView, CreateView, UpdateView
from .models import *
from django.urls import reverse

def poll_list(req):
    polls = poll.objects.all()
    return render_to_response('poll_list.html',{'polls':polls})


class PollList(ListView):
    model = poll
class PollDetail(DetailView):
    model = poll

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['cbe'] = Option.objects.filter(poll_id=self.kwargs['pk'])
        return ctx

class PollVote(RedirectView):
    def get_redirect_url(self, **kwargs):
        opt = Option.objects.get(id=self.kwargs['oid'])
        opt.count += 1
        opt.save()
        return "/poll/{}/".format(opt.poll_id)

class PollCreate(CreateView):
    model = poll
    fields = ['subject']
    success_url = '/poll/'
class PollUpdate(UpdateView):
    model = poll
    fields = ['subject']
    success_url = '/poll/'
class OptionCreate(CreateView):
    model = Option
    fields = ['title']
    template_name = 'default/poll_form.html'
    
    def get_success_url(self):
        #return '/poll/' + int(self.kwarges['zzz']) + '/'
        #return '/poll/{}/'.format(self.kwargs['zzz'])
        #return reverse('poll_view', kwargs={'pk': self.kwargs['zzz']})
        return reverse('poll_view', args=[self.kwargs['zzz']])

    def form_valid(self, form):
        form.instance.poll_id = self.kwargs['zzz']
        return super().form_valid(form)

class OptionEdit(UpdateView):
    modle = Option
    fields = ['title']
    template_name = 'default/poll_form.html'

    def get_success_url(self):
        return reverse('poll_view',args=[self.object.poll_id])