from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from django.template import RequestContext, loader
from bookmark.form import BookmarkForm, LoginForm
def RenderLogin(request,origin,url):
    form = LoginForm(initial={'Url': url,'Origin':origin})
    template = loader.get_template('login.html')
    context = RequestContext(request, {
            'form': form ,
        })
    return HttpResponse(template.render(context))