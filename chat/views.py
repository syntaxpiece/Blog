from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth.models import User
# Create your views here.

@login_required
def chat_view(request, username=None):
    users = []
    receiver = None
    messages = []

    if request.user.is_superuser:
        users = User.objects.exclude(id=request.user.id)

        if username:
            receiver = User.objects.get(username=username)
            messages = Message.objects.filter(
                sender=request.user, receiver=receiver
            ) | Message.objects.filter(
                sender=receiver, receiver=request.user
            ).order_by('timestamp')

    else:
        try:
            receiver = User.objects.get(is_superuser=True)
        except User.DoesNotExist:
            receiver = None

        if receiver:
            messages = Message.objects.filter(
                sender=request.user, receiver=receiver
            ) | Message.objects.filter(
                sender=receiver, receiver=request.user
            ).order_by('timestamp')

    if request.method == 'POST' and receiver:
        content = request.POST['content']
        Message.objects.create(sender=request.user, receiver=receiver, content=content)
        return redirect('chat', username=receiver.username)

    return render(request, 'consultation.html', {
        'users': users,
        'receiver': receiver,
        'messages': messages
    })