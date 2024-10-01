from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
def analyze(request):
    # Get the text from the request
    jangotext = request.GET.get('text', 'default')
    
    # Get the checkbox options
    removepunc = request.GET.get('removepunc', 'off')
    captalize = request.GET.get('captalize', 'off')  # Check for capitalize

    # Initialize an empty string for the analyzed text
    analyzed = ""

    print(f"Original Text: {jangotext}")
    print(f"Remove Punctuation: {removepunc}")
    print(f"Capitalize: {captalize}")

    # If remove punctuation option is selected
    if removepunc == "on":
        punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in jangotext:
            if char not in punctuation:
                analyzed += char
        jangotext = analyzed  # Update text after removing punctuation
        purpose = "Removed Punctuations"

    # If capitalize option is selected
    if captalize == "on":
        analyzed = jangotext.upper()  # Convert to uppercase
        purpose = "Capitalized Text"

    # If no action is selected, return the original text
    if removepunc != "on" and captalize != "on":
        analyzed = jangotext
        purpose = "No changes made"

    # Prepare context for rendering the template
    params = {"purpose": purpose, "analyzed_text": analyzed}

    # Render the template with the processed text
    return render(request, 'analyze.html', params)