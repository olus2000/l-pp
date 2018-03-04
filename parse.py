def parseline(ln, adds):
    ln = ln.lower()
    #definiuj słowa
    words = {
        'def': "jest prostrzy sposób na zapisanie",
        'enddef': "i taka definicja na razie wam wystarczy",
        'loop': "przestań dopierko, gdy",
        'endloop': "i to tyle",
        'if': "zieliński, do tablicy",
        'endif': "wtedy i tylko wtedy, gdy",
        'commentbegin': "przyklad",
        'commentend': "teraz zadanka",
        'inp': "żeby to rozwiązać, musimy znać",
        'outp': "a teraz makowski napisze mi",
        'newvar': "zdefiniujmy zmienną",
        'newvars': "zdefiniujmy zmienne",
        'result': "naszym rozwiązaniem jest",
        'let': "niech",
        '': "oraz"}
    for k in words:
        if words[k] in ln:
            if k=="commentend":
                return ['', '']
            if adds=='c':
                return ['','c']
            if k=="commentbegin":
                return ['','c']
            
            return [ln.replace(words[k], k), '']
    return ["",'e']



def parsestr(a):
    res = []
    n = ''
    for i in a.splitlines():
        [x, n] = parseline(i, n)
        res.append(x)
    return res

def parsefile(filein, fileout):
    f1 = open(filein, mode='r', encoding='utf-8')
    ret = parsestr(f1.read())
    f1.close()
    ret2 = .'\n'.join(ret1) + '\n'
    f1 = open(fileout, mode='w')
    f1.write(ret2)
    f1.close()

parsefile('foo.l-pp', 'foo.pl-pp')
