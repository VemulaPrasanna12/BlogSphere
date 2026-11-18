from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.text import slugify

from .forms import AdminLoginForm, PostForm
from .models import Post


def home(request):
    paginator = Paginator(Post.objects.all(), 6)
    page_obj = paginator.get_page(request.GET.get('page', 1))
    return render(request, 'home.html', {'posts': page_obj, 'page_obj': page_obj})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})


def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('dashboard')
    form = AdminLoginForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        if user.is_staff:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('dashboard')
        form.add_error(None, 'Only staff accounts can access the dashboard.')
    return render(request, 'admin_login.html', {'form': form})


def admin_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


staff_required = user_passes_test(
    lambda user: user.is_authenticated and user.is_staff,
    login_url='/admin-login/',
)


@staff_required
def dashboard(request):
    return render(request, 'dashboard.html', {'posts': Post.objects.all()})


def _save_post_form(request, form, action, post=None):
    if request.method == 'POST' and form.is_valid():
        saved_post = form.save(commit=False)
        if not saved_post.slug:
            base_slug = slugify(saved_post.title) or 'post'
            candidate = base_slug
            suffix = 2
            while Post.objects.filter(slug=candidate).exclude(pk=saved_post.pk).exists():
                candidate = f'{base_slug}-{suffix}'
                suffix += 1
            saved_post.slug = candidate
        saved_post.save()
        verb = 'updated' if post else 'published'
        messages.success(request, f'Post "{saved_post.title}" {verb}.')
        return redirect('dashboard')
    return render(request, 'post_form.html', {'form': form, 'action': action})


@staff_required
def post_new(request):
    form = PostForm(request.POST or None, request.FILES or None)
    return _save_post_form(request, form, 'New Post')


@staff_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    return _save_post_form(request, form, 'Edit Post', post)


@staff_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted.')
        return redirect('dashboard')
    return render(request, 'post_confirm_delete.html', {'post': post})
