from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
from dj_static import Cling, MediaCling

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

application = Cling(MediaCling(get_wsgi_application()))