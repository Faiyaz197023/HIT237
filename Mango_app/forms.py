from django import forms
from .models import UploadedImage, SurveySession, PestDisease, PlantPart

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']

class SurveySessionForm(forms.ModelForm):
    class Meta:
        model  = SurveySession
        fields = [
          'property_name', 'location', 'latitude', 'longitude',
          'area_hectares', 'stocking_rate', 'number_plants',
          'pest_disease','plant_part',
          'date_time','number_surveyed','duration_minutes'
        ]
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'latitude':  forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'number_plants': forms.NumberInput(attrs={'min':1}),
            'area_hectares': forms.NumberInput(attrs={'step':0.1}),
            'stocking_rate': forms.NumberInput(attrs={'step':0.1}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['pest_disease'].queryset = PestDisease.objects.all()
        self.fields['plant_part'].queryset   = PlantPart.objects.all()
        # require at least one field
        self.fields['property_name'].label = "Site Name"
        self.fields['location'].label      = "Site Address"