from dataclasses import fields
from django import forms


from .models import  Post, creator,Comment,publication
# this class make us to do same style in my add_post

class stylePost(forms.ModelForm): 
     class Meta: 
         model=Post
         fields=('titre', 'typeContenu', 'creator', 'contenu','image_post')
        #  css
         widgets={
          'titre': forms.TextInput(attrs={'class': 'form-control' ,'placeholder':'Le titre ' }),
          'typeContenu': forms.TextInput(attrs={'class': 'form-control','placeholder':'Le type'}),
          'creator': forms.TextInput(attrs={'class': 'form-control','placeholder':'Le Créateur'}),
          'contenu': forms.Textarea(attrs={'class': 'form-control','placeholder':'Le Contenu'}),
          
        }

class styleCreator(forms.ModelForm): 
     class Meta: 
         model=creator
         fields=('fullname', 'profile','image_creator', 'skill')
        #  css
         widgets={
           'color': '#000',
          'fullname': forms.TextInput(attrs={'class': 'form-control' ,'placeholder':'Le titre ' }),
          'skill': forms.TextInput(attrs={'class': 'form-control' ,'placeholder':'Le titre ' }),
          'profile': forms.Textarea(attrs={'class': 'form-control','placeholder':'Le type'}),
          
          
        }
class styleComment(forms.ModelForm): 
     class Meta: 
         model=Comment
         fields=('fullname', 'gmail','comment')
        #  css
         widgets={
          'fullname': forms.TextInput(attrs={'class' : 'fieldWrapper','placeholder':'fullname' }),
          'gmail': forms.TextInput(attrs={'class' : 'fieldWrapper' ,'placeholder':'gmail' }),
          'comment': forms.Textarea(attrs={'class' : 'fieldWrapper','placeholder':'comment'}),
          
          
        }
class styleRecommandation(forms.ModelForm): 
     class Meta: 
         model=publication
         fields=('title', 'content','image_recommandation','link')
        #  css
         widgets={
          'title': forms.TextInput(attrs={'class': 'form-control' ,'placeholder':' ' }),
          'content': forms.Textarea(attrs={'class': 'form-control' ,'placeholder':' ' }),
          'link': forms.TextInput(attrs={'class': 'form-control' ,'placeholder':' ' }),
          
          
          
        }

# style of answer template 
class styleAnswer(forms.ModelForm): 
     class Meta: 
         model=Comment
         fields=('response',)
        #  css
         widgets={

          'response': forms.Textarea(attrs={'class' : 'form-control','placeholder':'answer' }),
          
          
          
        }




# class stylePostFinal(forms.ModelForm): 
#      class Meta: 
#          model=Comment
#          fields=('fullname','comment','response')
#         #  css
#          widgets={
#           'fullname': forms.TextInput(attrs={'class' : 'form-control','placeholder':'answer' }),
#           'comment': forms.TextInput(attrs={'class' : 'form-control','placeholder':'answer' }),  
#           'response': forms.TextInput(attrs={'class' : 'form-control','placeholder':'answer' }),
          
          
          
#         }