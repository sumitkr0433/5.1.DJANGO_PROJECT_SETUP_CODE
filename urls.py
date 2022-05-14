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
from django.urls import path
from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
=======================================================================================================================================================
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
