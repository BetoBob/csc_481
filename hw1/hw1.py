import snap
import gzip

# read the gzip file
with gzip.open("amazon0601.txt.gz", "rb") as f:
    data = f.read()

# write to txt as bytes
with open("amazon0601.txt", "wb") as f:
    f.write(data)

# Create A Graph Object
G = snap.LoadEdgeListStr(snap.PNGraph, "amazon0601.txt", 0, 1)

# Number of nodes in the graph 
print("Number of Nodes: %d" % G.GetNodes())

# Number of directed edges in the graph
Count = snap.CntUniqDirEdges(G)
print("Directed Graph: Count of unique directed edges: %d" % Count)

# Number of undirected edges in the graph
Count = snap.CntUniqUndirEdges(G)
print("Directed Graph: Count of unique undirected edges: %d" % Count)

# Number of nodes with zero out-degree 
Count = snap.CntOutDegNodes(G, 0)
print("Directed Graph: Count of nodes with out-degree 0: %d" % Count)

# Number of nodes with zero in-degree
Count = snap.CntInDegNodes(G, 0)
print("Directed Graph: Count of nodes with in-degree 0: %d" % Count)

# Number of nodes with more in-coming edges than out-going edges
Count = len([NI.GetId() for NI in G.Nodes() if NI.GetInDeg() > NI.GetOutDeg()])
print("Count of nodes with more in-degrees than out-degrees: %d" % Count)