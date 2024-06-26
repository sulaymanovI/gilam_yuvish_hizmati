from django.shortcuts import render
from .forms import BuyurtmaForm

def buyurtma_olish(request):
    if request.method=='POST':
        form=BuyurtmaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form=BuyurtmaForm()
    return render(request , 'index.html',{'form':form})
    
