from django.contrib import admin
from Empire.models import Empire, EmpireCommanders, EmpireHeroes, EmpireBasicTroops, EmpireSpecialTroops, EmpireSingularTroops

@admin.register(Empire)
class EmpireAdmin(admin.ModelAdmin):
    pass

@admin.register(EmpireCommanders)
class EmpireCommandersAdmin(admin.ModelAdmin):
    pass

@admin.register(EmpireHeroes)
class EmpireHeroesAdmin(admin.ModelAdmin):
    pass

@admin.register(EmpireBasicTroops)
class EmpireBasicTroopsAdmin(admin.ModelAdmin):
    pass

@admin.register(EmpireSpecialTroops) 
class EmpireSpecialTroopsAdmin(admin.ModelAdmin):
    pass

@admin.register(EmpireSingularTroops)
class EmpireSingularTroopsAdmin(admin.ModelAdmin):
    pass 
  