from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.

def home(request):
    people = [
        {"name": "Alice", "age": 28, "role": "Developer"},
        {"name": "Bob", "age": 32, "role": "Designer"},
        {"name": "Charlie", "age": 25, "role": "Intern"},
    ]

    context = {
        "page": "Home",
        "people": people,
    }

    return render(request, "index.html", context=context)

def about (request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = (request.POST.get("name") or "").strip()
        email = (request.POST.get("email") or "").strip()
        message_text = (request.POST.get("message") or "").strip()

        context = {"page": "Contact", "name": name, "email": email, "message_value": message_text}

        if not (name and email and message_text):
            messages.info(request, "Please fill out all fields.")
            return render(request, "contact.html", context)

        # Here you could send an email or store the message. For now, just acknowledge receipt.
        messages.success(request, "Thanks! Your message has been sent.")
        return redirect("/contact/")

    return render(request, 'contact.html', context={'page': 'Contact'})

#backend to frontend data transfer: 
# we can use this data in frontend using {{key}} where key is the key of the context dictionary. 
# for example, if we want to use page variable in frontend, we can use {{page}} in frontend.

#and front end to backend data transfer:
# we can use forms to transfer data from frontend to backend.
#form will contain post method and action attribute which will specify the url to which the form data will be sent.