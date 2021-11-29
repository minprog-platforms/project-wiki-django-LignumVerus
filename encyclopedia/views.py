from logging import error
from django.shortcuts import render
from django import forms
from markdown2 import Markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

class NewPageForm(forms.Form):
    title = forms.CharField(label="Give a title:", strip=True)
    text = forms.CharField(label="Enter your contents in Markdown:", 
                            strip=True,
                            widget=forms.Textarea)

def newpage(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get("title")
            text = form.cleaned_data.get("text")
            articles = util.list_entries()
            articles_lower = list(map(lambda article: article.lower(), articles))

            if title.lower() not in articles_lower:
                util.save_entry(title, text)
                return entrypage(request, title)
            else:
                error = "The page you are trying to create already exists!"
                return errorpage(request, error)

    return render(request, "encyclopedia/newpage.html", {
        "form": NewPageForm()
    })

def entrypage(request, article):
    try:
        raw_text = util.get_entry(article)
        markdowner = Markdown()

        text = markdowner.convert(raw_text)

        return render(request, "encyclopedia/entrypage.html", {
        "text": text
        })
    except:
        error = "The page you are trying to reach does not exist (yet!)"
        return errorpage(request, error)

def errorpage(request, error):
    return render(request, "encyclopedia/errorpage.html", {
        "errormessage": error
    })

def search(request):
    searched = request.POST.get("q")
    searched_lower = searched.lower()

    articles = util.list_entries()
    articles_lower = list(map(lambda article: article.lower(), articles))

    i = 0

    for article_lower in articles_lower:
        if str(searched_lower) == article_lower:
            return entrypage(request, articles[i])

        i += 1

    # else
    results = [article for article in articles if searched_lower in article.lower()]

    return render(request, "encyclopedia/search.html", {
        "results": results
    })
