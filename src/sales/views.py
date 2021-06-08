from django.shortcuts import render
from django.views.generic import ListView
from .models import Sale
# Create your views here.
def home_view(request):
	hello = 'This is after all troubleshooting done!'
	return render(request,'sales/home.html',{'hello':hello})



# Class Based View
class SalesListView(ListView):
	model = Sale
	template_name = 'sales/main.html'
	