# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

firstScore = float(input("Type the first score of the student: "));
secondScore = float(input("Type the second score of the student: "));

averageScore = (firstScore + secondScore) / 2;

print(f"The average score of this student was {averageScore}");