from django.shortcuts import render
from GaleArticles.models import ArticleModel
# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def home(request):
	try:
		article_list = ArticleModel.objects.all()
		relatedarticle = ArticleModel.objects.get(id=1).relatedid.split(',')
		objrelarticle = []
		for artno in relatedarticle:
			objrelarticle.append(ArticleModel.objects.get(articleid=artno))

	except article_list.DoesNotExist:
		raise Http404("Article does not exist")
	template = loader.get_template('AllArticles.html')
	context = RequestContext(request, {
		'article_list': article_list,
		'objrelarticle':objrelarticle,
	})
	return HttpResponse(template.render(context))

def articles(request , article_id):
	try:
		article = ArticleModel.objects.get(articleid=article_id)
		relatedarticle = article.relatedid.split(',')
		objrelarticle = []
		for artno in relatedarticle:
			objrelarticle.append(ArticleModel.objects.get(articleid=artno))

	except article.DoesNotExist:
		raise Http404("Article does not exist")
	template = loader.get_template('ArticleDetails.html')
	context = RequestContext(request, {
		'article': article, 
		'objrelarticle':objrelarticle,
	})
	return HttpResponse(template.render(context))


