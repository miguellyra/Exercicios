# Ex111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamado moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108, e 109 para o primeiro pacote e mantenha tudo funcionando.

from pct111.utilidadescev.moeda import moeda

preço = float(input('Digite o preço: R$'))
moeda.resumo(preço, 35, 22, True)