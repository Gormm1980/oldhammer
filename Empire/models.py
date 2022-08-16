from django.db import models

# Create your models here.
class FeaturesModels(models.Model):
    movement= models.IntegerField( blank=False, null=False)
    HA = models.IntegerField( blank=False, null=False)
    HP = models.IntegerField( blank=False, null=False)
    Strength = models.IntegerField( blank=False, null=False) 
    Resistance = models.IntegerField( blank=False, null=False)
    Health = models.IntegerField( blank=False, null=False)
    Attacks = models.IntegerField( blank=False, null=False)
    leadership = models.IntegerField( blank=False, null=False)
    Equipment_Options = models.CharField( max_length=50, blank=False, null=False)
    Points = models.IntegerField( blank=False, null=False)
  
class EmpireCommanders (models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=250, blank=False, null=False)
    Special_rules = models.TextField(max_length=250, blank=False, null=False)
    url_images = models.URLField( blank=False, null=False) 
    Magic_Objects = models.TextField( blank=False, null=False)
    MountAndMonsters = models.TextField( blank=False, null=False)
    FeaturesModels = models.ForeignKey(FeaturesModels, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class EmpireHeroes (models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=250, blank=False, null=False)
    Special_rules = models.TextField(max_length=250, blank=False, null=False)
    url_images = models.URLField( blank=False, null=False) 
    Magic_Objects = models.TextField( blank=False, null=False)
    MountAndMonsters = models.TextField( blank=False, null=False)
    FeaturesModels = models.ForeignKey(FeaturesModels, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class EmpireBasicTroops(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=250, blank=False, null=False)
    Special_rules = models.TextField(max_length=250, blank=False, null=False)
    url_images = models.URLField( blank=False, null=False)  
    FeaturesModels = models.ForeignKey(FeaturesModels, on_delete=models.CASCADE)
  
    def __str__(self):
        return self.name
    
class EmpireSpecialTroops(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=250, blank=False, null=False)
    Special_rules = models.TextField(max_length=250, blank=False, null=False)
    url_images = models.URLField( blank=False, null=False)  
    FeaturesModels = models.ForeignKey(FeaturesModels, on_delete=models.CASCADE)
  
    def __str__(self):
        return self.name

class EmpireSingularTroops(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=250, blank=False, null=False)
    Special_rules = models.TextField(max_length=250, blank=False, null=False)
    url_images = models.URLField( blank=False, null=False)  
    FeaturesModels = models.ForeignKey(FeaturesModels, on_delete=models.CASCADE)
  
    def __str__(self):
        return self.name
    
class Empire(models.Model):
   EmpireCommanders = models.ForeignKey(EmpireCommanders, on_delete=models.CASCADE)
   EmpireHeroes = models.ForeignKey(EmpireHeroes, on_delete=models.CASCADE)
   EmpireBasicTroops = models.ForeignKey(EmpireBasicTroops, on_delete=models.CASCADE)
   EmpireSingularTroops = models.ForeignKey(EmpireSingularTroops, on_delete=models.CASCADE)
   EmpireSpecialTroops = models.ForeignKey(EmpireSpecialTroops, on_delete=models.CASCADE)
   
   def __str__(self):
       return self.EmpireCommanders.name,self.EmpireHeroes.name,self.EmpireBasicTroops.name,self.EmpireSpecialTroops.name, self.EmpireSingularTroops.name
        
        
