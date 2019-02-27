def index(request):
    boards = board.objects.get(id)
    return render(request, index.html, {'boards':boards})