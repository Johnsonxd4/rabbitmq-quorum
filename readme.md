# Replicação de filas:
Este repositorio abrange as direfença entre as formas de replicação de filas, e suas consequencias.

# Filas em cluster, sem replicação configurada:
## Comportamento:
* A fila existirá apenas em um nó do cluster
* Todas as operações podem ser executadas em qualquer nós, visto que o cluster irá rotear tais operações para o lider da fila de forma transparente.
* Em caso do nó em que a fila reside esteja indisponivel, obteremos comportamentos diferentes de acordo com a configuração da fila:
	- Filas *durable*, ficarão indisponiveis até que o o nó volte a operar.
	- Filas *non-durable" serão simplesmente deletadas.

# Filas espelhadas:
## Contexto:
* Este contexto abrange filas clássicas.
* Os conteudos de uma fila por padrão existem apenas em um nó (nó onde a fila foi declarada). 
* Exchanges e bindings existem em todos os nós.
* Existe a possibilidade de executar replicas adicionais em um outro nó do cluster, as chamada filas espelhadas

## Como funciona?
* Para que seja possivel, é necessário ter um cluster.
* Composta de uma replica lider, e um ou mais espelhos. 
* Replica lider reside no nó em que a fila foi declarada.
* Qualquer operação é executada primeiro na lider, depois replicada para as demais filas espelho:
	- publicações
	- entregas
	- rastreamento de acks de mensagens provindas dos consumidores.
* Mensagens publicadas para a fila, são replicadas para os outros espelhos
* Consumidores se conectam à fila lider, enquanto os espelhos deletam as mensagens já consumidas.
	-  Consequentemente, espelhamento de filas aumenta a disponibilidade, porém não distribui a carga de consumidores entre os nós.
* Em caso de falha na fila lider, o espelho mais velho torna-se o lider desde que esteja sincronizado por padrão. 
* Configuração para espelhos não sincronizados tornarem-se lider também é possivel.
* o Throughput de mensagens é menor quando espelhamento de filas são configurados.
* quanto mais espelhos, menor será o throughput.
* Não é possivel espelhar filas exclusivas. Visto que serão excluidas assim que a conexão que a declarou ser fechada.
* Mensagens não sincronizadas com os espelhos durante uma indisponibilidade da fila lider serão perdidas.
	- Mensagens enviadas ao consumidor que a fila não recebeu a confirmação de  consumo serão reenfileiradas.
	- neste caso, o espelho considera que todos os consumidores foram abruptamente desconectados.

## configurações:
* Feita via policy, setando a tag `ha-mode` utilizando um regex para informar as filas que devem ser espelhadas.
* É  possivel informar quantos espelhos será configurado para cada policy
* É possivel informar em qual nó a fila lider residirá, informando o parametro `x-queue-master-locator`.
* Também é possivel informar um numero minimo e máximo de filas lider por nó em seu ar

# Filas Quorum:
* Implementação baseada no algoritmo de consenso raft. 
# References:
* https://raft.github.io (simulação interativo no browser)
* http://thesecretlivesofdata.com/raft (bem explicativo, mas não tão interativo)

