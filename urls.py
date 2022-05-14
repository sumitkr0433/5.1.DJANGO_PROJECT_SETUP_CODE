from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cowform.urls'))
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


====================================================================================================================================================
from django.urls import path
from . import views
urlpatterns = [
      path('articles/<int:year>/', views.year_archive),
      path('articles/<int:year>/<int:month>/', views.month_archive),
      path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]
===================================================================================================================================================
