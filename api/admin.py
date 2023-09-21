from django.contrib import admin
from django.contrib.auth.models import User, Group
from . import models
from rangefilter.filters import DateRangeFilterBuilder

admin.site.unregister(User)
admin.site.unregister(Group)

# CREATE STUDET ADMIN AND VIEW LOGIN SIGNUO ---> THEN THE HOMWORK

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'review', 'level', 'is_paied', 'renew_date',)
    list_editable = ('is_paied', 'review', 'renew_date',)
    list_filter = (
        ("renew_date", DateRangeFilterBuilder()),
        'is_paied'
    )
    search_fields = ('phone',)

admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.Level)




class QInlines(admin.TabularInline):
    model = models.Question
    extra = 2

class AInlines(admin.TabularInline):
    model = models.Answer
    extra = 2

class HomeWrokAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'level', 'publish', 'date',)

    list_filter = ('level',)

    inlines = [QInlines, AInlines]

admin.site.register(models.HomeWork, HomeWrokAdmin)



class AnsweredQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'homework', 'question', 'is_correct', 'review', 'date',)
    search_fields = ('student__phone',)
    list_filter = ('homework',)

admin.site.register(models.AnsweredQuestion, AnsweredQuestionAdmin)




class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'level', 'date',)


admin.site.register(models.Lesson, LessonAdmin)


class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'level', 'date',)


admin.site.register(models.Media, MediaAdmin)