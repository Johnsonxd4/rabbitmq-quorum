#Comportamento:
* A fila existirá apenas em um nó do cluster
* Todas as operações podem ser executadas em qualquer nós, visto que o cluster irá rotear tais operações para o lider da fila de forma transparente.
* Em caso do nó em que a fila reside esteja indisponivel, obteremos comportamentos diferentes de acordo com a configuração da fila:
	- Filas *durable*, ficarão indisponiveis até que o o nó volte a operar.
	- Filas *non-durable" serão simplesmente deletadas.

