from django.contrib import admin

from blog.models import TaskChanging
from blog.models.task import Task
from blog.models.notifications import Notification
from blog.models.task_log import Task_log

from blog.models.user_backup import User_backup
from blog.models.user_login_his import User_login_his
from blog.models.user_profile_his import User_profile_his


class TaskAdm(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'author', 'status', 'start_date', 'end_date')
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name',)
    list_filter = ('status',)
    list_editable = ('status',)
    list_per_page = 10
    list_max_show_all = 100
    fields = ('name', 'description', 'author', 'status', 'start_date', 'end_date')
    readonly_fields = ('id', 'start_date',)


class TaskChangingAdm(admin.ModelAdmin):
    list_display = ('id', 'task', 'prevstatus', 'currentstatus', 'log_date',)
    list_display_links = ('id', 'task',)
    list_per_page = 10
    list_max_show_all = 100
    fields = ('task', 'prevstatus', 'currentstatus', 'log_date',)
    readonly_fields = ('id', 'task', 'prevstatus', 'currentstatus', 'log_date',)


class Task_logAdm(admin.ModelAdmin):
    list_display = ('id', 'action', 'task', 'datetime', 'last_status',)
    list_display_links = ('id', 'action',)
    list_per_page = (10)
    list_max_show_all = (100)
    fields = ('action', 'task', 'datetime', 'last_status',)
    readonly_fields = ('id', 'action', 'task', 'datetime', 'last_status',)


class Backup_Adm(admin.ModelAdmin):
    list_display = ('log_id', 'user_id', 'username', 'date_joined', 'deleted_at',)
    list_display_links = ('log_id', 'user_id',)
    list_per_page = (10)
    list_max_show_all = (100)
    fields = ('user_id', 'username', 'date_joined', 'deleted_at',)
    readonly_fields = ('log_id', 'user_id', 'username', 'date_joined', 'deleted_at',)


class Login_hisAdm(admin.ModelAdmin):
    list_display = ('log_id', 'user_id', 'logged_at', 'was_active', 'username',)
    list_display_links = ('log_id', 'user_id',)
    list_per_page = (10)
    list_max_show_all = (100)
    fields = ('user_id', 'logged_at', 'was_active', 'username',)
    readonly_fields = ('log_id', 'user_id', 'logged_at', 'was_active', 'username',)


class Profile_hisAdm(admin.ModelAdmin):
    list_display = (
        'log_id', 'log_date', 'user_id', 'old_password', 'new_password', 'first_name', 'last_name', 'old_email',
        'new_email',
        'username',)
    list_display_links = ('log_id', 'user_id',)
    list_per_page = (10)
    list_max_show_all = (100)
    fields = (
        'log_date', 'user_id', 'old_password', 'new_password', 'first_name', 'last_name', 'old_email', 'new_email',
        'username',)
    readonly_fields = (
        'log_id', 'log_date', 'user_id', 'old_password', 'new_password', 'first_name', 'last_name', 'old_email',
        'new_email', 'username',)


admin.site.register(Task, TaskAdm)
admin.site.register(TaskChanging, TaskChangingAdm)
admin.site.register(Notification)
admin.site.register(Task_log, Task_logAdm)

admin.site.register(User_backup, Backup_Adm)
admin.site.register(User_login_his, Login_hisAdm)
admin.site.register(User_profile_his, Profile_hisAdm)
