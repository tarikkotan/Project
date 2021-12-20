from django.db import models

# Create your models here.
class Poll(models.Model):
   
    option_one = models.CharField(max_length=300)
    option_two = models.CharField(max_length=300)
    option_three = models.CharField(max_length=300)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    
    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count
    
    def mostSelected(self):
        if self.option_one_count > self.option_two_count and  self.option_one_count > self.option_three_count:
            return self.option_one
        elif self.option_two_count > self.option_one_count and self.option_two_count > self.option_three_count:
            return self.option_two
        else:
            return self.option_three
        
    def choices(self):
        #pk'nın alıcağı değer birer birer artmalı ta ki en sonuncu index değerine ulaşana kadar.
        return  Poll.objects.get(pk=19).mostSelected()  
            
            
            

            
    