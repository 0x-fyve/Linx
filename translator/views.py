from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == "POST":
        text = request.POST.get("text")
        source_language = request.POST.get("source_language")
        target_language = request.POST.get("target_language")

        # Here you would typically call your translation function or API
        # For demonstration, let's just reverse the text as a placeholder
        translated_text = text[::-1]  # Placeholder for actual translation logic

        context = {
            "text": text,
            "translated_text": translated_text,
            "source_language": source_language,
            "target_language": target_language,
        }
        return render(request, "translator/index.html", context)
    return render(request, "translator/index.html")
