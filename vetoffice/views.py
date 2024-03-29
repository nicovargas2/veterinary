from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import random
from vetoffice.models import Owner, Patient
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


fortuneList = [
    "Do not be afraid of competition.",
    "An exciting opportunity lies ahead of you.",
    "You love peace.",
    "Get your mind set…confidence will lead you on.",
    "You will always be surrounded by true friends.",
    "Sell your ideas-they have exceptional merit.",
    "You should be able to undertake and complete anything.",
    "You are kind and friendly.",
    "You are wise beyond your years.",
    "Your ability to juggle many tasks will take you far.",
    "A routine task will turn into an enchanting adventure.",
    "Beware of all enterprises that require new clothes.",
    "Be true to your work, your word, and your friend.",
    "Goodness is the only investment that never fails.",
    "A journey of a thousand miles begins with a single step.",
    "Forget injuries; never forget kindnesses.",
    "Respect yourself and others will respect you.",
    "A man cannot be comfortable without his own approval.",
    "Always do right. This will gratify some people and astonish the rest.",
    "It is easier to stay out than to get out.",
    "Sing everyday and chase the mean blues away.",
    "You will receive money from an unexpected source.",
    "Attitude is a little thing that makes a big difference.",
    "Plan for many pleasures ahead.",
    "Experience is the best teacher.",
    "You will be happy with your spouse.",
    "Expect the unexpected.",
    "Stay healthy. Walk a mile.",
    "The family that plays together stays together.",
    "Eat chocolate to have a sweeter life.",
    "Once you make a decision the universe conspires to make it happen.",
    "Make yourself necessary to someone.",
    "The only way to have a friend is to be one.",
    "Nothing great was ever achieved without enthusiasm.",
    "Dance as if no one is watching.",
    "Live this day as if it were your last.",
    "Your life will be happy and peaceful.",
    "Reach for joy and all else will follow.",
    "Move in the direction of your dreams.",
    "Bloom where you are planted.",
    "Appreciate. Appreciate. Appreciate.",
    "Happy News is on its way.",
]

pets = [
    {
        "petname": "Fido Dido",
        "animal_type": "dog",
        "description": "This dog is very lovely",
    },
    {
        "petname": "Clementine",
        "animal_type": "cat",
        "description": "Beware with this animal!",
    },
    {"petname": "Theo Dominguez", "animal_type": "cat", "description": "Lovely cat"},
    {
        "petname": "Oreo",
        "animal_type": "dog",
        "description": "There's no better dog than this one!",
    },
]

# Create your views here.


def home(request):
    # template = loader.get_template("vetoffice/home.html")
    context = {"name": "Jhon Doe", "pets": pets}
    # return HttpResponse(template.render())
    return render(request, "vetoffice/home.html", context)


def fortune(request):
    fortune = random.choice(fortuneList)
    context = {"fortune": fortune}
    return render(request, "vetoffice/fortune.html", context)


def detail(request, petname):
    pet = petname.replace("-", " ")
    pet = pet.title()
    description = ""
    for animal in pets:
        if pet == animal["petname"]:
            description = animal["description"]
    context = {"petname": pet, "description": description}
    return render(request, "vetoffice/detail.html", context)


def pets_by_user(request, ownerId):
    # buscar asi con id o por nombre Y apellido
    owner_searched = Owner.objects.get(owner_id=ownerId)
    pets = Patient.objects.get(owner=owner_searched)
    context = {"pets": pets}
    return render(request, "vetoffice/pets.html", context)


class OwnerList(ListView):
    model = Owner
    template_name = "vetoffice/owner_list.html"


class OwnerCreate(CreateView):
    model = Owner
    template_name = "vetoffice/owner_create_form.html"
    fields = [
        "first_name",
        "last_name",
        "phone",
    ]


class OwnerUpdate(UpdateView):
    model = Owner
    template_name = "vetoffice/owner_update_form.html"
    fields = [
        "first_name",
        "last_name",
        "phone",
    ]


class OwnerDelete(DeleteView):
    model = Owner
    template_name = "vetoffice/owner_delete_form.html"


class PatientList(ListView):
    model = Patient
    template_name = "vetoffice/patient_list.html"


class PatientCreate(CreateView):
    model = Patient
    template_name = "vetoffice/patient_create_form.html"
    fields = [
        "animal_type",
        "breed",
        "pet_name",
        "age",
        "owner",
    ]


class PatientUpdate(UpdateView):
    model = Patient
    template_name = "vetoffice/patient_update_form.html"
    fields = [
        "animal_type",
        "breed",
        "pet_name",
        "age",
        "owner",
    ]


class PatientDelete(DeleteView):
    model = Patient
    template_name = "vetoffice/patient_delete_form.html"
