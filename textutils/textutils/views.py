from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analysetext(request):
    c = 0
    analysed_text=''
    if request.method == "POST":
        djtext = request.POST.get('text', '')

        if not djtext:
            return HttpResponse("Error: No text provided!") 

        action = request.POST.get('action', '')

        if action == "removepunc":
        	
        	char1 = "!#$%&\"'()*+,-./:;<=>?@[\]^_`{|}~"
        	for char in djtext:
        		if char not in char1:
        			analysed_text=analysed_text+char
        	c = len(analysed_text)
        	return render(request, 'analyse.html', {'original_text': djtext, 'analysed_text': analysed_text, 'character': c})

        elif action == "upper":
            analysed_text = djtext.upper()
            c = len(analysed_text)  
            return render(request, 'analyse.html', {'original_text': djtext, 'analysed_text': analysed_text, 'character': c})
        elif action == "lower":
            analysed_text = djtext.lower()
            c = len(analysed_text)  
            return render(request, 'analyse.html', {'original_text': djtext, 'analysed_text': analysed_text, 'character': c})
        elif action == "spaces":
        	for char in djtext:
        		if char!=' ':
        			analysed_text=analysed_text+char
        	c = len(analysed_text)
        	return render(request, 'analyse.html', {'original_text': djtext, 'analysed_text': analysed_text, 'character': c})
        elif action == "title":
        	analysed_text = djtext.title()
        	c = len(analysed_text)
        	return render(request, 'analyse.html', {'original_text': djtext, 'analysed_text': analysed_text, 'character': c})
        elif action=="clear":
        	c = len(analysed_text)
        	return render(request, 'analyse.html', {'original_text':"", 'analysed_text': analysed_text, 'character': c})
        	
    return render(request, 'analyse.html')

            

