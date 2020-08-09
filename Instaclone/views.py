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

def imagedetails(request,image_id):
    comments=Comment.objects.filter(image_id=image_id)


    try:
        image = Image.objects.get(id=image_id)
    except ObjectDoesNotExist:
         raise Http404()
    return render(request,"image.html",{"image":image,"comments":comments})

def profiledetails(request,profile_id):
    try:
        profile = Profile.objects.get(id=profile_id)
    except ObjectDoesNotExist:
        message = "You haven't searched for any term"


    return render(request,"profiledetails.html",{"profile":profile})

def new_image(request):
    current_user=request.user
    if request.method == 'POST':
        form =NewImageForm(request.POST,request.FILES)
        if form.is_valid():
            image=form.save(commit=False)
            image.profile = current_user
            image.save()
        return redirect('index')
    else:
        form=NewImageForm()
    return render(request,'new_image.html',{"form":form})

def new_comment(request):
    current_user=request.user
    if request.method == 'POST':
        form =NewCommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment=form.save(commit=False)

            comment.commenter = current_user

            comment.save()
        return redirect('index')
    else:
        form=NewCommentForm()
    return render(request,'new_comment.html',{"form":form})


