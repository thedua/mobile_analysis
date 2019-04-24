from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.views import View

import json

from dashboard.models import Mobile, MobileReviews
from dashboard.utils import total_trained_data
from .fonAPI import FonApi

fon = FonApi('31483eeecdbe6a708eeae0cd3c3edb76920e3442e7a611fb')

class IndexView(View):

    def get(self, request):
        context = {}
        mobiles_count = Mobile.objects.count
        mobiles = Mobile.objects.all
        reviews_count = MobileReviews.objects.count
        train_count = total_trained_data()
        context = {
            'mobiles_count':mobiles_count,
            'mobiles':mobiles,
            'reviews_count':reviews_count,
            'train_count':train_count,
        }
        return render(request, 'project/index.html', context)


class AnalysisMobileReview(View):

    def get(self, request, mobile=None):
        context = {}

        if mobile:
            mobile = get_object_or_404(Mobile, slug=mobile)
            context['mobile'] = mobile
            device = mobile.name
            phone = fon.getdevice(device)[0]
            context['phone'] = phone
            print(phone)

            return render(request, 'project/analysis.html', context)

        mobiles = Mobile.objects.all
        context['mobiles'] = mobiles
        return render(request, 'project/mobiles.html', context)

    def post(self, request):
        context = {}
        return redirect('project:analysis', request.POST['mobile'])

class GetMobileData(View):

    def post(self, request):
        mobile = get_object_or_404(Mobile, slug=request.POST['slug'])
        reviews = get_list_or_404(MobileReviews.objects.values_list('rating', flat=True), mobile=mobile)

        high = reviews.count(5)
        average = reviews.count(2)+reviews.count(3)+reviews.count(4)
        low = reviews.count(1)
        total = high + average + low

        dict = {}
        dict['low'] = {'y' : int((low/total)*100), 'name' : 'Low'}
        dict['average'] = {'y' : int((average/total)*100), 'name' : 'Average'}
        dict['high'] = {'y' : int((high/total)*100), 'name' : 'High'}

        return HttpResponse(json.dumps(dict), content_type="application/json")

class GetMobileCameraData(View):

    def post(self, request):
        mobile = get_object_or_404(Mobile, slug=request.POST['slug'])
        reviews = get_list_or_404(MobileReviews.objects.filter(review__contains='camera' \
          ).values_list('rating', flat=True), mobile=mobile)

        high = reviews.count(5)
        average = reviews.count(2)+reviews.count(3)+reviews.count(4)
        low = reviews.count(1)
        total = high + average + low

        dict = {}
        dict['low'] = {'y' : int((low/total)*100), 'name' : 'Low'}
        dict['average'] = {'y' : int((average/total)*100), 'name' : 'Average'}
        dict['high'] = {'y' : int((high/total)*100), 'name' : 'High'}

        return HttpResponse(json.dumps(dict), content_type="application/json")

class GetMobileBatteryData(View):

    def post(self, request):
        mobile = get_object_or_404(Mobile, slug=request.POST['slug'])
        reviews = get_list_or_404(MobileReviews.objects.filter(review__contains='battery' \
          ).values_list('rating', flat=True), mobile=mobile)

        high = reviews.count(5)
        average = reviews.count(2)+reviews.count(3)+reviews.count(4)
        low = reviews.count(1)
        total = high + average + low

        dict = {}
        dict['low'] = {'y' : int((low/total)*100), 'name' : 'Low'}
        dict['average'] = {'y' : int((average/total)*100), 'name' : 'Average'}
        dict['high'] = {'y' : int((high/total)*100), 'name' : 'High'}

        return HttpResponse(json.dumps(dict), content_type="application/json")

class GetMobileMemoryData(View):

    def post(self, request):
        mobile = get_object_or_404(Mobile, slug=request.POST['slug'])
        reviews = get_list_or_404(MobileReviews.objects.filter(review__contains='ram' \
          ).values_list('rating', flat=True), mobile=mobile)

        high = reviews.count(5)
        average = reviews.count(2)+reviews.count(3)+reviews.count(4)
        low = reviews.count(1)
        total = high + average + low

        dict = {}
        dict['low'] = {'y' : int((low/total)*100), 'name' : 'Low'}
        dict['average'] = {'y' : int((average/total)*100), 'name' : 'Average'}
        dict['high'] = {'y' : int((high/total)*100), 'name' : 'High'}

        return HttpResponse(json.dumps(dict), content_type="application/json")
