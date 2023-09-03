from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile, Post
from .forms import ArticleForm

@login_required(login_url="signin")
def feed(request):
    user_object = User.objects.get(username=request.user.username)
    posts = Post.objects.all()
    try:
        user_profile = Profile.objects.get(user=user_object)
    except:
        return redirect("/signin")

    return render(
        request,
        "feed.html",
        {"user_profile": user_profile, "posts": posts},
    )


@login_required(login_url="signin")
def article(request, user, pk):
    user_object = User.objects.get(username=request.user.username)
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        post = None
        return redirect("/404")

    try:
        user_profile = Profile.objects.get(user=user_object)
    except Profile.DoesNotExist:
        return redirect("/signin")

    context = {
        "title": post.title,
        "description": post.description,
        "content": post.content,
        "cover_img": post.cover_img,
        "date": post.formatted_date,
        "min_read": post.min_read,
    }

    return render(request, "article.html", {"user_profile": user_profile, **context})


"""

class BlogPostCreateView(CreateView):
    model = Post
    fields = ["title", "description", "content", "cover_img" ]

"""


@login_required(login_url="signin")
def upload_page(request):
    user_object = User.objects.get(username=request.user.username)
    form = ArticleForm()
    try:
        user_profile = Profile.objects.get(user=user_object)
    except:
        return redirect("/signin")
    return render(request, "add.html", {"user_profile": user_profile, "form": form})


@login_required(login_url="signin")
def upload(request):
    if request.method == "POST":
        """
        form = BlogPostCreateView(request.POST)
        if form.is_valid():
            form.save()
        """
        user = request.user.username
        cover_img = request.FILES.get("image_upload")
        title = request.POST["title"]
        content = request.POST["content"]
        new_post = Post.objects.create(
            user=user, cover_img=cover_img, title=title, content=content
        )
        new_post.save()

        return redirect("/")
    return redirect("/")


@login_required(login_url="signin")
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    return render(request, "setting.html", {"user_profile": user_profile})


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect("signup")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect("signup")
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()

                # log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                # create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(
                    user=user_model, id_user=user_model.id
                )
                new_profile.save()
                return redirect("/")
        else:
            messages.info(request, "Password Not Matching")
            return redirect("signup")

    else:
        return render(request, "signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Credentials Invalid")
            return redirect("signin")

    else:
        return render(request, "signin.html")


@login_required(login_url="signin")
def logout(request):
    auth.logout(request)
    return redirect("signin")
