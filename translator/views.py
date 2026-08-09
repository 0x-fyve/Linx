from django.shortcuts import render
from .services import TranslationService
from .models import Translation
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
def home(request):
    translated_text = None
    if request.method == "POST":

        if not request.session.session_key:
            request.session.create()

        current_session_id = request.session.session_key    

        text = request.POST.get("source_text")
        source_language = request.POST.get("source_language")
        target_language = request.POST.get("target_language")

        translation = TranslationService.translate(text, source_language, target_language, current_session_id)
        translations = Translation.objects.filter(session_key=current_session_id).order_by("-created_at")
        favorites = Translation.objects.filter(session_key=current_session_id, is_favorite=True).order_by("-created_at")

        context = {
            "text": text,
            "translation": translation,
            "source_language": source_language,
            "target_language": target_language,
            "translations": translations,
            "favorites": favorites
        }

        return render(request, "translator/index.html", context)
    return render(
        request, "translator/index.html", 
        {
            "translations": Translation.objects.filter(session_key=request.session.session_key).order_by("-created_at"),
            "favorites": Translation.objects.filter(session_key=request.session.session_key, is_favorite=True).order_by("-created_at"),
        })

def favorite(request, id):
    translation = get_object_or_404(Translation, id=id, session_key=request.session.session_key)

    translation.is_favorite = not translation.is_favorite
    translation.save()

    return redirect("/")

def delete_translation(request, id):
    translation = get_object_or_404(Translation, id=id, session_key=request.session.session_key)
    translation.delete()
    return redirect("/")