import requests

class TranslationService:
    BASE_URL = "https://api.mymemory.translated.net/get"

    @staticmethod
    def translate(text, source, target):
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

        return data["responseData"]["translatedText"]