coisa = input('Digite algo: ')
print('O tipo dela é: ', type(coisa))
print('Só tem espaçõs: ', coisa.isspace())
print('É um numero: ', coisa.isnumeric())
print('É uma letra: ', coisa.isalpha())
print('É alphanumerico: ', coisa.isalnum())
print('Esta em minusculo:', coisa.islower())
print('Esta em maiusculo:', coisa.isupper())
print('Esta capitalizada: ', coisa.istitle())
