# django_goto

Short, memorable redirect links (`/goto/<key>/`) that resolve to real
Django URL names via a settings dict — handy for marketing links, QR
codes, or anywhere you want a stable short path that can point at a
different destination later without touching a template.

## Usage

```python
# settings.py
INSTALLED_APPS = [
    ...,
    "django_goto",
]

GOTO_DESTINATIONS = {
    "roi": "marketing:roi",
    "prestige": "marketing:prestige",
}
```

```python
# urls.py
urlpatterns = [
    path("goto/", include("django_goto.urls")),
]
```

Visiting `/goto/roi/` redirects to whatever URL `reverse("marketing:roi")`
resolves to. An unknown key returns a 404.

### robots.txt

`django_goto.urls` also exports `GotoRobots`, a
[`django_robots_registry`](https://github.com/mike-glorioso/django-robots-registry)
provider that disallows crawling the redirect paths themselves:

```python
from django_goto.urls import GotoRobots
from django_robots_registry import robots_txt_view

urlpatterns = [
    path("robots.txt", robots_txt_view(GotoRobots())),
]
```

## Status

Extracted from an internal project (glotronic.net), with full commit
history preserved via `git subtree split`. Small and stable; grown
on-demand as needed.

## License

BSD-3-Clause — see [LICENSE](LICENSE).
