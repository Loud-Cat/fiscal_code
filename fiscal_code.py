def fiscal_code(d):
    d = {k:d[k].lower() for k in d}
    result, vowels = "", "aeiou"
    cons = [i for i in d['surname'] if i not in vowels]
    vows = [i for i in d['surname'] if i in vowels]
    if len(cons) >= 3:
        result += "".join(cons[:3])
    elif len(d['surname']) >= 3:
        result += "".join(cons) + "".join(vows[:3-len(cons)])
    else:
        result += "".join(cons) + "".join(vows) + "".join(["X","X","X"][:3-len(cons+vows)])

    cons = [i for i in d['name'] if i not in vowels]
    vows = [i for i in d['name'] if i in vowels]
    if len(cons) == 3:
        result += "".join(cons)
    elif len(cons) > 3:
        result += cons[0] + cons[2] + cons[3]
    elif len(d['name']) >= 3:
        result += "".join(cons) + "".join(vows[:3-len(cons)])
    else:
        result += "".join(cons) + "".join(vows) + "".join(["X","X","X"][:3-len(cons+vows)])

    dob = d['dob']
    result += dob[-2:]
    months = {'1':'A', '2':'B', '3':'C', '4':'D', '5':'E', '6':'H','7':'L',
        '8':'M', '9':'P', '10':'R', '11':'S', '12':'T'}
    month = dob[dob.index('/')+1:dob.replace('/', ' ', 1).index('/')]
    result += months.get(month, '?')

    day = dob[:dob.index('/')]
    if d['gender'] == 'm':
        if int(day) < 10:
            result += '0' + day
        else:
            result += day
    elif d['gender'] == 'f':
        result += str(int(day) + 40)
    return result.upper()
