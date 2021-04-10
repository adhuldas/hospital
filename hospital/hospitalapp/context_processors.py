from .models import Deprt


def menu_link(request):
    links = Deprt.objects.all()
    return dict(links=links)