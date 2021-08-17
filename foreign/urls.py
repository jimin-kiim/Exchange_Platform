from django.urls import path
from . import views

app_name = 'foreign'

urlpatterns = [
    path('univ_list', views.univ_list, name='univ_list'),
    path('univ_search', views.univ_search, name='univ_search'),

    path('wiki/<int:pk>', views.wiki, name='wiki'),
    path('wiki/<str:wiki_type>/<int:pk>',
         views.wiki_detail, name='wiki_detail'),

    path('<int:foreign_id>/review/list', views.review_list, name="review_list"),
    path('<int:foreign_id>/review/create',
         views.review_create, name="review_create"),
    path('<int:foreign_id>/review/delete/<int:pk>/',
         views.review_delete, name="review_delete"),
    path('<int:foreign_id>/review/detail/<int:pk>/',
         views.review_detail, name="review_detail"),
    path('<int:foreign_id>/review/update/<int:pk>/',
         views.review_update, name="review_update"),

    path('<int:foreign_id>/question/', views.question_list, name='question_list'),
    path('<int:foreign_id>/question/<int:pk>/',
         views.question_detail, name='question_detail'),
    path('<int:foreign_id>/question/create/',
         views.question_create, name='question_create'),
    path('<int:foreign_id>/question/<int:pk>/edit/',
         views.question_edit, name='question_edit'),
    path('<int:foreign_id>/question/<int:pk>/delete/',
         views.question_delete, name='question_delete'),
    path('<int:foreign_id>/question/<int:pk>/comment_create/',
         views.q_comment_create, name='q_comment_create'),
    path('<int:foreign_id>/question/<int:pk>/comment_update/',
         views.q_comment_edit, name='q_comment_edit'),
    path('<int:foreign_id>/question/<int:pk>/comment_delete/',
         views.q_comment_delete, name='q_comment_delete'),
    path('<int:foreign_id>/question/search/',
         views.question_search, name='question_search'),
    path('<int:foreign_id>/question/<int:pk>/undercomment_create/',
         views.undercomment_create, name='undercomment_create'),
    path('<int:foreign_id>/question/<int:pk>/undercomment_update/',
         views.undercomment_update, name='undercomment_update'),
    path('<int:foreign_id>/question/<int:pk>/undercomment_delete/',
         views.undercomment_delete, name='undercomment_delete'),

    path('<int:foreign_id>/review/detail/<int:pk>/comment_create/',
         views.comment_create, name="comment_create"),
    path('<int:foreign_id>/review/detail/<int:pk>/comment_update/',
         views.comment_update, name="comment_update"),
    path('<int:foreign_id>/review/detail/<int:pk>/comment_delete/',
         views.comment_delete, name="comment_delete"),
    path('<int:foreign_id>/review/detail/<int:pk>/recomment_create/',
         views.Rrecomment_create, name="Rrecomment_create"),
    path('<int:foreign_id>/review/detail/<int:pk>/recomment_update/',
         views.Rrecomment_update, name="Rrecomment_update"),
    path('<int:foreign_id>/review/detail/<int:pk>/recomment_delete/',
         views.Rrecomment_delete, name="Rrecomment_delete"),


    path('<int:foreign_id>/sister/',
         views.sister, name="sister"),
    path('<int:foreign_id>/create_sister/',
         views.create_sister, name="create_sister"),
]
