# Bir toplama fonksiyonu yaz ve iki parametreyi toplasın ve yazdırsın. 
# Bir çıkarma fonksiyonu yaz ve iki parametreyi çıkarsın ve yazdırsın. 
# Bir çarpma fonksiyonu yaz ve iki parametreyi çarpsın ve yazdırsın. 
# Bir bölme fonksiyonu yaz ve iki parametreyi bölsün ve yazdırsın. 

def topla(name, age): 
    print(name + " is "  + str(age) +  " years old")

topla("Ali", 25)


def topla(birinci, ikinci):
    print(birinci + ikinci)

topla(5,7)


def çıkar(x, y):
    print(x - y)

çıkar(5,1)


def çarp(sarı, beyaz):
    print(sarı * beyaz)

çarp(2,3)

def böl(kedi, tavşan):
    print(kedi / tavşan)

böl(9,3)