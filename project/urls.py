from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'project'

urlpatterns = [
	path('', views.IndexView.as_view(), name = 'index'),
	path('sentiment-analysis/', views.AnalysisMobileReview.as_view(), name = 'mobile_list'),
	path('sentiment-analysis/<str:mobile>/', views.AnalysisMobileReview.as_view(), name = 'analysis'),
	path('getMobileData/', views.GetMobileData.as_view(), name = 'getMobileData'),
	path('getMobileCameraData/', views.GetMobileCameraData.as_view(), name = 'getMobileCameraData'),
	path('getMobileBatteryData/', views.GetMobileBatteryData.as_view(), name = 'getMobileBatteryData'),
	path('getMobileMemoryData/', views.GetMobileMemoryData.as_view(), name = 'getMobileMemoryData'),
]
