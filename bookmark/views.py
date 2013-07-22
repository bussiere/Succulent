from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from bookmark.form import BookmarkForm

def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))


def popup(request):
    if request.method == 'POST': # If the form has been submitted...
        form = BookmarkForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            print form.cleaned_data['Url']

            return HttpResponseRedirect('../close/') # Redirect after POST
    template = loader.get_template('popup.html')
    context = RequestContext(request, {
        'form': BookmarkForm(),
    })
    return HttpResponse(template.render(context))


def close(request):
    template = loader.get_template('close.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))