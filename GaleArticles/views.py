from django.shortcuts import render
from GaleArticles.models import ArticleModel
# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def home(request):
	article_list = []
	try:
		article_list = ArticleModel.objects.getarticles()
		top = ArticleModel.objects.gettoparticle()
		relatedarticle = ArticleModel.objects.getrelatedarticles(top.articleid)
	except top.DoesNotExist:
		raise Http404("Article does not exist")
	template = loader.get_template('AllArticles.html')
	context = RequestContext(request, {
		'article_list': article_list,
		'objrelarticle':relatedarticle,
		'top':top,
	})
	return HttpResponse(template.render(context))

def articles(request , article_id):
	try:
		article = ArticleModel.objects.getarticle(article_id)
		relatedarticle = ArticleModel.objects.getrelatedarticles(article_id)
	except article.model.DoesNotExist:
		raise Http404("Article does not exist")
	template = loader.get_template('ArticleDetails.html')
	context = RequestContext(request, {
		'article': article, 
		'objrelarticle':relatedarticle,
	})
	return HttpResponse(template.render(context))


