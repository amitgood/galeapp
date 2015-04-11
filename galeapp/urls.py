from django.conf.urls import patterns, include, url
from django.contrib import admin
from GaleArticles import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'galeapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	# url(r'^home$', 'GaleArticles.views.home'),
	# url(r'^articles', 'views.articles'),

    url(r'^articles$', views.home, name='Article List'),
    # ex: /polls/5/
    url(r'^articles/(?P<article_id>\d+)/$', views.articles, name='article details')
]
