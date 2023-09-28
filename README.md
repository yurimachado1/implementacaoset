# T1 - Implementação do tipo de dado abstrato Set.

Em resumo, a escolha da estrutura de dados Hash Table é justificada principalmente pela eficiência das operações de adição, remoção e verificação de existência, que são realizadas em tempo médio constante (O(1)), tornando-a adequada para conjuntos grandes. No entanto, operações de combinação de conjuntos (união, interseção e diferença) têm complexidade de tempo linear no pior caso, mas ainda são eficientes em cenários típicos. O espaço ocupado é diretamente proporcional ao número de elementos no conjunto, resultando em complexidade de espaço linear (O(n)).

## Adicionar:
Em uma tabela hash, a adição de elementos é eficiente, pois permite o acesso direto ao local onde o elemento deve ser inserido com base em sua chave (no caso, o próprio elemento). Isso evita a necessidade de percorrer todo o conjunto para inserir um elemento, tornando a operação constante em tempo médio.
        
  - Complexidade de tempo: A adição de um elemento em uma tabela hash é, em média, uma operação de tempo constante (O(1)), porque a estrutura de tabela hash calcula o índice do elemento com base em sua chave (no caso, o próprio elemento) e insere diretamente no local apropriado. No entanto, vale ressaltar que, em casos raros, pode ocorrer uma colisão, o que pode exigir um tempo adicional para resolver a colisão, mas isso ainda é considerado um caso raro em implementações eficientes.
        
  - Complexidade de espaço: A complexidade de espaço é linear (O(n)), onde "n" é o número de elementos no conjunto. Cada elemento é armazenado na tabela hash, e o espaço ocupado é diretamente proporcional ao número de elementos.

## Remover:
A remoção de elementos também é eficiente em uma tabela hash, pois, da mesma forma que a adição, permite o acesso direto ao local do elemento a ser removido. Isso resulta em uma operação de remoção constante em tempo médio.

- Complexidade de tempo: Da mesma forma que a adição, a remoção em uma tabela hash é, em média, uma operação de tempo constante (O(1)). O algoritmo calcula o índice do elemento a ser removido e o exclui diretamente do local apropriado. Como na adição, em casos raros de colisão, pode haver um tempo adicional para resolver a colisão.

- Complexidade de espaço: A complexidade de espaço é linear (O(n)), como na adição, porque a estrutura de tabela hash precisa armazenar todos os elementos.

## Verificar existência:
Verificar a existência de um elemento em uma tabela hash é altamente eficiente, pois a estrutura permite um acesso direto ao local onde o elemento deve estar. Isso também resulta em uma operação de verificação de existência constante em tempo médio.

- Complexidade de tempo: A verificação da existência de um elemento em uma tabela hash também é uma operação de tempo constante (O(1)) em média, pois a estrutura permite o acesso direto ao local onde o elemento deve estar.

- Complexidade de espaço: A complexidade de espaço é linear (O(n)), pois a estrutura de tabela hash precisa armazenar todos os elementos.

## União, Interseção e Diferença:

As operações de união, interseção e diferença são eficientes neste caso, pois a estrutura de tabela hash permite a combinação de conjuntos de maneira eficiente, evitando elementos duplicados e eliminando elementos desnecessários em tempo constante ou linear, dependendo do número de elementos envolvidos.

- Complexidade de tempo: As operações de união, interseção e diferença têm complexidade de tempo linear no pior caso (O(n)), onde "n" é o número total de elementos nos conjuntos envolvidos. Isso ocorre porque essas operações envolvem percorrer todos os elementos de ambos os conjuntos para realizar a combinação. No entanto, em média, podem ser mais eficientes em cenários comuns, especialmente quando a tabela hash é bem dimensionada e não há muitas colisões.

- Complexidade de espaço: A complexidade de espaço para o resultado dessas operações é linear (O(n)), uma vez que o conjunto resultante pode conter até todos os elementos de ambos os conjuntos originais.
