import 'dart:io';

void main(List<String> args) {
  int n = int.parse(stdin.readLineSync()!);
  int total = 0;

  var vetor = stdin.readLineSync()!.split(' ');
  int a = int.parse(vetor[0]);
  int b = int.parse(vetor[2]);
  String simbolo = vetor[1];
  if (simbolo == "*") {
    total = a * b;
  } else {
    total = a + b;
  }

  if (total <= n) {
    print("OK");
  } else {
    print("OVERFLOW");
  }
}
