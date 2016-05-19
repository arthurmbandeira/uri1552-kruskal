from sys import stdin
import math

def makeSet(vertice):
	pai[vertice] = vertice
	ranking[vertice] = 0

def encontrar(vertice):
	if(pai[vertice] != vertice):
		pai[vertice] = encontrar(pai[vertice])
	return pai[vertice]

def unir(vertice1, vertice2):
	raiz1 = encontrar(vertice1)
	raiz2 = encontrar(vertice2)
	if raiz1 != raiz2:
		if (ranking[raiz1] > ranking[raiz2]):
			pai[raiz2] = raiz1
		else:
			pai[raiz1] = raiz2
			if ranking[raiz1] == ranking[raiz2]:
				ranking[raiz2] += 1

def kruskal(grafo):
	total = 0
	for vertice in grafo.keys():
		makeSet(vertice)
	arestas = criaArestas(grafo)
	edges = list(arestas.items())
	edges.sort(key=lambda x: x[1])
	for aresta in edges:
		vertice1, vertice2 = aresta[0]
		if encontrar(vertice1) != encontrar(vertice2):
			unir(vertice1, vertice2)
			total += aresta[1]
	print ('%.2f' % (total/100))

def ler(linha):
	line = stdin.readline()
	spt = line.split()
	x = int(spt[0])
	y = int(spt[1])
	if (0 <= x <= (10**4)) or (0 <= y <= (10**4)):
		G[j] = (x, y)
		return G
	else:
		print('%.2lf' % 0)
		return

def criaArestas(grafo):
	aresta = dict()
	for vertice1 in grafo.keys():
		for vertice2 in grafo.keys():
			if (vertice1 != vertice2) and ((vertice1, vertice2) not in aresta) and ((vertice2, vertice1) not in aresta):
				distY = math.pow(grafo[vertice1][1] - grafo[vertice2][1], 2)
				distX = math.pow(grafo[vertice1][0] - grafo[vertice2][0], 2)
				aresta[(vertice1, vertice2)] = math.sqrt(abs(distY + distX))
	return aresta

ranking = dict()
pai = dict()
G = dict()
c = int(stdin.readline())
for i in range(c):
	n = int(stdin.readline())
	if n <= 500:
		for j in range(n):
			ler(j)
		kruskal(G)
		G.clear()
	else:
		print('%.2lf' % 0)