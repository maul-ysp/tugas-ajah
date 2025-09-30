banner ="""

$$\      $$\                     $$\                               
$$$\    $$$ |                    $$ |                              
$$$$\  $$$$ | $$$$$$\  $$\   $$\ $$ | $$$$$$\  $$$$$$$\   $$$$$$\  
$$\$$\$$ $$ | \____$$\ $$ |  $$ |$$ | \____$$\ $$  __$$\  \____$$\ 
$$ \$$$  $$ | $$$$$$$ |$$ |  $$ |$$ | $$$$$$$ |$$ |  $$ | $$$$$$$ |
$$ |\$  /$$ |$$  __$$ |$$ |  $$ |$$ |$$  __$$ |$$ |  $$ |$$  __$$ |
$$ | \_/ $$ |\$$$$$$$ |\$$$$$$  |$$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |
\__|     \__| \_______| \______/ \__| \_______|\__|  \__| \_______|"""

print(banner)

teks = input("Masukkan sebuah string dengan 4 karakter : ")

hasil = ""

for ch in teks:
    
    kode = ord(ch)
    
    kapital = kode - 32
    
    hasil += chr(kapital)

print("Hasil kapitalisasi string tersebut adalah", hasil)
