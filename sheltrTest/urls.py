from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sheltrTest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/$', include('app.urls'))
    url(r'^contact/$', 'views.contact', name='contact'),
    url(r'^thanks/$', 'views.thanks', name='thanks'),
)
