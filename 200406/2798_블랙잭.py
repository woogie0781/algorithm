a, b = list(map(int, input().split(' '))) #카드의 갯수, 
                                        #합이 넘지않으면서 가장 큰 숫자
n = list(map(int, input().split(' '))) #카드에 적힌 숫자

biggest = 0
c = []
n = sorted(n)
for i in range(a): #0~4
    for j in range(i+1, a):#1~4
        for k in range(j+1, a):#2~4
            if n[i]+n[j]+n[k] <= b:
                biggest = n[i]+n[j]+n[k]
                c.append(biggest)
print(max(c))

###### 내 코드 ####################


a, b = list(map(int, input().split(' '))) #카드의 갯수, 
                                        #합이 넘지않으면서 가장 큰 숫자
n = list(map(int, input().split(' '))) #카드에 적힌 숫자

biggest = 0
sum = 0
for i in range(a): #0~4
    for j in range(i+1, a):#1~4
        for k in range(j+1, a):#2~4
            sum = n[i]+n[j]+n[k]
            if sum <= b:
                biggest=max(biggest, sum)
print(biggest)

##### 동빈님 코드 #########
