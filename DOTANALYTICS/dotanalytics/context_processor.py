# myapp/context_processors.py
from django.conf import settings

def site_url(request):
     print(settings.SITE_URL)
     return {'SITE_URL': settings.SITE_URL}
