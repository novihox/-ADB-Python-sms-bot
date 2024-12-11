# -ADB-Python-sms-bot

Bu yöntem, bilgisayarınızın Android telefonunuza bağlanarak SMS göndermesine olanak tanır.

Gereksinimler:
Android cihazınızda "Developer Options" (Geliştirici Seçenekleri) etkinleştirilmiş olmalı.
ADB yüklü olmalı. (requirements.txt)

adb shell am start -a android.intent.action.VIEW -d "sms:{phone_number}": Bu komut, telefonun SMS uygulamasını açar.
adb shell input text "{message}": Mesajı yazdırır.
adb shell input keyevent 66: Mesajı gönderir.
Bu yöntem, Android telefonunuzda geliştirici seçeneklerinin ve USB hata ayıklamanın açık olması gerektiğini unutmayın.

Excel Dosyasının Yapısı:
Bu örnek, telefon numaralarının 1. sütunda yer aldığı varsayımıyla yazıldı. Eğer telefon numaralarınız farklı bir sütunda yer alıyorsa, max_col=1 parametresini uygun sütun numarasıyla değiştirmeniz gerekir. Örneğin, telefon numaraları 2. sütunda ise, max_col=2 şeklinde değiştirirsiniz.

Telefonunuzu usb yardımıyla bilgisayarınıza bağlayın ve 
# python sms.py

çalıştırmasını yapın
