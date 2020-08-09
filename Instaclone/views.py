from django.shortcuts import render

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user=request.user

    photos=Image.get_photos()
    comments=Comment.get_comments()
    # profile = Profile.objects.get(user=current_user)
    profiles = Profile.objects.all()


    return render(request,'index.html',{"photos":photos,"profiles":profiles,"comments":comments})