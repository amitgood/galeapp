from django.contrib import admin

# Register your models here.
from .models import ArticleModel, ArticleContent, Author, ArticleImage, RelatedArticle

admin.site.register(ArticleModel)
admin.site.register(ArticleContent)
admin.site.register(Author)
admin.site.register(ArticleImage)
admin.site.register(RelatedArticle)

