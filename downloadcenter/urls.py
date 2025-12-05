from django import urls
from .views import index_function

urlpatterns = [
    urls.path("", index_function, name="home"),
]
