from django.shortcuts import render
from create.models import *

from datetime import datetime, timezone

# Create your views here.
def visit(request):
    return render(request, "./visit/visitlink.html")

def add(request):
    return render(request, "./visit/add.html")

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
    
    return render(request, "./visit/done.html",data)

