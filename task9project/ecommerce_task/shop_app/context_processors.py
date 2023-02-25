from .models import Category1
def menu_links(request):
    links=Category1.objects.all()
    return dict(links=links)