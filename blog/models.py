from audioop import reverse
from distutils.command.upload import upload
from email.policy import default
from enum   import auto


from django.urls import reverse
from django.db import IntegrityError, models
# her to connect my app with auth django
from django.contrib.auth.models import User
from datetime import date,datetime
# package to body editor
from ckeditor.fields import RichTextField


# Create your models here.

class Post(models.Model): 
    titre=models.CharField(max_length=200)
    typeContenu=models.CharField(max_length=200)
    # i make autour foreingkey (if admin user del all the post will be deleted)
    # creator=models.ForeignKey(User, on_delete=models.CASCADE)
    creator=models.CharField(max_length=200)
    # contenu=models.TextField()
    contenu=RichTextField(null=True, blank=True)
    date_post=models.DateField(auto_now_add=True)
    image_post=models.ImageField(null=True, blank=True, upload_to="images/")
    body = models.TextField(default='add you commant her !')

# function of post 
    def my_PRF_image(self):
     if self.image_post :
        return (self.image_post.url)
     return ''

    def __str__(self):
        return self.titre + ' | ' +str(self.creator)

    # create this func to post button 
    def get_absolute_url(self): 
        return reverse('mypost')

# models creator 
class creator(models.Model): 
    fullname=models.CharField(max_length=200)
    skill=models.CharField(max_length=200, default='Cyber Security')
    profile=RichTextField(null=True, blank=True)
    image_creator=models.ImageField(null=True, blank=True, upload_to="images/")
    date_join=models.DateField(auto_now_add=True)

# funtion of creator 
    def my_PRF_image(self): 
        if self.image_creator: 
            return (self.image_creator.url)
        return ''  

    def __str__(self) : 
        return self.fullname 
        
    

    def get_absolute_url(self): 
        return reverse('ourCreator')
# comment
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    fullname=models.CharField(max_length=200)
    gmail=models.CharField(max_length=200)
    comment=models.TextField(max_length=100)
    date_comment=models.DateTimeField(auto_now_add=True)
    response=models.TextField(default='Wait ....') 
    def get_comment(self):
        return self.comment.all().count()
    # def get_absolute_url(self): 
    #     return reverse('detail',kwargs={'pk': self.pk})    
    
    def __str__(self): 
        return self.fullname

    


# comment finale
class publication(models.Model):
    title=models.CharField(max_length=200)
    link=models.CharField(max_length=200, default='link')
    content=RichTextField(null=True, blank=True)
    image_recommandation=models.ImageField(null=True, blank=True, upload_to="images/")
    date_recommandation=models.DateField(auto_now_add=True)

    def __str__(self) : 
        return self.title
    
    def my_PRF_image(self):
        if self.image_recommandation :
           return (self.image_recommandation.url)
        return ''

    def get_absolute_url(self):
        return reverse('ourRecommandation')
        
 
        