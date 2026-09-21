from django.conf import settings
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import path, reverse

app_name = "goto"


def goto(request: HttpRequest, destination: str) -> HttpResponse:
    try:
        url_name: str = settings.GOTO_DESTINATIONS[destination]
    except KeyError:
        raise Http404 from None
    return HttpResponseRedirect(reverse(url_name))


def register_robots(*, base_url: str = "", user_agent: str = "*"):
    return [(f"User-agent: {user_agent}", f"Disallow: /{base_url}")]


urlpatterns = [
    path("<str:destination>/", goto, name="goto"),
]
