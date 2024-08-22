from django.urls import include, path
from rest_framework.routers import SimpleRouter

from todo.system.api.views import SentryDebugViewSet

router = SimpleRouter()

# app_name = "api"

router.register("system/sentry", SentryDebugViewSet)
urlpatterns = router.urls
urlpatterns += [
    path("api/v1/", include(("todo.users.api.v1.urls", "users_api"), namespace="users_api")),
    path("api/v1/", include(("todo.trivia.api.v1.urls", "trivia_api"), namespace="trivia_api")),
    path("api/v1/", include(("todo.questions.api.v1.urls", "questions_api"), namespace="questions_api")),
    path("api/v1/", include(("todo.teams.api.v1.urls", "teams_api"), namespace="teams_api")),
    path("api/v1/", include(("todo.events.api.v1.urls", "events_api"), namespace="events_api")),
    path("api/v1/", include(("todo.rosters.api.v1.urls", "rosters_api"), namespace="rosters_api")),
    path(
        "api/v1/", include(("todo.organizations.api.v1.urls", "organizations_api"), namespace="organizations_api")
    ),
]
