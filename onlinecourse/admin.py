from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Choice, Question

# <HINT> Register QuestionInline and ChoiceInline classes here

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    inlines = [ChoiceInline]

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    inlines = [QuestionInline]
    
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['question_text']
    

class ChoiceAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['choice_text']

# <HINT> Register Question and Choice models here
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question)
admin.site.register(Choice)