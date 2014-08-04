from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from django.http import Http404
from django.views import generic
from ipmi.models import ipmi

def IndexView(request):
	ipmi_info = ipmi.objects.all()
	template = loader.get_template('ipmi/index.html')
	#output = ', '.join([p.serv_name for p in ipmi_info])
	context = RequestContext(request, {
        'ipmi_info': ipmi_info,
    })
	#return render(request, 'ipmi/index.html', output)
	#return HttpResponse(output)
	return HttpResponse(template.render(context))