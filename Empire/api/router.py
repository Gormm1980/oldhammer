from django.urls import path
from Empire.api.views import Empire, EmpireCommander, EmpireHeroes, EmpireBasicTroops, EmpireSpecialTroops, EmpireSingularTroops 


urlpatterns = [
    path('empire/', Empire.as_view(), name= 'Human Empire'),
    path('empire/Commanders/', EmpireCommander.as_view()),
    path('empire/Heroes/', EmpireHeroes.as_view()),
    path('empire/BasicTroops/', EmpireBasicTroops.as_view()),
    path('empire/SpecialTroops/', EmpireSpecialTroops.as_view()),
    path('empire/SingularTroops/', EmpireSingularTroops.as_view()),
   
]