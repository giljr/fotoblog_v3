from django.contrib import admin

from blog.models import BlogContributor, Photo, Blog

admin.site.register(Photo)
admin.site.register(Blog)
admin.site.register(BlogContributor)
