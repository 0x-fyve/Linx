import requests
from .models import Translation

class TranslationService:
    BASE_URL = "https://api.mymemory.translated.net/get"

    @staticmethod
    def translate(text, source, target, current_session_id):
        response = requests.get(
            TranslationService.BASE_URL,
            params={
                "q": text,
                "langpair": f"{source}|{target}"
            },
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        translation =Translation.objects.create(
            session_key = current_session_id,
            text = text,
            source_language = source,
            target_language = target,
            translated_text = data["responseData"]["translatedText"]
        )

        return translation