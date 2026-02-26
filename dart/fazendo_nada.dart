import 'dart:io';

void main(List<String> args) {
  while (true) {
    var dados = stdin.readLineSync()!.split(' ').map(int.parse).toList();
    if (dados[0] == -1 && dados[1] == -1) {
      break;
    }
    var lista = stdin.readLineSync()!.split(' ').map(int.parse).toList();
    int tamanho = lista.length;
    int total = lista.fold(
      0,
      (previous, current) => previous + (current * tamanho),
    );

    print(total);
  }
}
