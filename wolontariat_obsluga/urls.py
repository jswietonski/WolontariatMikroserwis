from django.urls import path
from . import views
from .views import PublicMessageApiView, ProtectedMessageApiView, AdminMessageApiView


urlpatterns = [
    path('public', PublicMessageApiView.as_view(), name='public-message'),
    path(
        'protected', ProtectedMessageApiView.as_view(), name='protected-message'
    ),
    path('admin', AdminMessageApiView.as_view(), name='admin-message'),

    path('operator/create/', views.add_operator, name='Dodaj operatora projektu'),
    path('operator/all/', views.view_operator, name='Pokaz operatorow projektu'),
    path('operator/update/<int:pk>/', views.update_operator, name='Updatuj operatora projektu'),
    path('operator/item/<int:pk>/delete/', views.delete_operator, name='Usun operatora'),

    path('kategoria/create/', views.add_category, name='Dodaj kategorie'),
    path('kategoria/all/', views.view_category, name='Pokaz kategorie'),
    path('kategoria/update/<int:pk>/', views.update_category, name='Aktualizuj kategorie'),
    path('kategoria/item/<int:pk>/delete/', views.delete_category, name='Usun kategorie'),

    path('inicjatywa/create/', views.add_initiative, name='Dodaj inicjatywe'),
    path('inicjatywa/all/', views.view_initiative, name='Pokaz inicjatywy'),
    path('inicjatywa/update/<int:pk>/', views.update_initiative, name='Aktualizuj inicjatywe'),
    path('inicjatywa/item/<int:pk>/delete/', views.delete_initiative, name='Usun inicjatywe'),

    # path('uzytkownik/create/', views.add_user, name='Dodaj operatora projektu'),
    # path('uzytkownik/all/', views.view_user, name='Pokaz operatorow projektu'),
    # path('uzytkownik/update/<int:pk>/', views.update_user, name='update-items'),
    # path('uzytkownik/item/<int:pk>/delete/', views.delete_user, name='delete-items'),

    path('uczestnik/create/', views.add_participant, name='Dodaj uczestnika inicjatywy'),
    path('uczestnik/all/', views.view_participant, name='Pokaz uczestników inicjatywy'),
    path('uczestnik/update/<int:pk>/', views.update_participant, name='Aktualizuj uczestnika'),
    path('uczestnik/accept/<int:pk>/', views.accept_participant, name='Akceptuj uczestnika'),
    path('uczestnik/item/<int:pk>/delete/', views.delete_participant, name='Usun uczestnika'),
]
