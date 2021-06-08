from django.shortcuts import render

# Create your views here.
def home_view(request):
	hello = 'This is after all troubleshooting done!'
	return render(request,'sales/main.html',{'hello':hello})