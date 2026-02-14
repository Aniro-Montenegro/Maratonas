import 'dart:io';

void main(List<String> args) {
  bool isPrime(int n) {
    if (n <= 1) {
      return false;
    }
    for (int i = 2; i * i <= n; i++) {
      if (n % i == 0) {
        return false;
      }
    }
    return true;
  }

  int a = int.parse(stdin.readLineSync()!);
  int primoe = 0;
  int primod = 0;
  primod = a - 1;
  primoe = a + 1;
  while (primoe > 0) {
    if (isPrime(primoe) && isPrime(primod)) {
      print("$primod $primoe");
      break;
    }
    primod++;
    primoe--;
  }
}
