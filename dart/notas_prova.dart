import 'dart:io';

void main(List<String> args) {
  int a = int.parse(stdin.readLineSync()!);

  if (a == 0) {
    print('E');
  } else if (a > 0 && a < 36) {
    print('D');
  } else if (a > 35 && a < 61) {
    print('C');
  } else if (a > 60 && a < 86) {
    print('B');
  } else {
    print('A');
  }
}
