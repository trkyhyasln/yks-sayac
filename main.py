from datetime import datetime
import random
import pytz
import requests

# Türkiye saat dilimini ayarla
turkey_tz = pytz.timezone('Europe/Istanbul')
now = datetime.now(turkey_tz)
current_hour = now.hour

# 2027 YKS Geri Sayım Hesabı
target_date = datetime(2027, 6, 19, 10, 0, 0, tzinfo=turkey_tz)
remaining = target_date - now

days = remaining.days
hours = remaining.seconds // 3600
minutes = (remaining.seconds % 3600) // 60

yks_mesaji = f"YKS 2027 Kalan: {days} gun {hours} saat"

# Motivasyon cümlelerini motivasyon.txt dosyasından okuyoruz
try:
  with open("motivasyon.txt", "r", encoding="utf-8") as f:
    motivasyon_cumleleri = [
        line.strip() for line in f.readlines() if line.strip()
    ]
  secilen_motivasyon = random.choice(motivasyon_cumleleri)
except Exception as e:
  secilen_motivasyon = "Calismaya devam et."

# YKS Sayacının atılacağı saatler (07:00, 08:00, 13:00, 18:00)
yks_saatleri = [7, 8, 13, 18]

if current_hour in yks_saatleri:
  ham_mesaj = f"{yks_mesaji} - {secilen_motivasyon}"
else:
  ham_mesaj = f"{secilen_motivasyon}"

# CallMeBot için metni tam uyumlu formata getiriyoruz
encoded_text = requests.utils.quote(ham_mesaj)

phone = "905510050230"
apikey = "8937901"

# Doğrudan tarayıcıda tıkladığın formatın birebir aynısını Python ile oluşturuyoruz
url = f"https://api.callmebot.com/whatsapp.php?phone={phone}&text={encoded_text}&apikey={apikey}"

print("İstek atılan URL:", url)

response = requests.get(url)

print("CallMeBot Sunucu Yanıtı:", response.text)

if response.status_code == 200:
  print("İstek başarıyla iletildi.")
else:
  print("Bağlantı hatası, HTTP Kodu:", response.status_code)
  
