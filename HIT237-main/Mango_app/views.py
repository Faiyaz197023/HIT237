from django.shortcuts import render
from .classes import Pest,Protect_Against_Pest
from data.pests import pests_data
from data.pest_detail import pests_description
from django.views import View
from data.pest_protect import pest_protect_data
from data.diseases import diseases_data
from data.diseases_detail import diseases_description
from .classes import Disease

def home_view(response):
    """
    Take in a request (Django sends request)
    Return HTML as a response(We pick to return the response)
    """
    return render(response, "main/home.html", {})




""" 
def combine_pests_data():
    pests = []
    for pest in pests_data:
        pests.append(Pest.from_data(pest, pests_description))
    return pests

def pests(request):
    pests = combine_pests_data()  
    return render(request, "main/pests.html", {"pests": pests})

def pest_detail(request, key):
    pest = None  
    for p in pests_data:
        if p["key"] == key:  
            pest = Pest.from_data(p, pests_description) 
            break  

    if pest:
        return render(request, 'main/pest_detail.html', {"pest": pest})
    else:
        return render(request, 'pests/404.html', status=404)  

 """


class PestsView(View):
    def get(self, request): #get is from django's framework itself we don't need any constructer 
        pests = self.combine_pests_data()
        return render(request, "main/pests.html", {"pests": pests})

    def combine_pests_data(self):
        return [Pest.from_data(p, pests_description) for p in pests_data]

class PestDetailView(View):
    def get(self, request, key):
        pest = None
        for p in pests_data:
            if p["key"] == key:
                pest = Pest.from_data(p, pests_description)
                break

        if pest:
            return render(request, 'main/pest_detail.html', {"pest": pest})
        else:
            return render(request, 'pests/404.html', status=404)
        
class ProtectDetailView(View):
    def get(self, request, key):
        protected_pest = None
        for p in pests_data:
            if p["key"] == key:
                protected_pest = Protect_Against_Pest.from_protect_data(p, pests_description, pest_protect_data)
                break

        if protected_pest:
            return render(request, "main/protect_detail.html", {"pest": protected_pest})
        else:
            return render(request, "pests/404.html", status=404)
        

class ProtectView(View):
    def get(self, request):
        protected_pests = self.combine_protection_data()
        return render(request, "main/protect.html", {"protected_pests": protected_pests})

    def combine_protection_data(self):
        return [
            Protect_Against_Pest.from_protect_data(pest, pests_description, pest_protect_data)
            for pest in pests_data
        ]

class DiseasesView(View):
    def get(self, request):
        return render(request, 'main/diseases.html', {'diseases': diseases_data})

class DiseaseDetailView(View):
    def get(self, request, key):
        disease = next((d for d in diseases_description if d["key"] == key), None)
        return render(request, 'main/diseases_detail.html', {'disease': disease})

    
