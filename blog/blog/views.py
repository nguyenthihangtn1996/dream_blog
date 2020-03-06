from django.shortcuts import render
from .models import Post
from maketing.models import Signup
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    queryset = Post.objects.filter(feature=True)
    latest = Post.objects.order_by('-timestamp')[0:3]

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'object_list' : queryset,
        'latest': latest
    }
    return render(request, 'index.html', context )

def blog(request):
    queryset = Post.objects.all()
    paginator = Paginator(queryset, 4)
    page_request_var = 'page'
    recently = Post.objects.order_by('-timestamp')[0:3]

    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'object_list' : paginated_queryset,
        'page_request_var' : page_request_var,
        'recently': recently
    }
    return render(request, 'blog.html', context)

def post(request, id):

    return render(request, 'post.html', {})