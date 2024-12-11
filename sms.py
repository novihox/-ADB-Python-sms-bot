import os
import openpyxl

excel_file = 'numara.xlsx' 
wb = openpyxl.load_workbook(excel_file)
sheet = wb.active

def send_sms(phone_number, message):
    os.system(f'adb shell am start -a android.intent.action.VIEW -d "sms:{phone_number}"')
    os.system(f'adb shell input text "{message}"')
    os.system(f'adb shell input keyevent 66') 

for row in sheet.iter_rows(min_row=2, max_col=1, values_only=True):
    phone_number = row[0]
    if phone_number:
        send_sms(phone_number, "Merhaba! Bu bir test mesajıdır.")
        print(f"Mesaj gönderildi: {phone_number}")
