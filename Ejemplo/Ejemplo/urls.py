from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from entries.views import EntryCreateView,EntryDetailView,EntryListView,EntryUpdateView,EntryDeleteView

admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Ejemplo.views.home', name='home'),
    # url(r'^Ejemplo/', include('Ejemplo.foo.urls')),

    url(r'^create/$',EntryCreateView.as_view(),name='entry_create'),
    url(r'^(?P<slug>[-\w]+)$',EntryDetailView.as_view(),name='entry_detail'),
    url(r'^update/(?P<slug>[-\w]+)$',EntryUpdateView.as_view(),name='entry_update'),
    url(r'^delete/(?P<slug>[-\w]+)$',EntryDeleteView.as_view(),name='entry_delete'),
    url(r'^$',EntryListView.as_view(),name='entry_list'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
