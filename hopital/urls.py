from django.urls import path
from .views import (
    admin_login, logout_admin, home, about, contact, index,
    View_Doctor, Add_Doctor, Delete_Doctor,View_Patient,Add_Patient,Add_Appointment,Add_Facture,
    Add_Medicament, view_medicament, Update_medicament, Delete_Medicament,Delete_Patient,View_Appointment,Delete_Appointment,
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('index/', index, name='index'),
    path('admin_login/', admin_login, name='admin_login'),
    path('logout/', logout_admin, name='logout_admin'),
    path('index/', index, name='dashboard'),  # Correction : éviter la duplication d'index
    
    # Routes pour les docteurs
    path('view_doctor/', View_Doctor, name='view_doctor'),
    path('delete_doctor/<int:pid>/', Delete_Doctor, name='delete_doctor'),
    path('add_doctor/', Add_Doctor, name='add_doctor'),
    
    path('view_patient/', View_Patient, name='view_patient'),
    path('delete_patient/<int:pid>/', Delete_Patient, name='delete_patient'),
    path('add_patient/', Add_Patient, name='add_patient'),

    path('view_appointment/', View_Appointment, name='view_appointment'),
    path('delete_appointment/<int:pid>/', Delete_Appointment, name='delete_appointment'),
    path('add_appointment/', Add_Appointment, name='add_appointment'),
    # Routes pour les médicaments
    path('add_medicament/', Add_Medicament, name='add_medicament'),
    path('view_medicament/', view_medicament, name='view_medicament'),
    
    path('add_facture/', Add_Facture, name='add_facture'),
    
    
    path('update_medicament/<int:pid>/', Update_medicament, name='update_medicament'),
    path('delete_medicament/<int:pid>/', Delete_Medicament, name='delete_medicament'),  # Correction du nom
]
