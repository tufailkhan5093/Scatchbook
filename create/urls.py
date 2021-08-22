from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="create"),
    path("one/", views.one, name="one"),
    path("two/", views.two, name="two"),
    path("three/", views.three, name="three"),
    #path("three/", views.Prompt2, name="three"),
    path("final/", views.final, name="final"),
    path("afterfinal/", views.after_final, name="afterfinal"),
    path("link/<str:str>/<int:id>/", views.s_link, name="s_link"),

    path("viewbook/", views.viewbook, name="viewbook"),
    path("steps/", views.steps, name="steps"),
    path("steps_save", views.steps_save, name="steps_save"),
    path('delete',views.delete,name='delete'),
    path('update',views.messageone,name='update'),
    path('message2',views.messagetwo,name='messagetwo'),
    path('done',views.done,name='done'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
