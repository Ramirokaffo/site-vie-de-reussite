from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.core.files.storage import default_storage
from profil.models import UserProfilModel
from django.contrib import messages
from .models import TestimonyModel

@login_required
def create(request: WSGIRequest):  
  if request.method == 'POST':
    author = request.user
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    content = request.POST.get('content')
    rate = request.POST.get('rate')
    uploaded_image = request.FILES.get('profilImage')
    new_user_profil = UserProfilModel.objects.create(user=author)
    if uploaded_image:
        image_filename = f'user_image_{request.user.id}.jpg'  # Example filename
        image_path = default_storage.save(image_filename, uploaded_image)
        new_user_profil.profil_image = image_path
    my_testimony = TestimonyModel.objects.create(author=author, content=content, rate=int(rate))
    author.first_name = first_name
    author.last_name = last_name

    author.save()
    my_testimony.save()
    new_user_profil.save()

    messages.success(request, "Témoignage enregistré avec succès !")
    return render(request, 'index.html')
  else:
    return render(request, 'testimony/create.html')
        