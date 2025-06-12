// Problema:// 2982 - A Greve para ou Continua?
// Resposta:// Accepted
// Linguagem:// Dart 3.0 (dart 3.0.5)
// Tempo:// 2.004s
// Tamanho:// 441 Bytes
// Submissão:// 12/11/2024 23:31:09

import 'dart:io';

void main(List<String> args) {
  int a = int.parse(stdin.readLineSync()!);

  int g = 0;
  int v = 0;
  for (int i = 0; i < a; i++) {
    var b = stdin.readLineSync()!.split(' ');
    if (b[0] == 'V') {
      v = v + int.parse(b[1]);
    } else {
      g = g + int.parse(b[1]);
    }
  }
  if (v >= g) {
    print("A greve vai parar.");
  } else {
    print("NAO VAI TER CORTE, VAI TER LUTA!");
  }
}
