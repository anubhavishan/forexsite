from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests

def home(request):
    return render(request, 'forexapp/home.html')

def education(request):
    return render(request, 'forexapp/education.html')

def currency(request):
    return render(request, 'forexapp/currency.html')

def whatisforex(request):
    return render(request, 'forexapp/whatisforex.html')

def tools(request):
    amount = request.GET.get("amount")
    from_currency = request.GET.get("from_currency")
    to_currency = request.GET.get("to_currency")
    converted = None

    if amount and from_currency and to_currency:
        try:
            url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
            response = requests.get(url)
            data = response.json()
            rate = data["rates"].get(to_currency.upper())
            if rate:
                converted = round(float(amount) * rate, 2)
        except Exception:
            converted = "Error"

    return render(request, 'forexapp/tools.html', {
        "converted": converted,
        "amount": amount,
        "from_currency": from_currency,
        "to_currency": to_currency,
    })
