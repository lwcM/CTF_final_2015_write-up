def ext_euclid(a, b):
    if(b == 0):
        return (1, 0, a)
    else:
        (x, y, q) = ext_euclid(b, a%b)
        (x, y) = (y, x-a/b*y)
        return (x, y, q)

# find modular multiplicative inverse
# given (a, n), find a^{-1} (mod n)

def mod_mul_inverse(a, n):
    return (ext_euclid(a, n)[0] % n + n) % n

c = 56267348817991667025293700596381772772705100752049364933949564121901533557055297556368355657861
e = 65537
n = 69037356967092428811573699689752455282165460568629454083502861819413893435697699053715051257547
p = 244568058927274035851630625490731151685151358429
q = 282282802054792109028071238910250727429434271943
phi = (p - 1) * (q - 1)
d = mod_mul_inverse(e, phi)
m = pow(c, d, n)
print hex(m)[2:-1].decode('hex')

