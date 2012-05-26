from django.conf.urls.defaults import patterns, include, url
from mozaictodo.api import TodoItemResource
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

todo_resource = TodoItemResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mozaiclogger.views.home', name='home'),
    # url(r'^mozaiclogger/', include('mozaiclogger.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(todo_resource.urls)),
)
