from django.http import HttpResponse
from django.shortcuts import render
import string
# def index(request) :
#     return HttpResponse('''Hello Paridhi !!<br> <a href ="https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2"> Striver A2Z Sheet</a>''')

# def about(request):
#     return HttpResponse('''<h1> Hello Everyone!! </h1><br> <a href="https://leetcode.com/u/paridhij309/"> This is my leetcode profile</a>''')

def index(request):
    return render(request, "index.html")

def analyze(request):
    #Fetching text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', "off")
    upper = request.POST.get('upper', "off")
    lower = request.POST.get("lower", "off")
    newlineremover = request.POST.get('newlineremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    analyzed =djtext
    purpose_list =[]
    #Analyzing text
    # Removing punctuations 
    # punctuations = '''.,;:?!'\"‘’“”()[]{}<>-–—…/\\|+_@#&*%'''
    if removepunc == "on":
        temp=""
        for char in djtext:
            if char not in string.punctuations:
                temp += char
        analyzed = temp
        purpose_list.append('Remove Punctuations')
    # upper case
    if upper == "on":
        analyzed = analyzed.upper()
        purpose_list.append('Upper Case')
    # lower case
    if lower == "on":
        analyzed = analyzed.lower()
        purpose_list.append('Lower Case')

    #new line remover
    if newlineremover == "on":
        temp=""
        for char in analyzed:
            if(char != "\n"):
                temp += char      
        analyzed = temp
        purpose_list.append('New Line Remover')
    
    # char count
    char_cnt = None
    if charcount =='on':
        cnt = 0
        for char in analyzed:
            if char.isalnum() or char in string.punctuation:
                cnt += 1
        char_cnt = cnt
        purpose_list.append('Count Characters')

    if not purpose_list:  
        return HttpResponse("Error ! Please select an opeartion")

    params = {'analyzed_text':analyzed, 'purpose':', '.join(purpose_list), 'char_cnt':char_cnt}
    return render(request, 'analyze.html', params)


def features(request):
    return render(request, "features.html")

def contact(request):
    return render(request, "contact.html")