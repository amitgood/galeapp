from django.db import models
from django.contrib.auth.models import User

class ArticleManager(models.Manager):

  def getarticles(self):
    article_list = []
    articlesobj = ArticleModel.objects.all()
    for article in articlesobj:
      article.authorname = ArticleModel.objects.getarticleauthor(article.articleid)
      article_list.append(article)
    return article_list

  def getarticle(self, artid):
    article = ArticleModel.objects.get(articleid = artid)
    article.authorname = ArticleModel.objects.getarticleauthor(artid)
    article.content = ArticleModel.objects.getarticlecontent(artid)
    article.image = ArticleModel.objects.getarticleimages(artid)
    return article

  def getarticlescount(self):
    return self.count()

  def gettoparticle(self):
    toplist = ArticleModel.objects.order_by('-rank')
    top = ArticleModel.objects.getarticle(toplist[0].articleid)
    top.authorname = ArticleModel.objects.getarticleauthor(toplist[0].articleid)
    top.content = ArticleModel.objects.getarticlecontent(top.articleid)
    top.mainimage = ArticleModel.objects.getarticleimages(top.articleid)[1].artcicleimage
    return top

  def getrelatedarticles(self, artid):
    related =[]
    related = RelatedArticle.objects.filter(articleid = artid)
    return related

  def getarticlecontent(self, artid):
    content = ArticleContent.objects.filter(articleid = artid)
    return content.get().articlecontentpath

  def getarticleauthor(self, artid):
    article = ArticleModel.objects.filter(articleid = artid)
    authobj = Author.objects.filter(authorid = article.get().authorid.authorid)
    return authobj.get().authorname

  def getarticleimages(self, artid):
    images =[]
    images = ArticleImage.objects.filter(articleid = artid)
    return images

class Author(models.Model):
  authorid =   models.AutoField(primary_key=True)
  authorname = models.CharField(max_length=100)

  def __unicode__(self):
    return self.authorname

# Create your models here.
class ArticleModel(models.Model):
  articleid = models.AutoField(primary_key=True)
  category = models.CharField(max_length=100)
  rank =   models.IntegerField()
  articlename = models.CharField(max_length=100)
  authorid = models.ForeignKey(Author, related_name="article_authorid")
  lastupdated = models.DateTimeField(auto_now =True)
  shortdescription =  models.CharField(max_length=200)
  objects = ArticleManager()
 
  def __unicode__(self):
    return self.articlename

class ArticleContent(models.Model):
  articleid =      models.ForeignKey(ArticleModel, related_name="ArticleContent_articleid")
  articlecontentpath = models.CharField(max_length=100)
  def __unicode__(self):
    return self.articlecontentpath

class ArticleImage(models.Model):
  articleid =      models.ForeignKey(ArticleModel, related_name="ArticleImage_articleid")
  artcicleimage = models.CharField(max_length=100)
  imagetype = models.CharField(max_length=100)
  def __unicode__(self):
    return self.artcicleimage

class RelatedArticle(models.Model):
  articleid =      models.ForeignKey(ArticleModel, related_name="RelatedArticle_articleid")
  rel_artcile_id = models.ForeignKey(ArticleModel, related_name="RelatedArticle_articleid_1")
  category = models.ForeignKey(ArticleModel, related_name="relate_category")

