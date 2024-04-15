from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import mail_admins
from formation.models import Formation, SaleFormation, FormationVideo, VideoComment
from django.db.models import Count, F
from django.core.handlers.wsgi import WSGIRequest
from ebook.models import EbookModel

@login_required
def index(request: WSGIRequest):
    # mail_admins(subject="Le mail de test Django", message="Le contenu de ce mail")

    return render(request, "profil/index.html", context={"current_tab": "home"})


@login_required
def formation(request):
    my_formations = Formation.objects.annotate(
        user=F("saleformation__user__id"),
        isPaid=F("saleformation__isPaid"),
        video_count=Count('formationvideo')
    )
    formations = my_formations.filter(user=request.user.id, isPaid=True)
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
        # video_count=Count('formationvideo')
    )
    ebooks = my_ebook.filter(user=request.user.id)
    context = {
        "ebooks": ebooks,
        "current_tab": "ebook",
        "title": "Mes ouvrages | Site vie de réussite"
    }

    return render(request, "profil/ebook.html", context=context)


@login_required
def detail(request, formation_id: int):
    formation_videos = FormationVideo.objects.filter(formation__id=formation_id)
    current_v_index = request.GET.get("current_v_index")
    current_video = None
    next_video = None
    if current_v_index is None:
        current_v_index = formation_videos[0].id if len(formation_videos) != 0 else None
    for i, vid in enumerate(formation_videos):
        if vid.id == int(current_v_index):
            current_video = vid
            if not i+1 == len(formation_videos):
                next_video = formation_videos[i+1]
            break
    video_comments = VideoComment.objects.filter(video__id=current_video.id, published=True)

    context = {
        "videos": formation_videos,
        "current_video": current_video,
        "next_video": next_video,
        "current_tab": "formation",
        "title": current_video.formation.title,
        "video_comments": video_comments,
        "profil_title": current_video.formation.title
    }
    return render(request, "profil/details.html",  context=context)

