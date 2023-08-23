from django.db import models

class Record(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    Zipcode=models.CharField(max_length=20)

    def _str_(self):
        return(f"{self.first_name}){self.last_name}")

    


