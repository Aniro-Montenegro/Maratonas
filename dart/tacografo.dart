import 'dart:io';

void main(List<String> args) {
  int a = int.parse(stdin.readLineSync()!);
  int total = 0;
  for (int i = 0; i < a; i++) {
    var vetor = stdin.readLineSync()!.split(' ').map(int.parse).toList();
    total = total + (vetor[0] * vetor[1]);
  }

  print(total);
}
