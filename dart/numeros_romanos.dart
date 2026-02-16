import 'dart:io';

void main(List<String> args) {
  final Map<String, String> unidades = {
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
  };

  final Map<String, String> dezenas = {
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
  };

  final Map<String, String> centenas = {
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
  };

  var vetor = stdin.readLineSync()!;

  if (vetor.length == 4) {
    print("M");
  } else if (vetor.length == 3) {
    String palavra = "";
    palavra = palavra + centenas[vetor[0]]!;
    palavra = palavra + dezenas[vetor[1]]!;
    palavra = palavra + unidades[vetor[2]]!;
    print(palavra);
  } else if (vetor.length == 2) {
    String palavra = "";

    palavra = palavra + dezenas[vetor[0]]!;
    palavra = palavra + unidades[vetor[1]]!;
    print(palavra);
  } else if (vetor.length == 1) {
    String palavra = "";

    palavra = palavra + unidades[vetor[0]]!;
    print(palavra);
  }
}
