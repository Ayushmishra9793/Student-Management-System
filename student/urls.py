

from django.urls import path
from . import views
urlpatterns = [
    
    path("std", views.student_home, name= "student_home"),
    path("add-student", views.add_student , name='add_student'),
    path("delete-student/<int:student_id>", views.delete_student, name='delete_student'),
    path("update-student/<int:student_id>", views.update_student, name='update_student'),
]

# yaha hum sms ke urls.py se (student/) likhne per aay hai, now (std) likhte hi (views.student_home) views me student_home se ek function define hai useke pass chalo aur view karao display per
# IMP : "add-student" ye bss user ke dikhane ke liy karte hai , name='add_student' ye backend me as a url use karte hai

# path("delete-student/<int:id>"  => html se url ke sath sath int data type student_id ko laa rha hai, now student_id me jo store hai id vo views.py ke function(argument) me jayga

# path (route (url hota hai aur url me ye show karta hai), function, name )

# MVT => Model (DataBase) , View (function/urls) , Template ( UI )
