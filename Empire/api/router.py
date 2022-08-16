from django.urls import path
from Empire.api.views import Empire, EmpireCommander, EmpireHeroes, EmpireBasicTroops, EmpireSpecialTroops, EmpireSingularTroops 


urlpatterns = [
    path('empire/', Empire.as_view({'get': Empire}), name= 'Human Empire'),
    path('empire/Commanders/', EmpireCommander.as_view({'get': EmpireCommander, 'post': EmpireCommander, 'delete': EmpireCommander}), name= 'Human Empire Commanders'),
    path('empire/Heroes/', EmpireHeroes.as_view({'get': EmpireHeroes, 'post': EmpireHeroes, 'delete': EmpireHeroes}), name= 'Human Empire Heroes'),
    path('empire/BasicTroops/', EmpireBasicTroops.as_view({'get': EmpireBasicTroops, 'post': EmpireBasicTroops, 'delete': EmpireBasicTroops}), name= 'Human Empire Basic Troops'),
    path('empire/SpecialTroops/', EmpireSpecialTroops.as_view({'get': EmpireSpecialTroops, 'post': EmpireSpecialTroops, 'delete': EmpireSpecialTroops}), name= 'Human Empire Special Troops'),
    path('empire/SingularTroops/', EmpireSingularTroops.as_view({'get': EmpireSingularTroops, 'post': EmpireSingularTroops, 'delete': EmpireSingularTroops}), name= 'Human Empire Singular Troops'),
   
]