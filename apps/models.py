from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    dloc=models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.deptno)
class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    sal=models.DecimalField(max_digits=10,decimal_places=2)
    comm=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    hiredate=models.DateField(auto_now_add=True)
    mgr=models.ForeignKey('self',models.SET_NULL,null=True,blank=True)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self):
        return self.ename
class SalGrade(models.Model):
    grade=models.DecimalField(max_digits=10,decimal_places=2)
    lsal=models.DecimalField(max_digits=10,decimal_places=2)

    hsal=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return str(self.grade)