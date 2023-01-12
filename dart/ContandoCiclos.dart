// SUBMISSÃO # 31519685
// PROBLEMA:2497 - Contando Ciclos
// RESPOSTA:Accepted
// LINGUAGEM:Dart (dart 2.9) [+2s]
// TEMPO:0.004s
// TAMANHO:397 Bytes
// MEMÓRIA:-
// SUBMISSÃO:12/01/2023 13:08:06
import 'dart:io';

void main() {
  int a = int.parse(stdin.readLineSync()!);

  int i = 1;
  while (a != -1) {
    if (a % 2 == 0) {
      int z = a ~/ 2;

      print("Experiment ${i}: ${z} full cycle(s)");
      i++;
    } else {
      int z = (a - 1) ~/ 2;

      print("Experiment ${i}: ${z} full cycle(s)");
      i++;
    }
    a = int.parse(stdin.readLineSync()!);
  }
}
