from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm
from .forms import CommentForm
from django.shortcuts import get_object_or_404


def signup(request):
    if request.method == "POST":
        name = request.POST["name"]
        roll_number = request.POST["roll_number"]
        role = request.POST["role"]
        department = request.POST["department"]
        password = request.POST["password"]

        # Check if username already exists
        if User.objects.filter(username=roll_number).exists():
            messages.error(request, "Roll Number already registered.")
            return redirect("signup")

        # Create User
        user = User.objects.create_user(username=roll_number, password=password, first_name=name)
        user.save()

        # Create Profile
        UserProfile.objects.create(user=user, roll_number=roll_number, role=role, department=department)

        messages.success(request, "Registration successful! You can now log in.")
        return redirect("login")

    return render(request, "signup.html")


def user_login(request):
    if request.method == "POST":
        roll_number = request.POST["roll_number"]
        password = request.POST["password"]

        try:
            # Get the user associated with the roll number
            user_profile = UserProfile.objects.get(roll_number=roll_number)
            user = user_profile.user  # Get the related User instance

            # Authenticate the user
            user = authenticate(request, username=user.username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")  # Redirect to home page
            else:
                messages.error(request, "Invalid roll number or password")
        except UserProfile.DoesNotExist:
            messages.error(request, "Invalid roll number or password")

    return render(request, "login.html")

def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Assign the logged-in user
            post.save()
            return redirect('home')  # Redirect to home after submission
    else:
        form = PostForm()

    return render(request, 'post.html', {'form': form})

def base(request):
    return render(request, 'base.html')

@login_required
def home(request):
    if request.method == "POST":
        post_id = request.POST.get("post_id")
        text = request.POST.get("text")

        if post_id and text:
            post_instance = get_object_or_404(Post, id=post_id)
            comment = Comment.objects.create(user=request.user, post=post_instance, text=text)
            comment.save()

        return redirect("home")  # Redirect to home page after commenting

    posts = Post.objects.all()
    return render(request, "home.html", {"posts": posts})




