from django.shortcuts import render
from .forms import BuyurtmaForm
import requests

BOT_TOKEN = "7279156416:AAED89ccV2IyC8HTlHg97CnYICPj3En_nM8"
telegram_send_message_api = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
CHAT_ID= -1002169865219

def buyurtma_olish(request):
    try:
        if request.method == 'POST':
            form=BuyurtmaForm(request.POST)
            if form.is_valid():
                form.save()
                user_data = form.cleaned_data
                message_text = f"<b>Assalomu aleykum</b> \nYangi buyurtma !\n👤 Buyurtmachi : {user_data['fullname']}\n📞 Telefon : {user_data['telefon_raqam']}\n⚠️ Xizmat turi :{user_data['hizmat_turi']}"
                if user_data.get("manzil", None):
                    message_text += f"\n📍 Manzil: {user_data['manzil']}"
                payload = {
                    'chat_id': CHAT_ID,
                    'text': message_text,
                    'parse_mode': 'HTML'
                }
                requests.post(telegram_send_message_api,data=payload)
                return render(request, 'success.html')
        else:
            form=BuyurtmaForm()
        return render(request , 'index.html',{'form':form})
    except ConnectionError:
        return render(request, 'success.html')
    except :
        pass

    
