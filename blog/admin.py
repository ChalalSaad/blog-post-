from django.contrib import admin
# import my table her 
from .models import Post,creator,Comment, publication

# Register your models here.
admin.site.register(Post)
admin.site.register(creator)
admin.site.register(Comment)
admin.site.register(publication)


 
