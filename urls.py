from django.conf import settings
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import path, reverse


def goto(request: HttpRequest, destination: str) -> HttpResponse:
    try:
        url_name: str = settings.GOTO_DESTINATIONS[destination]
    except KeyError:
        raise Http404 from None
    return HttpResponseRedirect(reverse(url_name))

def register_robots():
    return [
        ("User-agent: *", "Disallow: /goto/")
    ]

urlpatterns = [
        path("goto/<str:destination>/", goto, name="goto"),
]
