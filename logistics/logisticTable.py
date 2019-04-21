from django_tables2 import tables, TemplateColumn
from .models import Vehicle

class logisticTable(tables.Table):
    
    edit = TemplateColumn(template_name='logistic_update_column.html')
    delete = TemplateColumn(template_name='logistic_delete_column.html')

    class Meta:
         model = Vehicle
         fields = ["vehical_type", "model_name", "model_number", "condition","edit","delete"]
         template_name = "django_tables2/bootstrap4.html"
         attrs = {"class": "table"}