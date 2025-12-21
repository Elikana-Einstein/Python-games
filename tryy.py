graph ={
    "A":{"B","J","M"},
    "B":{"F","C"},
    "C":{"E","D"},
    "D":{},
    "E":{},
    "F":{},
    "G":{},
    "H":{"I"},
    "I":{},
    "J":{"G"},
    "K":{"N","L"},
    "l":{},
    "N":{},
    "M":{"K","H"}
}


def depth_first_search(graph,startNode,target):
    to_visit = []
    path = []
    way=[]
    parent ={}
    def search(startNode,graph) :
        path.append(startNode)
        if graph.get(startNode):
            for node in graph.get(startNode):
                parent[node] = startNode
                if node == target:
                    path.append(node)
                    return path
                else:
                    to_visit.append(node)
            startNode = to_visit.pop()
            search(startNode,graph)
        else:
            startNode = to_visit.pop()
            search(startNode,graph)
    search(startNode,graph)
    target = path.pop()
    def reco_path(idx):
        way.append(idx)
        key = parent.get(idx)
        if key in path:
            reco_path(key)
    reco_path(target)
    print(way[::-1])


from queue import Queue


def breath_first_search(graph,startNode,target):
    path = []
    queue = Queue()
    parent ={}
    way = [target]

    def search(graph,startNode):
        if graph.get(startNode):
            for node in graph.get(startNode):
                if node == target:
                    path.append(node)
                    parent[node]=startNode
                    return path
                else:
                    queue.put(node)
                    path.append(node)
                    parent[node]=startNode
            while not  queue.empty():
                startNode = queue.get()
                search(graph,startNode)
    
    search(graph,startNode)
    def reco_path(idx):
        key = parent.get(idx)
        way.append(key)
        if key in path:
            reco_path(key)
    reco_path(target)
    return way[::-1]


k=breath_first_search(graph,"M","L")
print(k)




