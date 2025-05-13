from django.utils.translation import activate, get_language
from tiler_project import settings

class CustomLocaleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lang = request.COOKIES.get("user_lang")
        print(f"Received user_lang: {lang}")  # Проверяем куки

        if not lang:
            lang = request.headers.get("Accept-Language", "").split(",")[0][:2].lower()
            print(f"Header lang: {lang}")  # Проверяем заголовок

        if lang in [code for code, _ in settings.LANGUAGES]:  # Проверяем поддержку языка
            activate(lang)
            request.LANGUAGE_CODE = lang
        else:
            lang = settings.LANGUAGE_CODE  # Запасной вариант
            print(f"Fallback lang: {lang}")  # Проверяем, какой язык берётся по умолчанию

        response = self.get_response(request)
        response["Content-Language"] = lang

        # Устанавливаем куки в ответе, чтобы язык сохранялся
        response.set_cookie("user_lang", lang, max_age=31536000, path="/")

        print(f"Final language set: {get_language()}")  # Проверяем, какой язык реально активирован

        return response
