from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from django.template import RequestContext, loader
from bookmark.form import BookmarkForm
import urllib2
from BeautifulSoup import BeautifulSoup
from Script import savebookmark, getbookmark
from django.utils.http import urlencode



def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))


def popup(request,count=0):
    title = ""
    try : 
        url = request.META['HTTP_REFERER']
    except :
        url = request.GET['url']
        url = urlencode.decode(url)

    tag = getbookmark(url)
    if request.method == 'POST': # If the form has been submitted...
        form = BookmarkForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            savebookmark(form.cleaned_data['Title'],form.cleaned_data['Url'],form.cleaned_data['Description'],form.cleaned_data['Tag'],form.cleaned_data['Private'])
            return HttpResponseRedirect('../close/') # Redirect after POST
    print url
    if count < 3 :
        try :
            soup = BeautifulSoup(urllib2.urlopen(url))
            title = soup.title.string
        except :
            popup(request,count+1)
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