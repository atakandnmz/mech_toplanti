from django.shortcuts import render,redirect
from .forms import ToplantiForm
from .models import Toplanti_Konusu
# Create your views here.
def toplanti_list(request):
    context = {'toplanti_list':Toplanti_Konusu.objects.all()}
    return render(request,"katilimci/toplanti_list.html",context)

def toplanti_form(request,id=0):
    if request.method=="GET":
        if id==0:
            form=ToplantiForm()
        else:
            toplanti=Toplanti_Konusu.objects.get(pk=id)
            form=ToplantiForm(instance=toplanti)
        return render(request,"katilimci/toplanti_form.html",{'form':form})
    else:
        if id==0:
            form=ToplantiForm(request.POST)  
        else:  
            toplanti=Toplanti_Konusu.objects.get(pk=id)
            form=ToplantiForm(request.POST,instance=toplanti)
    if form.is_valid():
        form.save()
    return redirect('/toplanti/list')   

def toplanti_delete(request,id):
    toplanti=Toplanti_Konusu.objects.get(pk=id)
    toplanti.delete()
    return redirect('/toplanti/list')   