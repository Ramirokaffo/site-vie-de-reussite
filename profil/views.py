from django.contrib.auth.decorators import login_required
from django.core.mail import mail_admins
from formation.models import Formation, SaleFormation, FormationVideo, VideoComment
from django.db.models import Count, F
from django.core.handlers.wsgi import WSGIRequest
from ebook.models import EbookModel
from .models import UserProfilModel
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage


@login_required
def index(request: WSGIRequest):
    # mail_admins(subject="Le mail de test Django", message="Le contenu de ce mail")
    return formation(request)
    return render(request, "profil/index.html", context={"current_tab": "home"})


@login_required
def formation(request):
    my_formations = Formation.objects.annotate(
        user=F("saleformation__user__id"),
        isPaid=F("saleformation__isPaid"),
        video_count=Count('formationvideo')
    )
    formations = my_formations.filter(user=request.user.id, isPaid=True, published=True)
    context = {
        "formations": formations,
        "title": "Mes formations | Site vie de réussite",
        "current_tab": "formation"
    }
    # mail_admins(subject="Le mail de test Django", message="Le contenu de ce mail")
    return render(request, "profil/formation.html", context=context)


@login_required
def ebook(request):
    # mail_admins(subject="Le mail de test Django", message="Le contenu de ce mail")
    my_ebook = EbookModel.objects.annotate(
        user=F("saleebook__user__id"),
        isPaid=F("saleebook__isPaid"),
    )
    ebooks = my_ebook.filter(user=request.user.id, published=True, isPaid=True)
    context = {
        "ebooks": ebooks,
        "current_tab": "ebook",
        "title": "Mes ouvrages | Site vie de réussite"
    }

    return render(request, "profil/ebook.html", context=context)


@login_required
def detail(request, formation_id: int):
    my_formations = Formation.objects.annotate(
        user=F("saleformation__user__id"),
        isPaid=F("saleformation__isPaid"),
        video_count=Count('formationvideo')
    )
    formation = my_formations.filter(user=request.user.id, isPaid=True, id=formation_id)
    if formation:
        formation_videos = FormationVideo.objects.filter(formation__id=formation_id).order_by("order")
        current_v_index = request.GET.get("current_v_index")
        current_video = None
        next_video = None
        prev_video = None
        if current_v_index is None:
            current_v_index = formation_videos[0].id if len(formation_videos) != 0 else None
        for i, vid in enumerate(formation_videos):
            if vid.id == int(current_v_index):
                current_video = vid
                if not i+1 == len(formation_videos):
                    next_video = formation_videos[i+1]
                if i != 0:
                    prev_video = formation_videos[i-1]
                break
        if current_video is None:
            return render(request, "profil/unauthorised.html")
        video_comments = VideoComment.objects.filter(video__id=current_video.id, published=True)

        context = {
            "videos": formation_videos,
            "current_video": current_video,
            "prev_video": prev_video,
            "next_video": next_video,
            "current_tab": "formation",
            "title": current_video.formation.title,
            "video_comments": video_comments,
            "profil_title": current_video.formation.title
        }
        return render(request, "profil/details.html",  context=context)
    else:
        return render(request, "profil/unauthorised.html")



@login_required
def update(request: WSGIRequest):  
  if request.method == 'POST':
    author = request.user
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    uploaded_image = request.FILES.get('profilImage')
    user_profil = request.session.get("user_profile")
    if user_profil is None:
       new_user_profil = UserProfilModel.objects.create(user=author)
    else:
       new_user_profil = UserProfilModel.objects.get(id=user_profil.get("id"))
    if uploaded_image:
        image_filename = f'images/profil/user_image_{request.user.id}.jpg'
        image_path = default_storage.save(image_filename, uploaded_image)
        new_user_profil.profil_image = image_path
        
    author.first_name = first_name
    author.last_name = last_name

    author.save()
    new_user_profil.save()

    request.session['user_profile'] = {
            'id': new_user_profil.id,
            "profil_image": new_user_profil.profil_image.url
        }
    messages.success(request, "Profil modifié avec succès !")
    return redirect("profil:formation")
   


