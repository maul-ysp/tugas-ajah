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

data1=input("masukkan string pertama: ")
data2=input("masukkan string kedua: ")
data3=input("masukkan string ketiga: ")
hasil=" ".join([data1, data2, data3])
print("hasil dari pergabungan tiga string tersebut adalah", hasil)