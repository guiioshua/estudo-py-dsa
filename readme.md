# Estruturas de Dados e Algoritmos (DSA) em Python

Repositório de estudo e exercício. 
Implementações fundamentais de estruturas de dados, focadas em eficiência algorítmica e manipulação direta de referências no modelo de memória Python.

---

## 1. Lista Ligada Simples (Singly Linked List)

Uma implementação de lista linear que utiliza ponteiros para o início (`head`) e o fim (`tail`) da estrutura.

### Métodos Implementados:
* **`append(value)`**: Adiciona um elemento ao final da lista.
    * **Complexidade:** $O(1)$ devido ao uso da referência `tail`.
* **`delete()`**: Remove o último elemento da lista.
    * **Complexidade:** $O(n)$. Como a lista é simplesmente ligada, é necessário percorrer a estrutura para localizar o penúltimo nó e atualizar o `tail`.
* **`reverse()`**: Inverte a orientação de todos os ponteiros da lista de forma in-place.
    * **Complexidade:** $O(n)$ de tempo e $O(1)$ de espaço.
* **`read()`**: Percorre a lista para exibição dos valores.
* **`find_last_but_one()`**: Localiza o penúltimo nó da lista.

---

## 2. Pilha (Stack)

Implementação de estrutura LIFO (Last-In, First-Out) baseada em lista ligada simples. O gerenciamento ocorre no topo (`head`), permitindo atualizações de estado em tempo constante.

### Métodos Implementados:
* **`push(value)`**: Insere um elemento no topo da pilha.
    * **Complexidade:** $O(1)$.
* **`pop()`**: Remove o elemento do topo, atualizando a referência para o nó anterior.
    * **Complexidade:** $O(1)$.
* **`peek()`**: Retorna o valor no topo sem removê-lo.
    * **Complexidade:** $O(1)$.
* **`is_empty()`**: Verifica se a pilha contém elementos.

---

## 3. Fila (Queue)

Estrutura FIFO (First-In, First-Out) que utiliza referências de `head` e `tail` para garantir eficiência em ambas as extremidades.

### Métodos Implementados:
* **`enqueue(value)`**: Adiciona um elemento ao final da fila.
    * **Complexidade:** $O(1)$.
* **`dequeue()`**: Remove o primeiro elemento da fila.
    * **Complexidade:** $O(1)$.
* **`front()`**: Retorna o valor posicionado no início da fila.
    * **Complexidade:** $O(1)$.
* **`is_empty()`**: Verifica a vacuidade da estrutura.

---

## 4. Árvore de Prefixos (Trie)

Estrutura de árvore especializada para busca de strings e verificação da presença de prefixos, cada nó representando um char.

### Métodos Implementados:
* **`insert(word)`**: Insere uma string na árvore, mapeando caracteres para nós filhos.
    * **Complexidade:** $O(k)$, onde $k$ é o comprimento da palavra.
* **`search(word)`**: Verifica a existência de uma palavra completa.
    * **Complexidade:** $O(k)$.
* **`contains(prefix)`**: Verifica se um prefixo específico existe na árvore.
    * **Complexidade:** $O(k)$.

---

## Detalhes de Implementação

* **Gerenciamento de Referências:** As implementações manipulam diretamente referências de memória (`next_node_ref`, `previous_node_ref`), evitando overhead de cópias de objetos.
* **Ausência de Sentinelas:** Utiliza-se `None` para representar estados vazios, com tratamento explícito de casos de borda.