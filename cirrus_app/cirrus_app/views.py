from django.shortcuts import render


def index(request):
    payload = request.GET.get("payload", "")
    return render(request, "index.html", {"payload": payload})