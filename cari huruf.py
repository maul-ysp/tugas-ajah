banner ="""

$$\      $$\                     $$\                               
$$$\    $$$ |                    $$ |                              
$$$$\  $$$$ | $$$$$$\  $$\   $$\ $$ | $$$$$$\  $$$$$$$\   $$$$$$\  
$$\$$\$$ $$ | \____$$\ $$ |  $$ |$$ | \____$$\ $$  __$$\  \____$$\ 
$$ \$$$  $$ | $$$$$$$ |$$ |  $$ |$$ | $$$$$$$ |$$ |  $$ | $$$$$$$ |
$$ |\$  /$$ |$$  __$$ |$$ |  $$ |$$ |$$  __$$ |$$ |  $$ |$$  __$$ |
$$ | \_/ $$ |\$$$$$$$ |\$$$$$$  |$$ |\$$$$$
$$ |$$ |  $$ |\$$$$$$$ |
\__|     \__| \_______| \______/ \__| \_______|\__|  \__| \_______|"""

print(banner)

kalimat = input("Masukkan sebuah kalimat : ")

karakter = input("Karakter yang ingin dihitung jumlahnya : ")

jumlah = kalimat.count(karakter)

print(f"Jumlah karakter {karakter} dalam kalimat tersebut ada {jumlah}")
