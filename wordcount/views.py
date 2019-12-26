import operator

from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse('Hello')
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()

    worddictionary = {}
    for word in words:
        if word in worddictionary:
            # Increase the number
            worddictionary[word] += 1
        else:
            # add to the dict
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(words),
                                          'worddictionary': worddictionary, 'sortedwords': sortedwords})
