from django.shortcuts import render, HttpResponse
def home(request):
    context = {

    }
    return render(request, 'index.html', context)

def count(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        comment = comment.strip().split(" ")
        print(comment)
        word_length = len(comment)
    context = {
        "len" : word_length,
    }
    return render(request, 'count.html', context)
