from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.

def index(request):
    
    return render(request, 'all-awards/index.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    project = Project.objects.filter(user_id=current_user.id)

    return render(request,"profile.html",{'profile':profile})

