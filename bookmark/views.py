from django.http import HttpResponse
from django.http import HttpResponse
from django.template import RequestContext, loader
from bookmark.form import BookmarkForm

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")


def popup(request):
    template = loader.get_template('popup.html')
    context = RequestContext(request, {
        'form': BookmarkForm,
    })
    return HttpResponse(template.render(context))
