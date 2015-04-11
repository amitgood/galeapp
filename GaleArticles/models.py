from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ArticleModel(models.Model):
  articleid = models.CharField(max_length=100)
  category = models.CharField(max_length=100)
  rank =   models.IntegerField
  relatedid = models.CharField(max_length=300)
  articlename = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  lastupdated = models.DateTimeField(auto_now =True)
  mainImage =  models.CharField(max_length=100)
  contentImage1 =   models.CharField(max_length=100)
  contentImage2 =   models.CharField(max_length=100)
  contentImage3 =   models.CharField(max_length=100)
  shortdescription =  models.CharField(max_length=200)
  content =  models.CharField(max_length=6000)

 