from django.shortcuts import render
from .models import Language

# Create your views here.
def home(request):
	languages = Language.objects.all()
	return render(request,'index.html',{"languages":languages})
