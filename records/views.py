from django.shortcuts import render

# Create your views here.

def index(request):
   return render(request, 'records/records.html')

def studentinfo(request):
   return render(request, 'records/studentinfo.html')
    
def search(request):
   return render(request, 'records/search.html')
