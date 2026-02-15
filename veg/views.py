from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Recepie
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def recepies(request):
    if request.method == "POST":
        r_name = request.POST.get("r_name")
        r_description = request.POST.get("r_description")
        r_image = request.FILES.get("r_image")

        if not r_name or not r_description:
            queryset = Recepie.objects.filter(user=request.user)
            error = "Name and description are required."
            return render(request, "recepies.html", {"recepies": queryset, "error": error})

        Recepie.objects.create(
            r_name=r_name,
            r_description=r_description,
            r_image=r_image,
            user=request.user,
        )
        return redirect("/recepies/")

    search_term = (request.GET.get("search") or "").strip()
    queryset = Recepie.objects.filter(user=request.user)
    if search_term:
        queryset = queryset.filter(
            Q(r_name__icontains=search_term) | Q(r_description__icontains=search_term)
        )

    return render(request, "recepies.html", {"recepies": queryset, "search_term": search_term})


@login_required(login_url="/login/")
def delete_recepie(request, id):
    Recepie.objects.filter(id=id, user=request.user).delete()
    messages.info(request, "Recipe deleted successfully.")
    return redirect("/recepies/")


@login_required(login_url="/login/")
def update_recepie(request, id):
    recipe = get_object_or_404(Recepie, id=id, user=request.user)

    if request.method == "POST":
        recipe.r_name = request.POST.get("r_name")
        recipe.r_description = request.POST.get("r_description")
        if request.FILES.get("r_image"):
            recipe.r_image = request.FILES.get("r_image")
        recipe.save()
        return redirect("/recepies/")

    return render(request, "updated_recepies.html", {"recepie": recipe})


def login(request):
    if request.method == "POST":
        username = request.POST.get("username") or ""
        password = request.POST.get("password") or ""

        if not User.objects.filter(username=username).exists():
            error = "Invalid Username. Please try again."
            messages.info(request, error)
            return render(request, "veg/login.html", {"error": error, "username": username})

        user = authenticate(username=username, password=password)

        if user is None:
            error = "Invalid credentials. Please try again."
            messages.info(request, error)
            return render(request, "veg/login.html", {"error": error, "username": username})

        auth_login(request, user)
        return redirect("/recepies/")

    return render(request, "veg/login.html")


def logout(request):
    auth_logout(request)
    return redirect("/login/")


def register(request):
    if request.method == "POST":
        first_name = (request.POST.get("first_name") or "").strip()
        last_name = (request.POST.get("last_name") or "").strip()
        username = (request.POST.get("username") or "").strip()
        email = (request.POST.get("email") or "").strip()
        password = request.POST.get("password") or ""

        context = {
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "email": email,
        }

        if not (first_name and last_name and username and email and password):
            error = "All fields are required."
            messages.info(request, error)
            context["error"] = error
            return render(request, "register.html", context)

        if User.objects.filter(username=username).exists():
            error = "Username already exists."
            messages.info(request, error)
            context["error"] = error
            return render(request, "register.html", context)

        if User.objects.filter(email=email).exists():
            error = "Email already exists. Please login."
            messages.info(request, error)
            context["error"] = error
            return render(request, "register.html", context)

        User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )

        return redirect("/login/")

    return render(request, "register.html")
