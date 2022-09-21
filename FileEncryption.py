infile = open('info_security.txt', 'r')
encrypted = infile.read()

codes = {'A':'%','a':'9','B':'@','b':'#','C':'!','c':'3','D':'$','d':'2',
        'E':'7','e':'^','F':'*','f':'8','G':'/','g':'P','H':'1','h':'+',
        'I':')','i':'5','J':'m','j':'O','K':'<','k':';','L':'(','l':'q',
        'M':'6','m':']','N':'~','n':',','O':'?','o':'}','P':'|','p':'-',
        'Q':'4','q':'W','R':'>','r':'L','S':'0','s':';','T':'(','t':'=',
        'U':'88','u':'H','V':'t','v':'==','W':'MJ','w':'{','X':'|||','x':'v',
        'Y':'#@','y':'G','Z':'&','z':'oo','.':'*^',':':'%',' ':'$'}

outfile = open('encrypted.txt', 'w')

for a,b in codes.items():
    search = a
    replace = b
    encrypted=encrypted.replace(search,replace)
    
outfile.write(encrypted)