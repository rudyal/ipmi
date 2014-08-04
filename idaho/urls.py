from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from ipmi import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ipmi.views.IndexView', name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
) 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
