from django.contrib import admin
from .models import SubmitDoc, Article, Categorie, Profile

# Register your models here.
admin.site.register(SubmitDoc)
admin.site.register(Article)
admin.site.register(Categorie)
admin.site.register(Profile)