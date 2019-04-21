from django.forms import ModelForm,TextInput 
from django import forms 
from .models import Vehicle
  
# define the class of a form 
#from formValidationApp.models import * 
class logistiForm(ModelForm):
    class Meta: 
        # write the name of models for which the form is made 
        model = Vehicle         
  
        # Custom fields 
  
        fields =["vehical_type", "model_name", "model_number", "condition"] 
        # this function will be used for the validation 
    def clean(self): 
  
        # data from the form is fetched using super function 
        super(logistiForm, self).clean() 
          
        # extract the username and text field from the data 
        vehical_modal = self.cleaned_data.get('model_name') 
        vehical_name = self.cleaned_data.get('model_number') 
       # condition = self.cleaned_data.get('condition') 
        #Vehical_type = self.cleaned_data.get('type') 
        # conditions to be met for the username length 
        #if len(vehical_modal) < 2: 
            #self._errors['model_name'] = self.error_class([ 
                #'Minimum 2 characters required']) 
        #if len(vehical_name) <5: 
            #self._errors['model_number'] = self.error_class([ 
                #'Post Should Contain minimum 5 characters']) 
  
        # return any errors if found 
        return self.cleaned_data 