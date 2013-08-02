from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from django.template import RequestContext, loader
from bookmark.form import BookmarkForm, LoginForm
import urllib2
from BeautifulSoup import BeautifulSoup
from Script import savebookmark, getbookmark
from django.utils.http import urlencode
from django.contrib.auth import authenticate, login
from Render import RenderLogin




def loginu(request,origin=None,url=None):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid(): 
            username = form.cleaned_data['Name']
            password = form.cleaned_data['Password']
            origin = form.cleaned_data['Origin']
            url = form.cleaned_data['Url']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if origin == "main" :
                        return index(request)
                    elif origin == "popup" :
                        return popup(request,url=url,origin="login")
                else :
                    return RenderLogin(request,origin,url)
            else :
                return RenderLogin(request,origin,url)  
        else :
            return RenderLogin(request,origin,url)  
    else :
        return RenderLogin(request,origin,url)
        


def index(request):
    if request.user.is_authenticated():
        template = loader.get_template('index.html')
        context = RequestContext(request,{})
        return HttpResponse(template.render(context))
    else :
        loginu(request,"origin")


def popup(request,count=0,url=None,origin=None):
    if not url :
            try : 
                url = request.META['HTTP_REFERER']
            except :
                url = request.GET['url']
                url = urlencode.decode(url)  
    else :
        pass 
    if request.user.is_authenticated():
        title = ""
        tag = getbookmark(url,request.user)
        if request.method == 'POST' and not origin: # If the form has been submitted...
            form = BookmarkForm(request.POST) # A form bound to the POST data
            if form.is_valid(): # All validation rules pass
                savebookmark(form.cleaned_data['Title'],form.cleaned_data['Url'],form.cleaned_data['Description'],form.cleaned_data['Tag'],form.cleaned_data['Private'],request.user)
                return HttpResponseRedirect('../close/') # Redirect after POST
        print url
        if count < 3 :
            try :
                soup = BeautifulSoup(urllib2.urlopen(url))
                title = soup.title.string
            except :
                popup(request,count+1)
        form = BookmarkForm(initial={'Url': url,'Title':title,'Tag':tag})
        template = loader.get_template('popup.html')
        context = RequestContext(request, {
            'form': form ,
        })
        return HttpResponse(template.render(context))
    else :
        return loginu(request,"popup",url)

def tag(request):
    pass

def close(request):
    template = loader.get_template('close.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))