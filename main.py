#importa bibliotecile necesare
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import tkinter as tk


def update():
    global adresa_mail, parola_mail
    adresa_mail = adresa_entry.get()
    parola_mail = parola_entry.get()
    # afisam valorile din variabile
    print(adresa_mail, parola_mail)
    root.destroy()

# creăm fereastra
root = tk.Tk()
root.geometry("400x200")

# adăugăm un label pentru adresa de email
adresa_label = tk.Label(root, text="Adresa de email:")
adresa_label.pack()
# adăugăm un câmp de introducere a textului pentru adresa de email
adresa_entry = tk.Entry(root, width = 30)
adresa_entry.pack()

# adăugăm un label pentru parola
parola_label = tk.Label(root, text="Parola:")
parola_label.pack()
# adăugăm un câmp de introducere a textului pentru parola
parola_entry = tk.Entry(root, show="*", width = 30)
parola_entry.pack()

# adăugăm butonul de update
update_button = tk.Button(root, text="Update", command=update)
update_button.pack()


# pornim interfața grafică
root.mainloop()

print(parola_entry)


# deschide un browser Chrome
driver = webdriver.Chrome()
driver.get("https://www.olx.ro/")
driver.implicitly_wait(2)


#accepta politica de cookies
confirm = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
confirm.click()
driver.implicitly_wait(2)

#acceseaza pagina de login
account_link = driver.find_element(By.CLASS_NAME, "link.inlblk")
account_text = account_link.find_element(By.XPATH, "./strong[text()='Contul tău']")
account_text.click()
driver.implicitly_wait(2)

#introducerea credentialelor
username_box = driver.find_element(By.NAME, "username")
username_box.send_keys(adresa_mail)
pass_box = driver.find_element(By.NAME, "password")
pass_box.send_keys(parola_mail)
driver.implicitly_wait(20)

#intra in cont
account_link = driver.find_element(By.CLASS_NAME, "css-2tejtz")
account_text = account_link.find_element(By.XPATH, "./div[text()='Intră în cont']")
account_text.click()
driver.implicitly_wait(30)


#cautare element
count = 0
while count < 3:
    try:
        edit_button = driver.find_element(By.CSS_SELECTOR, "li.css-hh9o2s a.css-1gxnzjw")
        edit_button.click()
        driver.implicitly_wait(2)
        modifica = driver.find_element(By.CLASS_NAME, "css-1anknvg")
        modifica.click()
        driver.implicitly_wait(3)
        time.sleep(1)
        driver.get("https://www.olx.ro/d/myaccount/")
        driver.implicitly_wait(4)
        print("Elementul a fost găsit!")
    except:
        print("Elementul nu a fost găsit încă")
        count += 1

#inchide browser
driver.quit()
