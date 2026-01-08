# Estruturas de Dados e Algoritmos (DSA) em Python

Repositório de estudo e exercício. 
Implementações fundamentais de estruturas de dados, focadas em eficiência algorítmica e manipulação direta de referências no modelo de memória Python.

---

## 1. Lista Ligada Simples (Singly Linked List)

Uma implementação de lista linear que utiliza ponteiros para `head` (cabeça) e `tail` (cauda), otimizando a inserção.

### Métodos Implementados:
* **`append(value)`**: Adiciona um elemento ao final da lista. 
    * **Complexidade:** $O(1)$ devido ao uso do ponteiro `tail`.
* **`delete()`**: Remove o último elemento da lista. 
    * **Complexidade:** $O(n)$, Como não há ponteiros em duas direções, exige a percorrer toda estrutura para encontrar o penúltimo nó e atualizar o `tail`.
* **`reverse()`**: Inverte a orientação de todos os ponteiros da lista com lógica in-place.
    * **Complexidade:** $O(n)$ de tempo e $O(1)$ de espaço, utilizando a algoritmo sliding-window (`previous`, `current`, `next_node`).
* **`read()`**: Percorre a lista e exibe os valores formatados.
* **`find_last_but_one()`**: Método auxiliar que localiza o penúltimo nó para suporte à deleção, necessário por ser singly linked list.

---

## 2. Árvore de Prefixos (Trie)

Estrutura de árvore especializada para busca de strings e verificação da presença de prefixos, cada nó representando um char.

### Métodos Implementados:
* **`insert(word)`**: Insere uma palavra completa na árvore, criando nós para caracteres inexistentes e marcando o final da string.
* **`search(word)`**: Verifica se uma palavra completa existe na estrutura.
* **`contains(prefix)`**: Verifica se existe qualquer palavra que comece com o prefixo fornecido.

---

## Detalhes de Implementação

* **Ponteiros em Python:** As implementações evitam cópias desnecessárias de objetos, manipulando diretamente as referências de memória (`next_node_ref`).
* **Sem Sentinelas:** A lista ligada utiliza um início limpo (`None`), tratando explicitamente os casos de listas vazias ou com um único nó para garantir robustez.
* **Busca em Trie:** A busca por prefixos é otimizada para tempo $O(k)$, onde $k$ é o comprimento da string, independente do número de palavras