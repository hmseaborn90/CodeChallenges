def rgb(r, g, b):
    values = [r,g,b]
    for i in range(len(values)):
        if (values[i] < 0):
            values[i] = 0
            print(values[i])
        if values[i] > 255:
            values[i] = 255        
    r,g,b = values
    hexCode = '{:02X}{:02X}{:02X}'.format(r,g,b)
    return hexCode

def rgb(r, g, b):
    return '{0:02X}{1:02X}{2:02X}'.format(max(min(r, 255), 0), max(min(g, 255), 0), max(min(b, 255), 0))

def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
# rgb(0,0,0),"000000", "testing zero values"
# rgb(1,2,3),"010203", "testing near zero values"
# rgb(255,255,255), "FFFFFF", "testing max values")
# rgb(254,253,252), "FEFDFC", "testing near max values"
# rgb(-20,275,125), "00FF7D", "testing out of range values"