from django.db import models
class Crag(models.Model):
    cragName = models.CharField(max_length= 50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length= 2)

    def __str__(self):
        return (self.cragName)
class Wall(models.Model):
    wallName = models.CharField(max_length= 50)
    crag = models.ForeignKey(Crag, on_delete=models.CASCADE)

    def __str__(self):
        return (self.wallName)

class Route(models.Model):
    routeName = models.CharField(max_length= 50)
    comments = models.CharField(max_length=3000)
    description = models.CharField(max_length=100)
    wall = models.ForeignKey(Wall, on_delete=models.CASCADE)

    def __str__(self):
        return (self.routeName)