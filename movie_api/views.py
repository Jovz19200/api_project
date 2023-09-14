from rest_framework.permissions import AllowAny
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title = "swagger documentation",
        default_version = "v1",
        description = "this will show you how the api is structured",
        contact = openapi.Contact(email = "mugabo.kefa00@gmail.com"),
    ),
    public = True,
    permission_classes = (permissions.AllowAny,),

)