import 'dart:io';

void main(List<String> args) {
  int a = int.parse(stdin.readLineSync()!);
  var lista = [];

  for (int i = 0; i < a; i++) {
    if (i == 0 || i == 1) {
      lista.add(1);
    } else {
      lista.add(lista[i - 1] + lista[i - 2]);
    }
  }

  var resultado = lista.reversed.toList().join(" ");

  print(resultado);
}
