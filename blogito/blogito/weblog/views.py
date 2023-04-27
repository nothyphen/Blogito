from django.views import generic
from .models import Post, Comment, About, Contact, ContactUs
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .forms import CommentForm, ContactForm

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created')
    template_name = 'index.html'

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
        
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
    

def AboutMe(request):
        info = About.objects.all()[0].text
        instagram = Contact.objects.all()[0].instagram
        twitter = Contact.objects.all()[0].twitter
        linkdin = Contact.objects.all()[0].linkdin
        instagram_link = "https://instagram.com/"+instagram
        twitter_link = "https://twitter.com/"+twitter
        context = {
             'text' : info,
             'instagram' : instagram_link,
             'twitter' : twitter_link,
             'linkdin' : linkdin,
        }
        return render(request, 'about.html', context=context)


def ContactMe(request):
    template_name = 'contact.html'

    info = About.objects.all()[0].text
    instagram = Contact.objects.all()[0].instagram
    twitter = Contact.objects.all()[0].twitter
    linkdin = Contact.objects.all()[0].linkdin
    instagram_link = "https://instagram.com/"+instagram
    twitter_link = "https://twitter.com/"+twitter

    new_convertion = None
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            new_convertion = contact_form.save(commit=False)
            new_convertion.save()
    else:
        contact_form = ContactForm()
        
    return render(request, template_name, {
        'new_convertion' : new_convertion,
        'contact_form' : contact_form,
        'text' : info,
        'instagram' : instagram_link,
        'twitter' : twitter_link,
        'linkdin' : linkdin,
    })