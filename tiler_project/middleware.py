from django.utils.translation import activate, get_language
from tiler_project import settings


class CustomLocaleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lang = request.COOKIES.get("user_lang", None)
        print(lang)
        if not lang:
            lang = request.headers.get("Accept-Language", "").split(",")[0][:2]
        if lang and lang in dict(settings.LANGUAGES):
            activate(lang)
            request.LANGUAGE_CODE = lang
        response = self.get_response(request)
        print(get_language())
        response["Content-Language"] = lang
        return response
