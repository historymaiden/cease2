from django.db import models

# Create your models here.

class Disease (models.Model):
    disease = models.CharField(max_length=50, unique=True)
    intro = models.CharField(max_length=200, blank=True)
    background = models.CharField(max_length=600, blank=True)
    image = models.CharField(max_length=100)
    scenario = models.CharField(max_length=5000)
    
    class Meta(object):
        ordering = ('disease', 'pk')
    
    def __unicode__(self):
        return U'%s | %s' %(self.pk, self.disease)

class Treatments (models.Model):
    treatmentID = models.CharField(max_length=50)
    disease = models.ForeignKey(Disease)
    lifeExpectancy = models.CharField(max_length=200)
    treatmentPlan = models.CharField(max_length=5000)
    lifeExtension = models.CharField(max_length=200, blank=True)
    choice = models.CharField(max_length=5000, blank=True)
    cost = models.CharField(null=False, max_length=5000)
    doctorVisits = models.CharField(null=False, max_length=5000)

    
    class Meta(object):
        ordering = ('treatmentID', 'treatmentPlan')
    
    def __unicode__(self):
        return self.treatmentID
    
    def save(self, *args, **kwargs):
        self.treatmentID
        super(Treatments, self).save(*args, **kwargs)

