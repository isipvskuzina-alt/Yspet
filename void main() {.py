void main() {
 
  List<String> students = [
    'Катасонов Николай',
    'Кузьмин Даниил',
    'Спиридонова Ольга',
    'Волошедова Алиса',
    'Смирнов Клим',
    'Антонов Алексей',
    'Лёвичева Анна' 
  ];

  
  List<String> subjects = [
    'Математика',
    'Физика',
    'Литература',
    'История',
    'Английский язык' 
  ];


  List<List<int>> grades = [
      
    [5, 5, 5, 4, 5], // Средний балл: 4.8
    [4, 4, 5, 3, 4], // Средний балл: 4.0
    [5, 5, 5, 5, 5], // Средний балл: 5.0
    [3, 2, 4, 3, 3], // Средний балл: 3.0
    [5, 4, 5, 4, 5], // Средний балл: 4.6
    [2, 3, 3, 2, 4], // Средний балл: 2.8
    [4, 4, 4, 5, 4]  // Средний балл: 4.2
  ];

  print(' Журнал успеваемости \n');

  
  print('1. категории по успеваемости ');
  

  List<String> excellent = []; // отличники (средний >= 4.5)
  List<String> good = [];      // хорошисты (средний от 3.5 до 4.5)
  List<String> others = [];    // остальные (средний < 3.5)
  

  for (int i = 0; i < students.length; i++) {
   
    double sum = 0;
    for (int grade in grades[i]) {
      sum += grade;
    }
    double average = sum / subjects.length;
    
  
    if (average >= 4.5) {
      excellent.add(students[i]);
    } else if (average >= 3.5) {
      good.add(students[i]);
    } else {
      others.add(students[i]);
    }
  }
  

  print('Отличники (средний балл >= 4.5): ${excellent.isEmpty ? "нет" : excellent.join(", ")}');
  print('Хорошисты (средний балл 3.5 - 4.5): ${good.isEmpty ? "нет" : good.join(", ")}');
  print('Остальные (средний балл < 3.5): ${others.isEmpty ? "нет" : others.join(", ")}');
  print(''); 

  print('2. Статистика оценок ');
  
  // Счетчики для каждой оценки
  int count2 = 0, count3 = 0, count4 = 0, count5 = 0;
  
  // Проходим по всем оценкам
  for (var studentGrades in grades) {
    for (int grade in studentGrades) {
      if (grade == 2) count2++;
      else if (grade == 3) count3++;
      else if (grade == 4) count4++;
      else if (grade == 5) count5++;
    }
  }
  
  print('Оценка 2: $count2 раз(а)');
  print('Оценка 3: $count3 раз(а)');
  print('Оценка 4: $count4 раз(а)');
  print('Оценка 5: $count5 раз(а)');
  print('');

  print(' 3. по каждому предмету 5');
  
  // Проходим по каждому предмету
  for (int j = 0; j < subjects.length; j++) {
    List<String> studentsWith5 = [];
    
    // Ищем студентов с пятёркой по этому предмету
    for (int i = 0; i < students.length; i++) {
      if (grades[i][j] == 5) {
        studentsWith5.add(students[i]);
      }
    }
    
    print('${subjects[j]}: ${studentsWith5.isEmpty ? "нет" : studentsWith5.join(", ")}');
  }
  print('');

  print('4. предметы без двоек');
  
  List<String> subjectsWithout2 = [];
  
  // Проверяем каждый предмет
  for (int j = 0; j < subjects.length; j++) {
    bool hasTwo = false;
    
    for (int i = 0; i < students.length; i++) {
      if (grades[i][j] == 2) {
        hasTwo = true;
        break; // если нашли двойку, дальше можно не искать
      }
    }
    
    if (!hasTwo) {
      subjectsWithout2.add(subjects[j]);
    }
  }
  
  print(subjectsWithout2.isEmpty ? "Нет таких предметов" : subjectsWithout2.join(", "));
  print('');

  print('5. предмет с двойками');
  
  int maxTwos = 0;
  String subjectWithMaxTwos = '';
  
  // Считаем двойки по каждому предмету
  for (int j = 0; j < subjects.length; j++) {
    int twosCount = 0;
    
    for (int i = 0; i < students.length; i++) {
      if (grades[i][j] == 2) {
        twosCount++;
      }
    }
    
    if (twosCount > maxTwos) {
      maxTwos = twosCount;
      subjectWithMaxTwos = subjects[j];
    }
  }
  
  print('$subjectWithMaxTwos — $maxTwos двоек');
  print('');

  print('6. студенты с пятёрками');
  
  // Считаем пятёрки для каждого студента
  List<int> fivesCount = List.filled(students.length, 0);
  
  int maxFives = 0;
  for (int i = 0; i < students.length; i++) {
    for (int grade in grades[i]) {
      if (grade == 5) {
        fivesCount[i]++;
      }
    }
    if (fivesCount[i] > maxFives) {
      maxFives = fivesCount[i];
    }
  }
  
  for (int i = 0; i < students.length; i++) {
    if (fivesCount[i] == maxFives) {
      print('${students[i]} — $maxFives пятёрок');
    }
  }
  print('');

  print(' 7. Предметы с оценкой 4');
  
  for (int i = 0; i < students.length; i++) {
    List<String> badSubjects = [];
    
    for (int j = 0; j < subjects.length; j++) {
      if (grades[i][j] < 4) {
        badSubjects.add(subjects[j]);
      }
    }
    
    if (badSubjects.isNotEmpty) {
      print('${students[i]} (${badSubjects.length} предметов): ${badSubjects.join(", ")}');
    } else {
      print('${students[i]}: нет предметов с оценкой ниже 4');
    }
  }
  print('');

 
  print('8. ВСе пары с оценкой 5');
  
  for (int i = 0; i < students.length; i++) {
    for (int j = 0; j < subjects.length; j++) {
      if (grades[i][j] == 5) {
        print('${students[i]} — ${subjects[j]}');
      }
    }
  }
}