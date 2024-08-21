from django.urls import path


from .views import post_list,post_detail,create_post,delete_post,update_post


app_name='posts'

urlpatterns = [

    path('',post_list,name='post_list'),
    path('create_post',create_post,name='create_post'),
    path('<slug:slug>',post_detail,name='post_detail'),
    path('update/<slug:slug>',update_post,name='update_post'),
    path('delete/<slug:slug>',delete_post,name='delete_post'),
    

    
]
