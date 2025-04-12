from django.shortcuts import render
from .classes import Pest, Protect_Against_Pest, Diseases_Protection, Protect_Against_Diseases
from data.pests import pests_data
from data.pest_detail import pests_description
from data.pest_protect import pest_protect_data
from data.disease_protection import protection_data
from data.diseases import diseases_data
from data.diseases_detail import diseases_description
from data.disease_protection_detail import protection_data as protection_detail
from django.views import View

def home_view(response):
    return render(response, "main/home.html", {})

class PestsView(View):
    def get(self, request):
        pests = self.combine_pests_data()
        return render(request, "main/pests.html", {"pests": pests})

    def combine_pests_data(self):
        return [Pest.from_data(p, pests_description) for p in pests_data]

class PestDetailView(View):
    def get(self, request, key):
        pest = next((Pest.from_data(p, pests_description) for p in pests_data if p["key"] == key), None)
        if pest:
            return render(request, 'main/pest_detail.html', {"pest": pest})
        else:
            return render(request, 'pests/404.html', status=404)

class ProtectView(View):
    def get(self, request):
        query = request.GET.get('search', '').lower()
        protected_pests = self.combine_protection_data()

        if query:
            protected_pests = [
                pest for pest in protected_pests
                if query in pest.name.lower() or query in pest.scientific_name.lower()
            ]

        return render(request, "main/protect.html", {"protected_pests": protected_pests, "query": query})

    def combine_protection_data(self):
        return [
            Protect_Against_Pest.from_protect_data(pest, pests_description, pest_protect_data)
            for pest in pests_data
        ]

class ProtectDetailView(View):
    def get(self, request, key):
        protected_pest = next(
            (Protect_Against_Pest.from_protect_data(p, pests_description, pest_protect_data)
             for p in pests_data if p["key"] == key),
            None
        )
        if protected_pest:
            return render(request, "main/protect_detail.html", {"pest": protected_pest})
        else:
            return render(request, "pests/404.html", status=404)

class DiseasesView(View):
    def get(self, request):
        return render(request, 'main/diseases.html', {'diseases': diseases_data})

class DiseaseDetailView(View):
    def get(self, request, key):
        disease = next((d for d in diseases_description if d["key"] == key), None)
        return render(request, 'main/diseases_detail.html', {'disease': disease})

class DiseaseProtectionView(View):
    def get(self, request):
        query = request.GET.get('search', '').lower()
        protections = [
            Diseases_Protection.from_data(d, diseases_description, protection_detail)
            for d in diseases_data
        ]

        if query:
            protections = [
                d for d in protections
                if query in d.name.lower() or query in d.scientific_name.lower()
            ]

        return render(request, 'main/disease_protection.html', {'protections': protections, 'query': query})


class DiseaseProtectDetailView(View):
    def get(self, request, key):
        disease_data = next((d for d in diseases_data if d['key'] == key), None)
        if disease_data:
            disease_protection = Protect_Against_Diseases.from_disease_prot_data(
                disease_data, diseases_description, protection_detail
            )
            return render(request, 'main/disease_protection_detail.html', {'disease': disease_protection})
        else:
            return render(request, 'pests/404.html', status=404)

def about_us(request):
    return render(request, 'main/aboutus.html')
