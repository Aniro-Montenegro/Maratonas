unidades = {
    "0": "",
    "1": "I",
    "2": "II",
    "3": "III",
    "4": "IV",
    "5": "V",
    "6": "VI",
    "7": "VII",
    "8": "VIII",
    "9": "IX",
}

dezenas = {
    "0": "",
    "1": "X",
    "2": "XX",
    "3": "XXX",
    "4": "XL",
    "5": "L",
    "6": "LX",
    "7": "LXX",
    "8": "LXXX",
    "9": "XC",
}

centenas = {
    "0": "",
    "1": "C",
    "2": "CC",
    "3": "CCC",
    "4": "CD",
    "5": "D",
    "6": "DC",
    "7": "DCC",
    "8": "DCCC",
    "9": "CM",
}
n = input()

if len(n) == 4:
    print("M")
elif len(n) == 3:
    palavra = ""
    palavra = palavra + centenas[n[0]]
    palavra = palavra + dezenas[n[1]]
    palavra = palavra + unidades[n[2]]
    print(palavra)
elif len(n) == 2:
    palavra = ""
    palavra = palavra + dezenas[n[0]]
    palavra = palavra + unidades[n[1]]
    print(palavra)
elif len(n) == 1:
    palavra = ""
    palavra = palavra + unidades[n[0]]
    print(palavra)
