from django.forms import forms
from django.shortcuts import render
from django.views.generic.edit import FormView
from task2.forms import ReviewForm
from django.http import HttpResponse



class ReviewEmailView(FormView):
    template_name = 'review.html'
    form_class = ReviewForm

    def form_valid(self, form):
        form.send_email()
        msg = "Thanks For The Review"
        return HttpResponse(msg)

