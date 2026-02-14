// import 'dart:io';

// void main(List<String> args) {
//   int indice = 0;
//   while (true) {
//     int a = int.parse(stdin.readLineSync()!);
//     if (a == 0) {
//       break;
//     } else {
//       for (int z = 0; z < a; z++) {
//         var vetor = stdin
//             .readLineSync()!
//             .split(' ')
//             .map(int.parse)
//             .toList()
//             .asMap()
//             .entries
//             .where((entry) => entry.value <= 127)
//             .map((entry) => entry.key)
//             .toList();
//         ;

//         if (vetor.length != 1) {
//           print("*");
//         } else {
//           indice = vetor[0];
//           switch (indice) {
//             case 0:
//               print("A");
//               break;
//             case 1:
//               print("B");
//               break;
//             case 2:
//               print("C");
//               break;
//             case 3:
//               print("D");
//               break;
//             case 4:
//               print("E");
//               break;
//           }
//         }
//       }
//     }
//   }
// }

// ________________________________________________

import 'dart:io';

void main(List<String> args) {
  int quantidade = 0;
  int indice = 0;
  while (true) {
    int a = int.parse(stdin.readLineSync()!);
    if (a == 0) {
      break;
    } else {
      for (int z = 0; z < a; z++) {
        var vetor = stdin.readLineSync()!.split(' ').map(int.parse).toList();
        quantidade = 0;
        for (int x = 0; x < 5; x++) {
          if (vetor[x] <= 127) {
            quantidade = quantidade + 1;
            indice = x;
            if (quantidade != 1) {
              break;
            }
          }
        }
        if (quantidade != 1) {
          print("*");
        } else if (indice == 0) {
          print("A");
        } else if (indice == 1) {
          print("B");
        } else if (indice == 2) {
          print("C");
        } else if (indice == 3) {
          print("D");
        } else if (indice == 4) {
          print("E");
        }
      }
    }
  }
}
