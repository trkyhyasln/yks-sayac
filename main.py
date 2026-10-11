from datetime import datetime, timedelta, timezone
import urllib.parse
import requests

# Türkiye saat dilimi (UTC+3)
tr_offset = timezone(timedelta(hours=3))
simdi = datetime.now(tr_offset)

# 2027 YKS Tarihi: 19 Haziran 2027, Saat 10:15
hedef = datetime(2027, 6, 19, 10, 15, 0, tzinfo=tr_offset)

fark = hedef - simdi
saniye = int(fark.total_seconds())

if saniye > 0:
  gun = saniye // 86400
  saat = (saniye % 86400) // 3600
  dakika = (saniye % 3600) // 60
  mesaj = (
      f'🎯 2027 YKS Geri Sayım:\n⏳ {gun} gün, {saat} saat,'
      f' {dakika} dakika kaldı! Hedefe tam gaz devam! 🚀'
  )
else:
  mesaj = '🎯 2027 YKS vakti geldi, başarılar dilerim!'

# Bilgilerin işlenmiştir
telefon = '+905510050230'
api_key = '8937901'

encoded_mesaj = urllib.parse.quote(mesaj)
url = f'https://api.callmebot.com/whatsapp.php?phone={telefon}&text={encoded_mesaj}&apikey={api_key}'

response = requests.get(url)
print(response.text)
