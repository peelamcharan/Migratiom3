from django.db import models

# Create your models here.
class Dept(models.Model):
    dept_no=models.IntegerField(primary_key=True)
    dept_name=models.CharField(max_length=100)
    dept_loc=models.CharField(max_length=100)
    
    def _str_(self) -> str:
        return self.dept_name


class Emp(models.Model):
    emp_no=models.IntegerField(primary_key=True)
    emp_name=models.CharField(max_length=100)
    emp_sal=models.IntegerField
    dept_no=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def _str_(self) -> str:
        return self.emp_name
