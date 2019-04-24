from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'dashboard'

urlpatterns = [
	path('train/', views.TrainMobile.as_view(), name = 'train'),
	path('train/<str:mobile>', views.TrainReviewView.as_view(), name = 'train_mobile')
]
