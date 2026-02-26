import 'dart:io';

void main(List<String> args) {
  int a = int.parse(stdin.readLineSync()!);
  int b = 0;
  int cont = 0;
  int variavel = 0;
  var dados = stdin.readLineSync()!.split(' ').map(int.parse).toList();
  int i = 0;
  for (var d in dados) {
    if (i == 0) {
      b = d;
    } else {
      if (d < b && cont == 0) {
        cont = 1;
        variavel = i + 1;
      }
    }
    b = d;
    i++;
  }
  print(variavel);
}
