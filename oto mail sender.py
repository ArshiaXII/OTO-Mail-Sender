import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import simpledialog, messagebox

def send_mail():
    mail_content = message_entry.get("1.0","end-1c")

    # Gönderen ve alıcı e-posta adresleri
    sender_address = sender_entry.get()
    receiver_address = receiver_entry.get()

    # Google account kimlik doğrulamaları
    username = sender_address
    password = password_entry.get()

    # E-Posta kurulumu
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject_entry.get() 
    message.attach(MIMEText(mail_content, 'plain'))

    # Session oluştur ve e-postayı gönder
    session = smtplib.SMTP('smtp.gmail.com', 587) 
    session.starttls()  # Güvenli bağlantı için gerekli

    session.login(username, password)  # Giriş yap
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

    messagebox.showinfo("Bilgi", 'Mail başarıyla gönderildi!')

root = tk.Tk()
root.title("E-posta Gönderme Arayüzü")

sender_label = tk.Label(root, text="Gönderenin E-posta Adresi:")
sender_label.pack()
sender_entry = tk.Entry(root)
sender_entry.pack()

password_label = tk.Label(root, text="Gönderenin Şifresi:")
password_label.pack()
password_entry = tk.Entry(root, show='*')
password_entry.pack()

receiver_label = tk.Label(root, text="Alıcının E-posta Adresi:")
receiver_label.pack()
receiver_entry = tk.Entry(root)
receiver_entry.pack()

subject_label = tk.Label(root, text="E-posta Konusu:")
subject_label.pack()
subject_entry = tk.Entry(root)
subject_entry.pack()

message_label = tk.Label(root, text="E-posta İçeriği:")
message_label.pack()
scrollbar = tk.Scrollbar(root) 
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
message_entry = tk.Text(root, height=10, yscrollcommand=scrollbar.set)
message_entry.pack()
scrollbar.config(command=message_entry.yview)

submit_button = tk.Button(root, text="E-Postayı Gönder", command=send_mail)
submit_button.pack()

root.mainloop()
