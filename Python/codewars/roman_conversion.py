"""TODO: create a RomanNumerals helper object"""
class RomanNumerals():
    def __init__(self, sn):
        self.sn = sn
    def to_roman(sn):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = ''
        i = 0
        while sn > 0:
            for _ in range(sn // val[i]):
                res += rom[i]
                sn -= val[i]
            i += 1
        return res

    
    def from_roman(s):
            rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            int_val = 0 
            for i in range(len(s)): 
                if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                    int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
                else:
                    int_val += rom_val[s[i]]
            print(int_val)
            return int_val