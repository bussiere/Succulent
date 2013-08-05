# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from django.template import RequestContext, loader
from bookmark.form import BookmarkForm, LoginForm,SearchForm
import urllib2
from BeautifulSoup import BeautifulSoup
from Script import savebookmark, getbookmark,MiseEnPage
from django.utils.http import urlencode
from django.contrib.auth import authenticate, login
from Render import RenderLogin
from models import Bookmark,Tag



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
    request.method = None
    if request.user.is_authenticated():
        bookmarks = Bookmark.objects.filter(user = request.user)
        retour  = MiseEnPage(bookmarks)
        bookmarks = retour[0]
        tags = retour[1]
        template = loader.get_template('index.html')
        form = SearchForm(initial={'Own':True})
        context = RequestContext(request,{'bookmarks':bookmarks,'tags':tags,'form':form,'id':request.user.id})
        return HttpResponse(template.render(context).encode('utf8'))
    else :
        return  loginu(request,"main")


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

def tag(request,tag=None,user=None):
    if request.user.is_authenticated():
        print int(request.user.id)
        if request.method == 'POST' :
            form = SearchForm(request.POST)
            if form.is_valid():
                tag = form.cleaned_data['Search']
                tag = tag.lower()
                if (form.cleaned_data['Own'] == True) :
                    user == int(request.user.id)
                old = tag.replace(" ","+")
                tags = tag.split(" ")
        else :
            tag = tag.lower()
            old = tag
            if tag :
                tags = tag.split("+")
            else :
                request.method = None
                return index(request)
        tagso = []
        for t in tags :
           tagsresult = Tag.objects.filter(tag = t)
           for tg in tagsresult :
               tagso.append(tg)
               
        tags = None 
        #a optimiser
        if not tagso :
             return index(request) 
        bookmarks = Bookmark.objects.filter(user = request.user,tag = tagso[0])
        if user and int(user) == int(request.user.id) :  
            request.method = None
            for t in tagso : 
                bookmarks =  bookmarks.filter(user = request.user,tag = t)
            retour  = MiseEnPage(bookmarks)
            bookmarks = retour[0]
            tags = retour[1]
            template = loader.get_template('tag.html')
            form = SearchForm(initial={'Own':True})
            
            context = RequestContext(request,{'bookmarks':bookmarks,'tags':tags,'form':form,'id':request.user.id,'old':old,'told':old.split('+')})
            return HttpResponse(template.render(context).encode('utf8'))
        else :
            for t in tagso : 
                bookmarks =  bookmarks.filter(tag = t,private__private = False)
            retour  = MiseEnPage(bookmarks)
            bookmarks = retour[0]
            tags = retour[1]
            template = loader.get_template('taga.html')
            form = SearchForm(initial={'Own':True})
            context = RequestContext(request,{'bookmarks':bookmarks,'tags':tags,'form':form,'old':old,'told':old.split('+')})
            return HttpResponse(template.render(context).encode('utf8'))
            
    else :
        return  loginu(request,"main")


def close(request):
    template = loader.get_template('close.html')
    context = RequestContext(request,{})
    return HttpResponse(template.render(context))