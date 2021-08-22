from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Occasion,Step2,Step3,message1,message2,prompt1,prompt2
from accounts.models import Profile
from .forms import Update,Message1,Message2
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from datetime import datetime, timezone


# Create your views here.
def index(request):
    return render(request, "./create/index.html")
@login_required
def one(request):
    return render(request, "./create/one.html")
@login_required
def two(request):
    if request.method == "POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        
        coverpic=request.FILES['coverpic']
        
        
        date=request.POST.get('date')
        step2=Step2(user=request.user,firstname=firstname,lastname=lastname,cover_pic=coverpic,dead_line=date)
        step2.save()
        print(coverpic)
        return redirect('three')
    else:
        return render(request,"./create/two.html")

    return render(request, "./create/two.html")


def three(request):
    step2=Step2.objects.last()
    print(step2)
    if request.user.is_authenticated:

        if request.method == "POST":
            first=request.POST.get('first')
            second=request.POST.get('second')
            third=request.POST.get('third')
            print(first)
            data=Step3(user=request.user,first=first,second=second,third=third)
            data.save()
            return redirect('final')

    else:
        return redirect('/')   
        
    return render(request, "./create/three.html",{'step2':step2})
@login_required
def final(request):
    step2=Step2.objects.last()
    step3=Step3.objects.last()
    occasion=Occasion.objects.last()
    print(step2)
    print(step3)
    print(occasion)
    s_link='http://127.0.0.1:8000/create/link/'
    data={'step2':step2,'step3':step3,'occasion':occasion,'s_link':s_link}
    return render(request, "./create/final.html",data)

def viewbook(request):
    return render(request, "./create/viewbook.html")
@login_required
def steps(request):
    if request.method == "POST":
        print(Profile)
        data=request.POST.get('hb')
        print(data)
        occ=Occasion(user=request.user,event=data)
        occ.save()
        return redirect('two')
    return render(request, "./create/steps.html")
@login_required
def steps_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("steps"))
    else:
        name = request.POST.get('name')
        deadline = request.POST.get('deadline')
        occasion = request.POST.get('occasion')
        try:
            steps_form = StepsModel(name=name,deadline=deadline,occasion=occasion)
            steps_form.save() 
            messeges.success(request, 'Great, lets start!')
            return HttpResponseRedirect('/final')
        except:
            messages.error(request, 'Sorry, there has been an error.')
            return HttpResponseRedirect('/steps')
@login_required
def after_final(request):
    step2=Step2.objects.last()
    step3=Step3.objects.last()
    occasion=Occasion.objects.last()
    time=datetime.now(timezone.utc)
    print(time)
    print(step2.dead_line)
    time_left=step2.dead_line-time
    print(occasion.event)
    s_link='http://127.0.0.1:8000/create/link/'
    
    data={'step2':step2,'step3':step3,'occasion':occasion,'timeleft':time_left,'s_link':s_link}
    return render(request, "./create/afterfinal.html",data)
    
@login_required
def delete(request):
    try:

        step2=Step2.objects.last()
        step3=Step3.objects.last()
        occasion=Occasion.objects.last()
    
        step2.delete()
        step3.delete()
        occasion.delete()
        return render(request,'./create/steps.html',{'msg':'Do you want delete this page ?'})

    
    except:
        return redirect('steps')
  
def messageone(request):
    step2=Step2.objects.last()
    
    if request.method=='POST':
       
        fm=Message1(request.POST)
        if fm.is_valid():
            msg=fm.cleaned_data['msg']
            obj=message1(msg=msg,user=request.user)
                
            obj.save()
            fm=Message1()
    else:
        fm=Message1()          
    message=message1.objects.last()
    return render(request,'./create/update.html',{'fm':fm,'step2':step2,'message':message})



def messagetwo(request):
    step2=Step2.objects.last()
    
    if request.method=='POST':
       
        fm=Message2(request.POST)
        if fm.is_valid():
            msg=fm.cleaned_data['msg']
            obj=message2(msg=msg)
                
            obj.save()
            fm=Message2()
        return redirect('done')
    else:
        fm=Message2()          
    message=message2.objects.last()
    return render(request,'./create/update1.html',{'fm':fm,'step2':step2,'message':message})


def s_link(request,str,id):
    
    step2=Step2.objects.last()
    step3=Step3.objects.last()
    occasion=Occasion.objects.last()
    count=message1.objects.filter(user=request.user).count()
    print(count)
    time=datetime.now(timezone.utc)
    print(step2.dead_line)
    
    print(time)
    print(step2.dead_line)
    time_left=step2.dead_line-time
    print(occasion.event)
    s_link="http://127.0.0.1:8000/create/link/"
    
    data={'count':count,'step2':step2,'step3':step3,'occasion':occasion,'timeleft':time_left,'s_link':s_link}
    return render(request, "./create/s_link.html",data)

def done(request):
    step2=Step2.objects.last()
    step3=Step3.objects.last()
    occasion=Occasion.objects.last()
    print(step3)
    msg1=message1.objects.last()
    msg2=message2.objects.last()
    time=datetime.now(timezone.utc)
    time_left=step2.dead_line-time
    s_link="http://127.0.0.1:8000/create/link/"
    data={'s_link':s_link,'step2':step2,'step3':step3,'occasion':occasion,'msg1':msg1,'msg2':msg2,'timeleft':time_left}
    return render(request, "./create/done.html",data)




