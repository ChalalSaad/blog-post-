
from audioop import reverse
from dataclasses import fields
from genericpath import commonprefix
from pyexpat import model
import django

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.test import RequestFactory
from django.urls import reverse_lazy
from requests import post
from .models import   Post, creator,Comment,User,publication
from .form import  styleAnswer, styleComment, styleCreator, stylePost,  styleRecommandation
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
# this import make me to list my database (cols, values)
from django.views.generic import ListView,DetailView,CreateView,UpdateView, DeleteView
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


def index(response): 
    return render(response,'index.html', {})


def contact(response): 
    return render(response, 'contact.html')

# def get_context_data(self, *args, **kwargs):
#     context = super(blog, self).get_context_data(*args, **kwargs)
#     cart_obj, new_obj = Post.objects.new_or_get(self. request)
#     context['cart'] = cart_obj
    
#     return context


class blog(ListView): 
    model=Post
    template_name='blog.html'
    # make last post in the top
    ordering=['-date_post']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pub=publication.objects.all().order_by('-date_recommandation')
        
        context['publication'] = pub
        return context


class PostBackend(ListView): 
    model=Post
    template_name='myPost.html'
    # make last post in the top
    ordering=['-date_post']


# detail of the post + comment of user
class ArticleDetailView(DetailView): 

    model=Post
    template_name='detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pub=publication.objects.all().order_by('-date_recommandation')
        context['publication'] = pub
        return context

    

# create post 
class AddPostView(SuccessMessageMixin,CreateView): 
    model=Post
    form_class=stylePost
    template_name='addPost.html'
    success_message = "Post Add successfully"


class UpdatePostView(SuccessMessageMixin,UpdateView): 
    model=Post   
    form_class=stylePost
    template_name="edit_post.html"
    success_message = "Post updated successfully"
    
# delete our post
class DeletePostView(SuccessMessageMixin,DeleteView): 
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('mypost')
    success_message = "Post deleted successfully"

# add creator profile
class AddCreator(SuccessMessageMixin,CreateView): 
    model=creator
    form_class=styleCreator
    template_name='addCreator.html'
    success_message = "Creator Add successfully"


# add  commant  by user  
class commant(CreateView): 
    model=Comment
    template_name='commant.html'
    form_class=styleComment
    def form_valid(self,form): 
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)
    def get_success_url(self):
        post_id = self.kwargs['pk']
        return reverse_lazy("detail", kwargs={"pk": post_id})
        
    

# craete post finale
# class postFinal(DetailView): 
#     model=Comment
#     form_class=stylePostFinal
#     template_name='postComment.html'
#     success_url=reverse_lazy('mypost')

# class postFinalfront(ListView): 
#     model=test
    
#     template_name='blog.html'
    


# manage comment backend
class comment_back(DetailView): 
    model=Post
    template_name='CommentsBack.html'

# # delete comments
# class DeleteComment(SuccessMessageMixin,DeleteView): 
#     model=Comment
#     template_name='delete_comment.html'
#     success_url=reverse_lazy('mypost')
#     success_message = "Comment deleted successfully"

def delete_comment(SuccessMessageMixin,pk):
    event=Comment.objects.get(pk=pk)
    event.delete()   
    
    return redirect('mypost')
    success_message = "Comment deleted successfully"   
   
   
        
   
        # post_id = self.kwargs['pk']
        # return reverse_lazy("detail", kwargs={"pk": post_id})


# # get pk of the comment
# class Commentanswer(DetailView): 
#     model=commant
#     template_name='answer.html'
# answer of coment
class Commentanswer(SuccessMessageMixin,UpdateView): 
    model=Comment
    form_class=styleAnswer
    template_name='answer.html'
    success_url=reverse_lazy('mypost')
    success_message = "Answer write with successfully"   

# list all the comments in every post l
class comment_back (DetailView): 
    model=Post
    template_name='CommentsBack.html'

    




# 
# detail of recomm
class Detailpublication(DetailView): 
    model=publication
    template_name='detailRecommandation.html'

################## back end ###################

# create recommandation backend
class AddRecommandation(SuccessMessageMixin,CreateView): 
    model=publication
    form_class=styleRecommandation
    template_name='addRecommandation.html'
    success_message = "Recommandation  Add successfully"
    
    success_url=reverse_lazy('manageRecommandation')
    # def get_success_url(self):
    #     post_id = self.kwargs['pk']
    #     return reverse_lazy("detail", kwargs={"pk": post_id})


# delete recommandation 
class DeleteRecommdation(SuccessMessageMixin,DeleteView): 
    model=publication
    template_name='delete_recommandation.html'
    success_url=reverse_lazy('manageRecommandation')
    success_message = "Recommandation deleted successfully"
    
# update recommandation 
class UpdateRecommondation(SuccessMessageMixin,UpdateView): 
    model=publication
    form_class=styleRecommandation
    template_name="edit_recommandation.html"
    success_url=reverse_lazy('manageRecommandation')
    success_message = "Recommandation updated successfully"  


# manage our reomm 
class backR(ListView): 
    model=publication
    template_name='ourRecommandation.html'
    ordering=['-date_recommandation']
    

    

# list our creator in backend
class ourCreator(ListView): 
    model=creator
    template_name='ourCreator.html'
    # make last post in the top
    ordering=['-date_join']

# delete our creator
class DeleteCreator(SuccessMessageMixin,DeleteView): 
    model=creator
    template_name='deleteCreator.html'
    success_url=reverse_lazy('ourCreator')
    success_message = "Creator deleted  successfully"

#update our creator
class UpdateCreator(SuccessMessageMixin,UpdateView): 
    model=creator  
    form_class=styleCreator
    template_name="editCreator.html"
    success_message = "Creator updated successfully"


# creator page frontend
class the_creator(ListView): 
    model=creator
    template_name='creator.html'    

# detail of creator
class DetailCreator(DetailView): 
    model=creator
    template_name='detailCreator.html'



def custom_page_not_found(request):
    return django.views.defaults.page_not_found(request, None)

def custom_server_error(request):
    return django.views.defaults.server_error(request)
