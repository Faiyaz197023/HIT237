from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
=======
from django.contrib import admin
from .models import (
    UploadedImage,
    PestDisease,
    PlantPart,
   
    SurveySession,
)

admin.site.register(UploadedImage)
admin.site.register(PestDisease)
admin.site.register(PlantPart)

admin.site.register(SurveySession)
>>>>>>> daa7809 (ASSIGNMENT 4 STRUCTURE)
