from django.shortcuts import render,HttpResponseRedirect
from .forms import studentregisteration
from.models import user
# Create your views here.
def add_show(request):
    if request.method =='POST':
        fm=studentregisteration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            ps=fm.cleaned_data['password']
            reg=user(name=nm,email=em,password=ps)
            reg.save()
            fm=studentregisteration()
    else:
        fm=studentregisteration()
    stud=user.objects.all()
        
    return render(request, 'enroll/addandshow.html',{'form':fm,'stu':stud})

# for delete function

def delete_data(request,id):
    if request.method =='post':
        pi=user.objects.get(pk=id)            #pk=primary
        pi.delete()
        return HttpResponseRedirect('/')