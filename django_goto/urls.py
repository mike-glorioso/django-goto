from django.conf import settings
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import path, reverse
from django_robots_registry import RobotSpec, RobotSpecProvider

app_name = "goto"


def goto(request: HttpRequest, destination: str) -> HttpResponse:
    try:
        url_name: str = settings.GOTO_DESTINATIONS[destination]
    except KeyError:
        raise Http404 from None
    return HttpResponseRedirect(reverse(url_name))


class GotoRobots(RobotSpecProvider):
    def __init__(self, *, base_url: str = "goto", user_agent: str = "*") -> None:
        self.base_url = base_url
        self.user_agent = user_agent
        super().__init__()

    def __call__(self) -> RobotSpec:
        return RobotSpec(user_agent=self.user_agent, instruction=f"Disallow: /{self.base_url}")


urlpatterns = [
    path("<str:destination>/", goto, name="goto"),
]
