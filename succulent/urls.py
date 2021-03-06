from django.conf.urls import patterns, include, url


from bookmark import views


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'succulent.views.home', name='home'),
    # url(r'^succulent/', include('succulent.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^$', views.index, name='index'),
     url(r'^tag/$',views.tag, name='tag'),
     url(r'^tag/(?P<tag>(.*))/$',views.tag, name='tag'),
     url(r'^tag/(?P<tag>(.*))/(?P<user>\d+)/$',views.tag, name='tag'),
     url(r'^popup/', views.popup, name='popup'),
     url(r'^login/', views.loginu, name='loginu'),
     url(r'^close/', views.close, name='close'),
)

