import numpy as np
from timeit import default_timer as timer

try:
    CSVData = open("graph.csv")
    res = np.genfromtxt(CSVData, delimiter=" ", dtype='int')
    res = np.delete(res, (2,3), axis=1)
    for i in res:
        for j in i:
            if (int(j) < 0):
                raise ValueError
    n,m = res[0]
    ress = np.delete(res, 0 ,0)
except ValueError:
    print("Wrong data")
    quit()

def sumj(re):
    mat =np.zeros((n,n), dtype ='int')
    for i in re:
        mat[i[0]-1][i[1]-1] = 1
        mat[i[1]-1][i[0]-1] = 1
    return mat

def ssum(mat):
    dic = {}
    for i in range(0,n):
        for j in range(0,n):
            if i+1 not in dic.keys():
                dic[i+1]=[]
                if mat[i][j]==1:
                     dic[i+1].append(j+1)
            else:
                if mat[i][j]==1:
                     dic[i+1].append(j+1)
    return dic

def bfs(graph, node, visited = list(), queue=list(), printlist=[]):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        printlist.append(m)
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return printlist

matsum = sumj(ress)

def main():
    try:
        start =  int(input("Введіть вершину з якої починати пошук: "))
        assert 1<= start <= 18
    except Exception:
        print("Wrong data")
        quit
    start_time = timer()
    bfs_search = bfs(ssum(matsum), start)
    end_time = timer()
    print('DFS обхід графу:', *bfs_search)
    print('Час на виконання програми:', (end_time - start_time)*1000, 'мс')

if __name__ == '__main__':
    main()



