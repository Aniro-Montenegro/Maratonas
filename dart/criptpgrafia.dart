import 'dart:io';

void main(List<String> args) {
  int n = int.parse(stdin.readLineSync()!);

  for (int ii = 0; ii < n; ii++) {
    var vetor = stdin.readLineSync()!;
    int tamanho = vetor.length;
    int metade = tamanho ~/ 2;

    List<int> codigos = vetor.codeUnits.toList();

    List<int> invertida = List<int>.filled(tamanho, 0);
    ;
    int contador = tamanho - 1;
    for (int i = 0; i < tamanho; i++) {
      if ((codigos[i] >= 65 && codigos[i] <= 90) ||
          (codigos[i] >= 97 && codigos[i] <= 122)) {
        invertida[contador] = codigos[i] + 3;
        contador--;
      } else {
        invertida[contador] = codigos[i];
        contador--;
      }
    }

    while (metade < tamanho) {
      var l = invertida[metade];
      invertida[metade] = l - 1;
      metade++;
    }

    print(String.fromCharCodes(invertida));
  }
}
