import openai
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

openai.api_key = settings.OPENAI_API_KEY

@csrf_exempt
def forex_chatbot(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")

        if not user_message:
            return JsonResponse({"reply": "Please enter a message."})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",   # You can use gpt-3.5-turbo if needed
                messages=[
                    {"role": "system", "content": "You are a helpful Forex trading assistant."},
                    {"role": "user", "content": user_message}
                ]
            )
            reply = response.choices[0].message["content"].strip()
        except Exception as e:
            reply = f"Error from OpenAI: {str(e)}"

        return JsonResponse({"reply": reply})




# views.py (add this below the API view)
from django.shortcuts import render

def chat_page(request):
    return render(request, "chatbot/chat.html")
