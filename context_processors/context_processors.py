from contact_us_app.models import ContactUsInfo
from post_detail_app.models import Category


def all_categories(request):
    categories = Category.objects.all()
    return {"categories": categories}


def social_media_links(request):
    contact_us_info = ContactUsInfo.objects.all().last()
    return {"contact_us_info": contact_us_info}
