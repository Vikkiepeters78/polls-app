from django.urls import path
from .views import index, contact, about, detail


app_name = 'polls'

urlpatterns = [
    path("", index, name='home'),
    path("contact", contact, name='contact_us'),
    path("about", about, name='about'),
    path('detail/<int:question_id>/', detail, name='detail')


]