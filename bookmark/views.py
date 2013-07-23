from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from django.template import RequestContext, loader
from bookmark.form import BookmarkForm
import urllib2
from BeautifulSoup import BeautifulSoup


def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))


def popup(request):
    try : 
        url = request.META['HTTP_REFERER']
    except :
        url = request.GET['url']
    soup = BeautifulSoup(urllib2.urlopen(url))
    title = soup.title.string
    if request.method == 'POST': # If the form has been submitted...
        form = BookmarkForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            print form.cleaned_data['Url']

            return HttpResponseRedirect('../close/') # Redirect after POST
    form = BookmarkForm(initial={'Url': url,'Title':title})
    template = loader.get_template('popup.html')
    context = RequestContext(request, {
        'form': form ,
    })
    return HttpResponse(template.render(context))


def close(request):
    template = loader.get_template('close.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))