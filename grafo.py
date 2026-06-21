import networkx as nx
import matplotlib.pyplot as plt

#Observação: A execução do código requer Python, Matplotlib e NetworkX instalados.

G = nx.Graph() #Criação do grafo

#Adicionando vértices (usuários)
G.add_nodes_from(["Alice", "Bob", "Carla", "Diana", "Ivo",'ana'])

#Adicionando arestas (amizades)
G.add_edges_from([("Alice", "Bob"), 
                  ("Alice", "Carla"), 
                  ("Bob", "Diana"), 
                  ("Carla", "Diana"), 
                  ("Diana", "Ivo"),
                  
                  ])

# Ajustando o tamanho da figura
plt.figure(figsize=(12, 7))  # Largura e altura em polegadas

# Visualização do grafo
nx.draw(G, with_labels=True, node_color='lightblue', node_size=2500, font_size=15)
plt.show()

#Análise do grafo
#Encontrando a centralidade (degree centrality)
centralidade = nx.degree_centrality(G)
print("Centralidade dos nós (influência):", centralidade)

#Encontrando o caminho mínimo entre dois usuários
caminho_minimo = nx.shortest_path(G, source="Alice", target="Ivo")
print("Caminho mínimo entre Alice e Ivo:", caminho_minimo)

#### CD​(v) = deg(v)​ / n-1