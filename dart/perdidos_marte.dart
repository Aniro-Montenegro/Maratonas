import 'dart:io';

void main(List<String> args) {
  // ignore: unused_local_variable
  int n = int.parse(stdin.readLineSync()!);
  var vetor = stdin.readLineSync()!.split(' ');
  String palavra = "";

  for (var c in vetor) {
    palavra = palavra + String.fromCharCode(int.parse(c, radix: 16));
  }
  print(palavra);
}
