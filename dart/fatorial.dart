import 'dart:io';

int fatorial(int n) {
  if (n == 0) {
    return 1;
  } else {
    return n * fatorial(n - 1);
  }
}

void main(List<String> args) {
  int a = int.parse(stdin.readLineSync()!);
  int quantidade = 0;
  int referencial = 1;

  while (a >= 1) {
    var x = fatorial(referencial);
    if (x > a) {
      var z = fatorial(referencial - 1);
      a = a - z;
      quantidade++;
      referencial = 1;
    } else {
      referencial++;
    }
  }
  print(quantidade);
}
