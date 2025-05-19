from django.db import models
<<<<<<< HEAD

# Create your models here.
=======
from django.contrib.auth.models import User

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} – {self.image.name}"

class PestDisease(models.Model):
    KEY_CHOICES = [
        ("anthracnose",    "Anthracnose"),
        ("dendritic_spot", "Dendritic Spot"),
    ]
    key = models.CharField(max_length=30, choices=KEY_CHOICES, unique=True)
    def __str__(self): return dict(self.KEY_CHOICES)[self.key]

class PlantPart(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self): return self.name

class SurveySession(models.Model):
    grower           = models.ForeignKey(User, on_delete=models.CASCADE)

    # property details captured on each session
    property_name    = models.CharField(max_length=200)
    location         = models.CharField(max_length=255, help_text="Start typing address…")
    latitude         = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude        = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    area_hectares    = models.FloatField(blank=True, null=True, help_text="Optional: site area")
    stocking_rate    = models.FloatField(blank=True, null=True, help_text="Optional: plants per hectare")
    number_plants    = models.PositiveIntegerField()

    pest_disease     = models.ForeignKey(PestDisease, on_delete=models.PROTECT)
    plant_part       = models.ForeignKey(PlantPart,   on_delete=models.PROTECT)

    date_time        = models.DateTimeField()
    number_surveyed  = models.PositiveIntegerField(help_text="How many plants you inspected")
    duration_minutes = models.PositiveIntegerField(help_text="Total minutes spent")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_time"]

    @property
    def pct_inspected(self):
        return round(100 * self.number_surveyed / self.number_plants, 1) if self.number_plants else 0

    @property
    def mins_per_plant(self):
        return round(self.duration_minutes / self.number_surveyed, 2) if self.number_surveyed else 0

    def __str__(self):
        return f"{self.property_name} – {self.pest_disease} on {self.date_time:%Y-%m-%d %H:%M}"

from django.contrib.auth.models import User

class AnalyzedImage(models.Model):
    grower      = models.ForeignKey(User, on_delete=models.CASCADE)
    upload      = models.ForeignKey(UploadedImage, on_delete=models.CASCADE)
    label       = models.CharField(max_length=100)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.upload.image.name} → {self.label}"
>>>>>>> daa7809 (ASSIGNMENT 4 STRUCTURE)
