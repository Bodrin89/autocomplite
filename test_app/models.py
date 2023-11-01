from django.db import models

class City(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.name}"

class District(models.Model):
    name = models.CharField(max_length=255, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city')
    def __str__(self):
        return f"{self.name}"


class Address(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='address')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='address')
