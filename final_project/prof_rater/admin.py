from django.contrib import admin
from prof_rater.models import Department, Professor, Review, Course, WordCloud

# Register your models here.
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Professor)
admin.site.register(Review)
admin.site.register(WordCloud)
