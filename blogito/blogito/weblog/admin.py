from django.contrib import admin
from .models import Post, Comment, About, Contact, ContactUs

# Register your models here.
class CommentAdminInLine(admin.TabularInline):
    model = Comment
    fields = ['text', 'date']
    extra = 0

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'status','created')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentAdminInLine]

class PostComment(admin.ModelAdmin):
    list_display = ['id', 'text', 'post']

class abouttext(admin.ModelAdmin):
    list_display = ['id', 'text']

class contacttext(admin.ModelAdmin):
    list_display = ['id', 'instagram', 'twitter', 'linkdin']

class ContactUsText(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    
admin.site.register(Comment, PostComment)
admin.site.register(Post, PostAdmin)
admin.site.register(About, abouttext)
admin.site.register(Contact, contacttext)
admin.site.register(ContactUs, ContactUsText)