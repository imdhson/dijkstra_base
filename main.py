#다익스트라 알고리즘 구현
def dijkstra(graph, visited, distance):
    n = 0
    while not allvisited(visited):
        #print(visited)
        a = findMinimum(distance, n) #n번째로 작은 노드를 찾기
        if not checkvisited(a, visited):#n번째로 작은 노드가 첫방문인지 확인 F:처음 T:처음아님
            current = a
            #print(n, current) # 정상 작동 확인 !
            
            #r이 접근할 수 있는 노드 중 가중치를 갱신 하였을 때 더 낮아지는 경우에만 갱신
            for v in graph[current]:
                #print(type(v), v, v[0], v[1]) #current에서의 목적지 노드 번호 v[0], 목적지 노드 cost v[1]
                if distance[v[0]] > distance[current] + v[1]:  #지금 distance보다 작은 값이면 갱신
                    distance[v[0]] = distance[current] + v[1]
                #print(distance[1], v[0])
                visited[current] = True
            
        else: 
            n+=1
    return distance

def findMinimum(distance, n):
    #temp = copy.deepcopy(distance)
    temp = {}
    for i in range(1, len(distance)): #노드 번호가 1부터임으로 1~길이만큼
        temp[i] = distance[i] # dict에 temp['i']에 distance 변수의 i 값을 대입시킴
    temp = sorted(temp.items(), key=lambda x:x[1]) #Value를 기준으로 정렬함
    temp = dict(temp)
    rstnumber = 0
    #print(temp)
    for i, _ in temp.items(): #순회하여 n번째로 작은 값을 반환
        if n == 0: # n이 0이면 n번째 작은 값을 찾아냄
            rstnumber = i
        n -= 1 # n번째로 작은 값을 반환하기 위해서 for문 안에서 1씩 줄여감.
    return rstnumber

def checkvisited(i, visited):
    if visited[i] == False:
        return False
    else: return True
    
def allvisited(visited):
    rst = True
    for i in range(1, len(visited)):
        if visited[i] == False: 
            rst = False
    return rst

#입력 전체 노드, 전체 간선 수
node, lines = map(int, input("노드와 간선 수를 입력하세요: ").split())
#print("노드 수" , node)
#print("간선 수" , lines)
#출발 노드 번호 지정
start = int(input("출발 노드를 지정해주세요: "))

#무한 inf값을 지정 > 억, 10억
INF = int(1e9)
#그래프를 저장하는 리스트
graph = [ [] for i in range(node+1) ]

#방문 이력
visited = [False]* (node+1)

#최단 거리를 저장하는 리스트
distance = [INF] * (node+1)

#출발 지점을 0 으로 초기화
distance[start] = 0

#간선 정보를 입력
for _ in range (lines):
    node_a, node_b , cost = map(int, input("").split()) #현재 노드, 다음 노드, 비용
    graph[node_a].append((node_b, cost))
    graph[node_b].append((node_a, cost)) #양방향 그래프일 수 있음으로 반대로도 추가
    
    

rst = dijkstra(graph, visited, distance)
for i in range(1,len(rst)):
    print("node",i,":",rst[i], end="\n") #형식 출력
    #print(rst[i], end=", ") #간단하게 출력

#print(graph)
