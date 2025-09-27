# Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temperaturaCelsius = float(input("Digite uma temperatura em Celsius: "));

temperaturaFahrenheit = temperaturaCelsius + 273;

print(f"A temperatura de {temperaturaCelsius:.1f} °C graus Celsius\nÉ em Fahrenheit {temperaturaFahrenheit:1f} F");