from django.shortcuts import render
<<<<<<< HEAD
from .classes import Pest,Protect_Against_Pest
from data.pests import pests_data
from data.pest_detail import pests_description
from data.disease_protection import protection_data
from django.views import View
from data.pest_protect import pest_protect_data
from data.diseases import diseases_data
from data.diseases_detail import diseases_description
from .classes import Protect_Against_Diseases

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
=======
from .classes import Pest, Protect_Against_Pest, Diseases_Protection, Protect_Against_Diseases
from data.pests import pests_data
from data.pest_detail import pests_description
from data.pest_protect import pest_protect_data
from data.disease_protection import protection_data
from data.diseases import diseases_data
from data.diseases_detail import diseases_description
from data.disease_protection_detail import protection_data as protection_detail
from django.views import View
import os
import base64
import io
from collections import Counter
from PIL import Image, ImageFilter
from django.shortcuts import render
from django.conf        import settings
from .forms             import ImageUploadForm,SurveySessionForm,SurveySession
from roboflow           import Roboflow
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.forms import ProfileForm, CustomPasswordChangeForm
from .models import UploadedImage, AnalyzedImage,SurveySession
from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView


def home_view(response):
    return render(response, "main/home.html", {})

class PestsView(View):
    def get(self, request):
>>>>>>> daa7809 (ASSIGNMENT 4 STRUCTURE)
        pests = self.combine_pests_data()
        return render(request, "main/pests.html", {"pests": pests})

    def combine_pests_data(self):
        return [Pest.from_data(p, pests_description) for p in pests_data]

class PestDetailView(View):
    def get(self, request, key):
<<<<<<< HEAD
        pest = None
        for p in pests_data:
            if p["key"] == key:
                pest = Pest.from_data(p, pests_description)
                break

=======
        pest = next((Pest.from_data(p, pests_description) for p in pests_data if p["key"] == key), None)
>>>>>>> daa7809 (ASSIGNMENT 4 STRUCTURE)
        if pest:
            return render(request, 'main/pest_detail.html', {"pest": pest})
        else:
            return render(request, 'pests/404.html', status=404)
<<<<<<< HEAD
        
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
        
=======
>>>>>>> daa7809 (ASSIGNMENT 4 STRUCTURE)

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

<<<<<<< HEAD
=======
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
>>>>>>> daa7809 (ASSIGNMENT 4 STRUCTURE)

class DiseasesView(View):
    def get(self, request):
        return render(request, 'main/diseases.html', {'diseases': diseases_data})

class DiseaseDetailView(View):
    def get(self, request, key):
        disease = next((d for d in diseases_description if d["key"] == key), None)
        return render(request, 'main/diseases_detail.html', {'disease': disease})
<<<<<<< HEAD
    
class DiseaseProtectionView(View):
    def get(self, request):
        return render(request, 'main/disease_protection.html', {'protections': protection_data})

class DiseaseProtectDetailView(View):
    def get(self, request, key):
        disease_protection = None
        for data in protection_data:
            if data["key"] == key:
                disease_protection = Protect_Against_Diseases.from_disease_prot_data(data, protection_data)
                break

        if disease_protection:
            return render(request, 'main/disease_protect_detail.html', {'disease': disease_protection})
        else:
            return render(request, 'pests/404.html', status=404)




=======

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

>>>>>>> daa7809 (ASSIGNMENT 4 STRUCTURE)
def about_us(request):
    return render(request, 'main/aboutus.html')


<<<<<<< HEAD
    
=======
def calculate(request):
    return render(request,'main/calculate.html')
rf      = Roboflow(api_key="3kaeexKXgE5Mt5pkD47L")
project = rf.workspace().project("mango-disy-z19mo")
def _infer_label(
    model,
    img_path,
    confidence: int = 80,
    filter_size: int = 5,
    min_pixels: int = 500,
    min_fraction: float = 0.01
) -> str:
    """
    Run one pass of inference + mask cleanup → return the dominant class label,
    or “Healthy mango” if the segmented area is too small.
    
    - confidence: pixel-confidence threshold (0–100).
    - filter_size: median-filter kernel size to remove noise.
    - min_pixels: absolute minimum number of “disease” pixels required.
    - min_fraction: minimum fraction of non-background pixels (e.g. 0.01 = 1%).
    """
    # 1) Predict & decode mask
    resp = model.predict(img_path, confidence=confidence).json()
    pred = resp["predictions"][0]
    
    mask_data = base64.b64decode(pred["segmentation_mask"])
    mask_img  = Image.open(io.BytesIO(mask_data)).convert("L")

    # 2) Clean up noise
    mask_img = mask_img.filter(ImageFilter.MedianFilter(size=filter_size))

    # 3) Tally non-background pixels
    pixels = list(mask_img.getdata())
    total  = len(pixels)

    counts = Counter(pixels)
    counts.pop(0, None)  # drop background

    disease_pixels = sum(counts.values())

    # 4) Area threshold: if too small, call it healthy
    if disease_pixels < min_pixels or (disease_pixels / total) < min_fraction:
        return "Healthy mango (no disease detected)"

    # 5) Otherwise pick the dominant disease class
    most_idx, _ = counts.most_common(1)[0]
    return pred["class_map"].get(str(most_idx), "Unknown")


class AnalyzeImageView(View):
    template_name = "main/analyze.html"
    form_class    = ImageUploadForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request, *args, **kwargs):
        action = request.POST.get("action")

        # 1) UPLOAD & ANALYZE
        if action == "analyze":
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                upload   = form.save()  # ← this is an UploadedImage instance
                img_path = os.path.join(settings.MEDIA_ROOT, upload.image.name)

                # run inference…
                versions_list  = project.versions()
                latest_version = max(v.version for v in versions_list)
                model          = project.version(latest_version).model

                first  = _infer_label(model, img_path)
                second = _infer_label(model, img_path)
                label = first if first == second else (first if first != "No object detected" else second)

                return render(request, self.template_name, {
                    "form":   self.form_class(),
                    "upload": upload,
                    "label":  label,
                })

            # invalid upload → re-render form with errors
            return render(request, self.template_name, {"form": form})

        # 2) SAVE RECORD
        elif action == "save":
            uid    = request.POST.get("upload_id")
            label  = request.POST.get("label")
            upload = UploadedImage.objects.get(pk=uid)

            AnalyzedImage.objects.create(
                grower = request.user,
                upload = upload,
                label  = label
            )
            messages.success(request, "✅ Analysis saved!")
            return redirect("session-list")

        # fallback
        return redirect("analyze")
    


@login_required
def profile(request):
    if request.method == 'POST':
        # Determine which form was submitted by button name
        if 'update_profile' in request.POST:
            p_form  = ProfileForm(request.POST, instance=request.user)
            pw_form = CustomPasswordChangeForm(user=request.user)
            if p_form.is_valid():
                p_form.save()
                messages.success(request, "Your profile has been updated.")
                return redirect('profile')
        elif 'change_password' in request.POST:
            p_form  = ProfileForm(instance=request.user)
            pw_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
            if pw_form.is_valid():
                user = pw_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Your password was successfully changed.")
                return redirect('profile')
    else:
        p_form  = ProfileForm(instance=request.user)
        pw_form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'accounts/profile.html', {
        'p_form':  p_form,
        'pw_form': pw_form,
    })




class SessionListView(LoginRequiredMixin, ListView):
    model               = SurveySession
    template_name       = 'main/session_list.html'
    context_object_name = 'sessions'

    def get_queryset(self):
        return SurveySession.objects.filter(grower=self.request.user)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['analyzed_images'] = AnalyzedImage.objects.filter(grower=self.request.user)
        return ctx

class SessionCreateView(LoginRequiredMixin, View):
    template_name = 'main/session_form.html'

    def get(self, request):
        form = SurveySessionForm(user=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SurveySessionForm(request.POST, user=request.user)
        if form.is_valid():
            sess = form.save(commit=False)
            sess.grower = request.user
            sess.save()
            messages.success(request, "Record saved successfully.")
            return redirect('session-list')
        return render(request, self.template_name, {'form': form})
    


class SessionDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView
):
    model = SurveySession
    template_name = 'main/session_confirm_delete.html'
    success_url = reverse_lazy('session-list')

    def test_func(self):
        # only the owner can delete
        return self.get_object().grower == self.request.user
    

class AnalyzedImageListView(LoginRequiredMixin, ListView):
    model               = AnalyzedImage
    template_name       = 'main/session_list.html'
    context_object_name = 'analyzed_images'
    
    def get_queryset(self):
        # only show analyses for the logged-in user
        return AnalyzedImage.objects.filter(grower=self.request.user)

    def get_context_data(self, **kwargs):
        # grab the default context (which already has 'analyzed_images')
        context = super().get_context_data(**kwargs)
        # add your survey sessions into the same context
        context['sessions'] = SurveySession.objects.filter(grower=self.request.user)
        return context
    
class AnalyzedImageDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView
):
    model = AnalyzedImage
    template_name = 'main/analyzed_confirm_delete.html'
    success_url = reverse_lazy('session-list')

    def test_func(self):
        # only the owner can delete their analysis
        return self.get_object().grower == self.request.user
>>>>>>> daa7809 (ASSIGNMENT 4 STRUCTURE)
