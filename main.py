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

yks_mesaji = (
    f"⏳ *2027 YKS Geri Sayım*:\nKalan Süre: {days} gün, {hours} saat,"
    f" {minutes} dakika"
)

# Motivasyon cümlelerini harici motivasyon.txt dosyasından okuyoruz
try:
  with open("motivasyon.txt", "r", encoding="utf-8") as f:
    # Boş satırları filtreleyerek listeye atıyoruz
    motivasyon_cumleleri = [
        line.strip() for line in f.readlines() if line.strip()
    ]
  secilen_motivasyon = random.choice(motivasyon_cumleleri)
except Exception as e:
  secilen_motivasyon = (
      "Motivasyon dosyası okunamadı ama sen yine de çalış!"
  )
  print("Dosya okuma hatası:", e)

# YKS Sayacının atılacağı saatler (07:00, 08:00, 13:00, 18:00)
yks_saatleri = [7, 8, 13, 18]

if current_hour in yks_saatleri:
  mesaj = f"{yks_mesaji}\n\n{secilen_motivasyon}"
  print(f"YKS Sayacı + Motivasyon gönderiliyor (Saat: {current_hour}:00)...")
else:
  mesaj = f"{secilen_motivasyon}"
  print(f"Sadece Motivasyon gönderiliyor (Saat: {current_hour}:00)...")

# CallMeBot WhatsApp API
phone = "5510050230"
apikey = "8937901"
url = f"https://api.callmebot.com/whatsapp.php?phone={phone}&text={requests.utils.quote(mesaj)}&apikey={apikey}"

response = requests.get(url)

print("CallMeBot Sunucu Yanıtı:", response.text)

if response.status_code == 200:
  print("İstek sunucuya başarıyla iletildi.")
else:
  print("Bağlantı hatası oluştu, HTTP Kodu:", response.status_code)
    
