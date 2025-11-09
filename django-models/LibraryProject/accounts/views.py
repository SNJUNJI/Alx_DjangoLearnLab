from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required

def admin_required(user):
    return hasattr(user, 'profile') and user.profile.role == 'Admin'

def librarian_required(user):
    return hasattr(user, 'profile') and user.profile.role == 'Librarian'

def member_required(user):
    return hasattr(user, 'profile') and user.profile.role == 'Member'

@login_required
@user_passes_test(admin_required)
def admin_view(request):
    return render(request, 'admin_view.html', {'user': request.user})

@login_required
@user_passes_test(librarian_required)
def librarian_view(request):
    return render(request, 'librarian_view.html', {'user': request.user})

@login_required
@user_passes_test(member_required)
def member_view(request):
    return render(request, 'member_view.html', {'user': request.user})
