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

c2 = 206637277523316507362139933927937155550022837331244504843965961476614019383602527135957853427917306492229654755594402899976160152565954096952013998754261364976683601827478960752661812105682644979115118449037217502679256098833185214123033778956176050884024055785470382538505502611153823671541088605506318657243
c1 = 339959282219630878273388034415899015715280698706451230817010044015469192892656193972643297879339983976482429859742722123922248960332900708343396147001513953051717287451489145910315870265557144166292539976534836410296038897655096434286755122269741042033918108687883258989922194108269475911699633595111809007293
e2 = 13521927979417175825463063347222803267672338126236919097685639546419640649137631879086526055040440600762677713171345276116684002435281179604562770545346538476338105973545203128426046290278877261803791446624619505571960450739503996077069249754644676412779930081062763034873018062088748804140695301545479
e1 = 13720370251305502198453722303188629715020031854527043028194234587721186750392338568840741980913602828872478379633547127489067215473859867030790069290379619590347878081800599482228153098812888823547824784484067322280093055550108000430624575508213640786019798979841125209412964502922275741976071872949241
n = 497173522389038132581679656348726441223635460077646001242117112508529043004662639934569016294650189660831221622187412764733543952232789394101543715734107673614961378260798863533871182763922914061270612268219742193327876392527222918923185069291141197452073838031685654611566686242080080446337367447541588723277

x, y, g = ext_euclid(e1, e2)
# x < 0
m = mod_mul_inverse(pow(c1, -x, n), n) * pow(c2, y, n) % n
print hex(m)[2:-1].decode('hex')

