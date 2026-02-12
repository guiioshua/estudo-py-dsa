# Estruturas de Dados e Algoritmos (DSA) em Python

Repositório de estudo e exercício. 
Implementações fundamentais de estruturas de dados, focadas em eficiência algorítmica e manipulação direta de referências no modelo de memória Python.

---

## 1. Lista Ligada Simples (Singly Linked List)

Uma implementação de lista linear que utiliza ponteiros para o início (`head`) e o fim (`tail`) da estrutura, permitindo crescimento dinâmico e acesso eficiente às extremidades.

### Métodos Implementados:
* **`append(value)`**: Adiciona um elemento ao final da lista.
    * **Complexidade:** $O(1)$ devido à manutenção da referência `tail`.
* **`delete(value)`**: Remove a primeira ocorrência do valor especificado.
    * **Lógica:** Utiliza a busca de predecessor para realizar o "bridge" (ponte) entre os nós, ignorando o nó alvo. Trata especificamente a remoção do `head` e atualiza o `tail` se o último elemento for removido.
    * **Complexidade:** $O(n)$ para localização do valor.
* **`search(value)`**: Percorre a lista linearmente para localizar o nó que contém o valor informado.
    * **Complexidade:** $O(n)$.
* **`reverse()`**: Inverte a orientação de todos os ponteiros da lista de forma *in-place*.
    * **Complexidade:** $O(n)$ de tempo e $O(1)$ de espaço.
* **`read_list()`**: Percorre a estrutura exibindo os valores e as conexões visuais entre os nós.
* **`_find_predecessor(value)`**: Método auxiliar interno que localiza o nó imediatamente anterior ao valor alvo, permitindo operações de remoção seguras.

---

## 2. Pilha (Stack)

Implementação de estrutura LIFO (*Last-In, First-Out*) baseada em lista ligada simples. O gerenciamento ocorre no topo (`head`), permitindo atualizações de estado sem necessidade de deslocamento de memória.

### Métodos Implementados:
* **`push(value)`**: Insere um elemento no topo da pilha.
    * **Complexidade:** $O(1)$.
* **`pop()`**: Remove o elemento do topo, retornando seu valor.
    * **Complexidade:** $O(1)$.
* **`peek()`**: Retorna o valor no topo sem removê-lo.
    * **Complexidade:** $O(1)$.
* **`is_empty()`**: Verifica se a pilha contém elementos.

---

## 3. Fila (Queue)

Estrutura FIFO (*First-In, First-Out*) que utiliza referências de `head` e `tail` para garantir que as operações de entrada e saída ocorram em ambas as extremidades com eficiência máxima.

### Métodos Implementados:
* **`enqueue(value)`**: Adiciona um elemento ao final da fila.
    * **Complexidade:** $O(1)$.
* **`dequeue()`**: Remove o primeiro elemento da fila.
    * **Complexidade:** $O(1)$.
* **`front()`**: Retorna o valor posicionado no início da fila sem removê-lo.
* **`is_empty()`**: Verifica a vacuidade da estrutura.

---

## 4. Árvore de Prefixos (Trie)

Estrutura de árvore especializada para busca de strings e verificação da presença de prefixos, onde cada nó representa um caractere.

### Métodos Implementados:
* **`insert(word)`**: Insere uma string na árvore, mapeando caracteres para nós filhos.
    * **Complexidade:** $O(k)$, onde $k$ é o comprimento da palavra.
* **`search(word)`**: Verifica a existência de uma palavra completa.
    * **Complexidade:** $O(k)$.
* **`contains(prefix)`**: Verifica se um prefixo específico existe na árvore.
    * **Complexidade:** $O(k)$.

---

## 5. Tabela Hash (Hash Table)

Mapeamento associativo de pares chave-valor utilizando **Encadeamento Externo** (*Separate Chaining*) para resolução de colisões.

### Mecanismos Principais:
* **Slots e Cadeias**: Cada posição na tabela (*slot*) contém uma instância de `LinkedList` que armazena tuplas no formato `(key, value)`.
* **Resolução de Colisões**: Chaves distintas que resultam no mesmo índice de hash coexistem no mesmo slot através da lista ligada.
* **Dimensionamento**: Utiliza `sympy.nextprime` para definir o tamanho da tabela como um número primo, reduzindo padrões de colisão.

### Métodos Implementados:
* **`put(key, value)`**: Implementa lógica de **Upsert**. Busca a chave na cadeia correspondente; se encontrada, o valor é atualizado; caso contrário, um novo par é anexado.
    * **Complexidade:** $O(1)$ médio; $O(k)$ no pior caso (onde $k$ é o tamanho da cadeia).
* **`get(key)`**: Localiza a chave via hash e realiza busca linear na cadeia para retornar o valor associado.
    * **Complexidade:** $O(1)$ médio.
* **`remove(key)`**: Remove a entrada correspondente à chave. Trata os ponteiros da lista ligada para garantir que a cadeia permaneça íntegra após a remoção.
    * **Complexidade:** $O(1)$ médio.

---

## Detalhes de Implementação

* **Gerenciamento de Referências**: As estruturas manipulam diretamente os atributos `next_node_ref`, operando no nível de ponteiro para evitar o custo de realocação de listas nativas do Python.
* **Armazenamento em Tuplas**: Na Tabela Hash, a informação é encapsulada em tuplas `(key, value)` dentro de cada nó, permitindo a distinção entre chaves colidentes durante a recuperação dos dados.
* **Ausência de Sentinelas**: Utiliza-se `None` para representar estados vazios e o fim das cadeias, com tratamento explícito para evitar erros de referência em listas vazias ou com um único elemento.