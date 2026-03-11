# İSTENEN ÇIKTI:
# X sayısı ile Y sayısının toplamı Z.
# Z sayısı ile W sayısının toplamı V.
# V sayısı ile U sayısının çarpımı T.
# T sayısı ile S sayısının bölümü R.

x = 5
y = 10
w = 3
u = 2
s = 4

# Z, V, T, R değerleri hesaplanacak ve kullanılacak.
# Sonrasında üstteki çıktı sağlanacak.
# bu dosya içerisinde sum, sub, mul ve div fonksiyonları da tanımlansın.


def sum(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

 
x = 5
y = 10
w = 3
u = 2
s = 4


z = sum(x, y)
v = sub(z, w)
t = mul(v, u)
r = div(t, s)


print("X = " + str(x))
print("Y = " + str(y))
print("W = " + str(w))
print("U = " + str(u))
print("S = " + str(s))

print("X sayısı ile Y sayısının toplamı Z =" + " " + str(z))
print("Z sayısı ile W sayısının farkı V = " + str(v))
print("V sayısı ile U sayısının çarpımı T = " + str(t))
print("T sayısı ile S sayısının bölümü R = " + str(r))


print(str(x) + " sayısı ile " + str(y) + " sayısının toplamı " + str(z))
print(str(z) + " sayısı ile " + str(w) + " sayısının farkı " + str(v))
print(str(v) + " sayısı ile " + str(u) + " sayısının çarpımı " + str(t))
print(str(t) + " sayısı ile " + str(s) + " sayısının bölümü " + str(r))




