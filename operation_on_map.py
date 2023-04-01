def solution(maps):
    INF = int(1e9)
    graph = [[[] for j in range(len(maps[i]))] for i in range(len(maps))]
    visited = [[False for _ in range(len(maps[i]))] for i in range(len(maps))]
    distance = [[INF for _ in range(len(maps[i]))] for i in range(len(maps))]
    distance[0][0] = 1 #시작값 지정

    def nearby(): #이어진 노드에 graph를 작성해주는 함수
        for i in range(len(maps)):
            for j in range(len(maps[i])):
                for arrow in range(4):
                    if maps[i][j] == 1:
                        if arrow == 0 and i-1 >= 0 and maps[i-1][j] == 1: #왼쪽
                            graph[i][j].append((i-1, j, 1)) #대상 x, y, 거리는 1고정
                        elif arrow == 1 and i+1 < len(maps) and maps[i+1][j] == 1: #오른쪽
                            graph[i][j].append((i+1, j, 1))
                        elif arrow == 2 and j-1 >= 0 and maps[i][j-1] == 1  : #위쪽
                            graph[i][j].append((i, j-1, 1))
                        elif arrow == 3 and j+1 < len(maps) and maps[i][j+1] == 1: #아래쪽
                            graph[i][j].append((i, j+1, 1))
    nearby()

    def dijkstra(graph, visited, distance):
        n = 0
        while not allvisited(visited):
            x,y = findMinimum(distance, n) #n번째로 작은 노드를 찾기
            if not checkvisited(x,y, visited):#n번째로 작은 노드가 첫방문인지 확인 F:처음 T:처음아님
                #print(x,y,checkvisited(x,y,visited))
                currentx,currenty = x,y #현재 다루고 있는 노드 번호 
                #r이 접근할 수 있는 노드 중 가중치를 갱신 하였을 때 더 낮아지는 경우에만 갱신
                for v in graph[currentx][currenty]:
                    #print(v,"n:", n, "바뀔distance:",distance[currentx][currenty]+v[2]) #current에서의 목적지 노드 X축 v[0], 목적지 노드 Y축 v[1], 간선cost v[2]
                    if distance[v[0]][v[1]] > distance[currentx][currenty] + v[2]:
                        distance[v[0]][v[1]] = distance[currentx][currenty] + v[2]
                    visited[currentx][currenty] = True
            else: 
                n+=1
            #if not changed and n > 0:
             #   return False
        return distance

    def findMinimum(distance, n):
        temp = {}
        for i in range(len(distance)): #노드 번호가 0부터임으로 0~길이만큼
            for j in range(len(distance[i])):
                temp[str(i)+str(j)] = distance[i][j] # dict에 temp['ij']에 distance[i][j] 변수의 값을 대입시킴
        temp = sorted(temp.items(), key=lambda x:x[1]) #Value를 기준으로 정렬함
        temp = dict(temp)
        rstnumber = 0
        for i, _ in temp.items(): #순회하여 n번째로 작은 값을 반환
            if n == 0: # n이 0이면 n번째 작은 값을 찾아냄
                rstnumber = list(i) #문자열을 리스트화함
            n -= 1 # n번째로 작은 값을 반환하기 위해서 for문 안에서 1씩 줄여감.
        return int(rstnumber[0]), int(rstnumber[1])

    def checkvisited(i,j, visited):
        #print(visited[i][j])
        if visited[i][j] == False:
            return False
        else: return True
        
    def allvisited(visited): # all visited를 도달하지 못할때 적절하게 리턴하는 것만 만들면 될듯
        rst = True
        for i in range(len(visited)):
            for j in range(len(visited[i])):
                if maps[i][j]==1 and visited[i][j] == False: 
                    rst = False
        return rst

    #for i in range(len(graph)):
    #print(graph[i])
    rst = dijkstra(graph, visited, distance)
    if rst == False:
        return -1
    max = 0
    for i in range(0,len(rst)):
        print("node",i,":",rst[i]) #형식 출력
        for j in range(len(rst[i])):
            if max < rst[i][j] and maps[i][j] == 1:
                max = rst[i][j]
    return distance[len(distance)-1][len(distance)-1]

    
maps = [[1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1],
[0,0,0,0,1,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,0,1,0,0,0],
[0,0,0,0,1,0,0,0],
[0,1,1,1,1,1,1,1]]
print("rst: ",solution(maps))
