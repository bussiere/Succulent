from django.contrib import admin
from bookmark.models import Bookmark
from bookmark.models import Url
from bookmark.models import Tag
from bookmark.models import Image
from bookmark.models import Description


admin.site.register(Bookmark)
admin.site.register(Url)
admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Description)