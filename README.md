Problema do Caixeiro Viajante

Abordagem a partir de problemas sempre solúveis. Problema estático. 

Premissa: A linguagem emergente de um alfabeto não pode ser estática, quando as instâncias a serem codificadas são dinâmicas. 
O que define o limite de um sistema de codificação é seu alfabeto e não sua linguagem. 
Um alfabeto é o conjunto máximo sob o qual se resolve problemas, sendo assim, instâncias não codificáveis são irreais para o universo de resolução. 
Instâncias reais são codificáveis dentro do universo [possível] de resolução. 
Uma instância pode ser parcialmente real ou incompleta, se existirem instâncias impossíveis para o universo da linguagem, mas não para o universo do alfabeto. 
Para um sistema de alfabeto absolutamente dinâmico, qualquer instância é real. 
Para um sistema de alfabeto estático, algumas instâncias podem ser irreais e instâncias reais podem ser momentaneamente parciais. 

S: alfabeto sob o qual podem ser codificadas as instâncias de P. 

P: conjunto dinâmico de instâncias sobre S. 

G: conjunto dinâmico de instancias codifificáveis de P, em S. 

E: conjunto dinâmico de instâncias não codificáveis de P, em S. 

I: instâncias irreais. 

I pertence a E. 

G + E = P 

G pode ser codificado em S

E não pode ser codificado em S se S não é um alfabeto dinâmico. 

E talvez possa ser codificado em S se S é um alfabeto dinâmico. 

I não pode ser codificado em S. 

Conjuntos dinâmicos variam em tamanho. 
Alfabetos dinâmicos variam em aleatoriedade. 

Assim: 

Um conjunto dinâmico deve ser capaz de ter quantidade variável de instâncias.

Um alfabeto dinâmico deve ser capaz de oferecer codificações para instâncias não codificáveis, a partir de um estado de codificação anterior, variando seu código proporcionalmente. Ou seja: S possui um tamanho fixo e aleatoridade variável e menor que seu tamanho.

O grau maximo de aleatoriedade em S é proporcional ao seu tamanho. A aleatoriedade máxima de S é a combinação possível de seu alfabeto. A aleatoriedade mínima de S é seu estado atual enquanto E possui tamanho 0. 

A variação de aleatoriedade em S é uma variação de tipos de instâncias em P, proporcional a E. 

A variação mínima de S se dá quando o tamanho de E é igual a zero. 
I é maior que zero para aquelas instâncias não codificáveis quando a aleatoriedade de S é igual ao tamanho de S. 
A classe do alfabeto é definida quando I é maior que zero. O tipo do alfabeto é dinâmico de acordo com o valor de I. 

<S> = ({P, I}, {0, >0}, {P, 0, I}, {P, >0, I}, P, {P})
