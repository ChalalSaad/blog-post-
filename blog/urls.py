
from django.urls import path







from . import views 
from .views import  AddCreator, AddRecommandation, Commentanswer,  DeleteCreator, DeletePostView, DeleteRecommdation, DetailCreator, Detailpublication, PostBackend, UpdateCreator, UpdatePostView, UpdateRecommondation, backR, blog,ArticleDetailView,AddPostView, commant, comment_back,  custom_page_not_found, custom_server_error, ourCreator,   the_creator
from django.contrib.auth import views as auth_views

# my class with values from db


urlpatterns = [
    path('', views.index,name="index"),
    path('home', views.index,name="index"),
    path('contact', views.contact,name="contact"),
    # path('blog', blog.as_view(),name="blog"),
    path('blog', blog.as_view(),name="blog"),
   # this path make me to go to login page of django admin 
    path('login.mts.dj/', auth_views.LoginView.as_view(template_name='accounts/login.html',),name="login"),

    
    path('mypost', PostBackend.as_view(),name="mypost"),
    # if we click in post number 1 we will go with parmt(id=1 ) to show our post by hist id 
    path('detail/<int:pk>/', ArticleDetailView.as_view(),name="detail"),
    
    
    path('AddPost/', AddPostView.as_view(),name="addPost"),

    # path('AddCreator/', AddCreator.as_view(),name="addCreator"),

    
    
    path('UpdatePost/<int:pk>', UpdatePostView.as_view(),name="update"),
    
    
    # 
    path('DeletePost/<int:pk>/remove', DeletePostView.as_view(),name="delete"),
    # creator backend
    path('AddCreator/', AddCreator.as_view(),name="addCreator"),
    path('ourCreator/', ourCreator.as_view(),name="ourCreator"),
    path('DeleteCreator/<int:pk>/remove', DeleteCreator.as_view(),name="delete_creator"),
    path('UpdateCreator/<int:pk>', UpdateCreator.as_view(),name="update_creator"),
    # creator frontend
    path('creator', the_creator.as_view(),name="teem"),
    path('detailCreator/<int:pk>', DetailCreator.as_view(),name="detail_creator"),
#   comment
    path('detail/<int:pk>/comment', commant.as_view(),name="comment"),
    path('mypost/<int:pk>/commentBack', comment_back.as_view(),name="commentBack"),
    path('DeleteComment/<int:pk>/remove', views.delete_comment,name="delete_comment"),
# answer
    path('AddReponse/<int:pk>/change/', Commentanswer.as_view(),name="Post_answer"),
    
    


    # recommandation
    path('publication/<int:pk>', Detailpublication.as_view(),name="Detail-publication"),
    path('AddRecommandation/', AddRecommandation.as_view(),name="addRecommandation"),
    
    path('Publication/', backR.as_view(),name="manageRecommandation"),
    path('UpdateRecommandation/<int:pk>/change/', UpdateRecommondation.as_view(),name="updateRecommandation"),
    path('DeleteRecommandation/<int:pk>/change/', DeleteRecommdation.as_view(),name="deleteRecommandation"),
    # page 404 
    
    path("404/", custom_page_not_found),
    path("500/", custom_server_error),

]