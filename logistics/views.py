from django.shortcuts import render,redirect,get_object_or_404
from django.conf import settings
from django import forms
from django_tables2 import RequestConfig
from .logisticForm import logistiForm
from .models import Vehicle
from .logisticTable import logisticTable

# Create your views here.
def logistic_reg(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table=logisticTable(Vehicle.objects.all())
    RequestConfig(request).configure(table)
    # check if the request is post       
    if request.method =='POST':   
  
        # Pass the form data to the form class 
        details = logistiForm(request.POST) 
  
        # In the 'form' class the clean function  
        # is defined, if all the data is correct  
        # as per the clean function, it returns true 
        if details.is_valid():   
  
            # Temporarily make an object to be add some 
            # logic into the data if there is such a need 
            # before writing to the database    
            post = details.save(commit = False) 
  
            # Finally write the changes into database 
            post.save()   
  
            # redirect it to some another page indicating data 
            # was inserted successfully 
            return redirect("logistic") 
              
        else: 
          
            # Redirect back to the same page if the data 
            # was invalid 
            return render(request, "logisctics_form.html", {'form':details,'table':table})   
    else: 
  
        # If the request is a GET request then, 
        # create an empty form object and  
        # render it into the page 
        form = logistiForm(None)    
        return render(request, 'logisctics_form.html', {'form':form,'table':table}) 


# Create your views here.
def logistic_update(request,pk):
    table=logisticTable(Vehicle.objects.all())
    RequestConfig(request).configure(table)
    form_data = get_object_or_404(Vehicle, id=pk)
    form = logistiForm(request.POST or None, instance=form_data)  
    if request.method =='POST':   
        details = logistiForm(request.POST) 
        if form.is_valid():      
            post = form.save(commit = False) 
            post.save()    
            return redirect("logistic") 
              
        else:
            return render(request, "logisctics_form.html", {'form':form,'table':table})   
    else:    
        return render(request, 'logisctics_form.html', {'form':form,'table':table}) 

# def logistic_update(request, pk):
#     form_data = get_object_or_404(Vehicle, id=pk) 
#     table=logisticTable(Vehicle.objects.all())
#     RequestConfig(request).configure(table)
#     form = logistiForm(request.POST, instance=form_data)
#     return render(request, "logisctics_form.html", {'form': form}) 

def logistic_delete(request, pk):
    Vehicle.objects.filter(id=pk).delete()
    return redirect("logistic") 