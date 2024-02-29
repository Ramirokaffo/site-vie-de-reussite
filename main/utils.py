from django.core.exceptions import ValidationError


def validate_video_file(value):
    if not value.name.endswith('.mp4'):
        raise ValidationError("Le fichier doit être au format MP4")