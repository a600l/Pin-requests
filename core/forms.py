
from django import forms
from .models import RequestModel

class RequestForm(forms.ModelForm):
    class Meta:
        model = RequestModel
        fields = ['representative_name', 'order_id', 'pnr', 'comments', 'image_data']




class ActionTakenForm(forms.ModelForm):
    class Meta:
        model = RequestModel
        fields = ['remarks']  # Updated field name
        widgets = {
            'remarks': forms.Textarea(attrs={'rows': 4}),  # Optional: Adjust widget attributes as needed
        }
