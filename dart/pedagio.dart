import 'dart:io';

void main(List<String> args) {
  var vetor = stdin.readLineSync()!.split(' ').map(int.parse).toList();
  var vetor2 = stdin.readLineSync()!.split(' ').map(int.parse).toList();

  print((vetor[0] * vetor2[0]) + ((vetor[0] ~/ vetor[1]) * vetor2[1]));
}
