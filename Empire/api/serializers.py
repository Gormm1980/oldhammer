from rest_framework import serializers
from Empire.models import Empire, EmpireCommanders, EmpireHeroes, EmpireBasicTroops, EmpireSpecialTroops, EmpireSingularTroops

class EmpireCommandersSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmpireCommanders  
        exclude = ['is_removed', 'created', 'modified']
    


class EmpireHeroesSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmpireHeroes  
        exclude = ['is_removed', 'created', 'modified']
        
  

class EmpireBasicTroopsSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmpireBasicTroops  
        exclude = ['is_removed', 'created', 'modified']
        
 
        
class EmpireSpecialTroopsSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmpireSpecialTroops  
        exclude = ['is_removed', 'created', 'modified']
        


class EmpireSingularTroopsSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmpireSingularTroops  
        exclude = ['is_removed', 'created', 'modified']
        


class EmpireSerializers(serializers.ModelSerializer):
    class Meta:
        model = Empire  
        exclude = ['is_removed', 'created', 'modified']
        
   
    