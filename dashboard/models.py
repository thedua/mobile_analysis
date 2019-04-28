from django.db import models
from django.shortcuts import get_object_or_404, get_list_or_404
from django.utils.text import slugify

import os
import pandas as pd
from textblob import TextBlob
from unidecode import unidecode

from .utils import get_clean_text
from analysis.settings import BASE_DIR

class Mobile(models.Model):
    COMPANY_NAME = (
        ('Xiaomi', 'Xiaomi'),
        ('Samsumg', 'Samsumg'),
	('Asus', 'Asus'),
	('Honor', 'Honor'),
	('Moto', 'Moto'),
	('Nokia', 'Nokia'),
	('Realme',  'Realme'),
	('Oneplus', 'Oneplus'),
	('LG','LG'),
	('Oppo','Oppo'),
	('Huawei','Huawei'),


    )

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, blank=True)
    company = models.CharField(max_length=30, choices=COMPANY_NAME, default=None)
    image = models.ImageField(upload_to='mobiles/', null=True)

    def save(self):
        self.slug = slugify(self.name)
        super().save()

    def __str__(self):
        return self.name

class MobileData(models.Model):
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE)
    datafile = models.FileField()

    def save(self):
        for field in self._meta.fields:
            if field.name == 'datafile':
                field.upload_to = 'Mobile Data/'+self.mobile.name + '/'
        super(MobileData, self).save()

    def delete(self):
        self.datafile.delete(False)
        super(MobileData, self).delete()

    def __str__(self):
        return self.mobile.name

class MobileReviews(models.Model):
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE)
    review = models.TextField(blank=True)
    rating = models.IntegerField(default=0)
    sentiment = models.DecimalField(default=0.00, max_digits=6, decimal_places=3)

    def save(self):
        mobile_data = get_list_or_404(MobileData, mobile=self.mobile.id)
        for data in mobile_data:
            path = data.datafile
            dataset = pd.read_excel(os.path.join(BASE_DIR, 'media', str(path)))
            reviews = dataset.loc[:, 'Content'].tolist()
            for review in reviews:
                text = get_clean_text(review)
                if text:
                    tweet = unidecode(str(review))
                    analysis = TextBlob(tweet)
                    self.sentiment = analysis.sentiment.polarity

                    self.review = text
                    super(MobileReviews, self).save()
                    self.pk = None

    def __str__(self):
        return (self.review[:20] + '..') if len(self.review) > 20 else self.review
