from django.urls import path
from .views import *

urlpatterns = [

    path('logout', user_logout ,name='user_logout'),
    path('my-application', my_application ,name='my_application'),
    path('', user_login ,name='user-login'),
    path('application-approval/<int:id>/<int:sts>', application_approval ,name='application_approval'),
    path('all-application', all_application ,name='all_application'),
    path('userprofile', user_profile , name='user_profile'),
    path('add-leaveform', add_leave_form ,name='add-leave-form'),
    path('todolist', to_do_list ,name='todolist'),
    path('todo-list-evaluation/<int:id>/<sts>', todo_list_evaluation ,name='todo-list-evaluation'),
    path('add-todo-list', add_todo_list ,name='add_todo_list'),
    path('add-employee', add_employee ,name='add_employee'),
    
    
    
]