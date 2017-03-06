from django.db import models
from django.db.models.fields import CharField, SlugField
from docx import Document

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length =100)
    auteur = models.CharField(max_length =100)
    contenu = models.TextField(max_length =100)
    date = models.DateTimeField(auto_now_add=True, verbose_name = "Date of creation")
    slug = models.SlugField(max_length =100)
    categorie = models.ForeignKey('Categorie')
    
    def __str__(self):
        return self.titre +" par " +self.auteur
    
class Categorie(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to = 'pictures')
    
    class Meta:
        db_table = "profile"
        
        
        
class Login(models.Model):
    username = models.CharField(max_length =100)
    password = models.CharField(max_length =100)
        
    def __str__(self):
        return self.username
    

# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return 'user_{0}/{1}'.format(instance.lastname.id, filename)

class SubmitDoc(models.Model):
    Student = 'stu'
    Professional = 'Pro'
    
    Status_CHOICES = (
        (Student, 'Stu'),
        (Professional, 'Pro'),
       
    )
    
    firstName = models.CharField(max_length =100)
    lastName = models.CharField(max_length =100)
    email = models.EmailField()
    Stud_status = models.CharField(
        max_length=3,
        choices=Status_CHOICES,
        default=Student,
    )
    uploadDoc = models.FileField(upload_to='documents/%Y/%m/%d/')   
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    paid = models.BooleanField(default=False)
    finished_read = models.BooleanField(default=False)
    read_by = models.CharField(max_length = 100, default="none")
    
  
#     def obtain_text(self):
#         compteur =0
#         with open(self.uploadDoc) as data:
#             document = Document(data)
#             for para in document.paragraphs:
#                 content = para.text
#                 countage= len(content.split()) 
#                 compteur=countage + compteur
#             
#             return compteur
    
    