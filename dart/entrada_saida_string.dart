import 'dart:io';

// void main(List<String> args) {
//   String palavra1 = stdin.readLineSync()!;
//   String palavra2 = stdin.readLineSync()!;
//   String palavra3 = stdin.readLineSync()!;
//   String pal1 = "";
//   String pal2 = "";
//   String pal3 = "";
//   if (palavra1.length > 10) {
//     pal1 = palavra1.substring(0, 10);
//   } else {
//     pal1 = palavra1;
//   }
//   if (palavra2.length > 10) {
//     pal2 = palavra2.substring(0, 10);
//   } else {
//     pal2 = palavra2;
//   }

//   if (palavra3.length > 10) {
//     pal3 = palavra3.substring(0, 10);
//   } else {
//     pal3 = palavra3;
//   }

//   print(palavra1 + palavra2 + palavra3);
//   print(palavra2 + palavra3 + palavra1);
//   print(palavra3 + palavra1 + palavra2);
//   print(pal1 + pal2 + pal3);
// }

void main(List<String> args) {
  String palavra1 = stdin.readLineSync()!;
  String palavra2 = stdin.readLineSync()!;
  String palavra3 = stdin.readLineSync()!;

  print(palavra1 + palavra2 + palavra3);
  print(palavra2 + palavra3 + palavra1);
  print(palavra3 + palavra1 + palavra2);
  print(
    (palavra1.length <= 10 ? palavra1 : palavra1.substring(0, 10)) +
        (palavra2.length <= 10 ? palavra2 : palavra2.substring(0, 10)) +
        (palavra3.length <= 10 ? palavra3 : palavra3.substring(0, 10)),
  );
}
