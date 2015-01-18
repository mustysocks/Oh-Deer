from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
#from deermap.models import Animal

#need to rework index.html to take advantage of Django templates4
#ie. index.html would be the base template, all data display would be templates extending the base 
urlpatterns = patterns('',
	url('', TemplateView.as_view(template_name='index.html')),
	# getlayerpoints returns geojson, to be displayed on map
	#url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Animal), name='data'),
)
