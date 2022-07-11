
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from jobiter import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),

    path('api/reviews/',include('reviews.urls')),
    path('api/interviews/',include('interviews.urls')),

    path('api/profiles/', include('profiles.urls')),
    path('api/skills/', include('skills.urls'))

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
