from blogs.models import Category,Links

def get_categories(request):
    categories=Category.objects.all()
    return dict(categories=categories)


def get_social_links(request):
    social_link=Links.objects.all()
    return dict(social_link=social_link)