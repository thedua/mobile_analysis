from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator

import requests, json
import numpy as np
import time


from .models import Mobile, MobileReviews
from .utils import train_data


class TrainMobile(View):
    def get(self, request):
        context = {}
        mobiles = Mobile.objects.all
        context = {'mobiles':mobiles}
        return render(request, 'project/train.html', context)

class TrainReviewView(View):
    def get(self, request, mobile):
        context = {}
        mobile = get_object_or_404(Mobile, slug=mobile)
        reviews =  get_list_or_404(MobileReviews.objects.values_list('review', flat=True), mobile=mobile)
        data =  get_list_or_404(MobileReviews, mobile=mobile)

        result = train_data(reviews)

        for i in range(0,len(reviews)):
            data[i].rating =  result[i]
            super(MobileReviews, data[i]).save()

        context = {'mobile':mobile}
        return render(request, 'project/complete.html', context)
