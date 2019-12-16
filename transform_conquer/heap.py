class Heap:
    def __init__(self, isMax):
        self.array = []
        self.isMax = isMax
        
    def insert(self, data):
        self.array.append(data)
        locate = len(self.array)-1
        while locate>0:
            parent = (locate-1)//2
            if (self.array[parent] > self.array[locate]) == self.isMax:
                break
            self.array[parent], self.array[locate] = self.array[locate], self.array[parent]
            locate = parent
    
    def pop(self):
        if len(self.array)==0:
            return -1
        locate = 0
        out = self.array[locate]
        self.array[locate] = self.array[len(self.array)-1]
        self.array.pop()
        while locate < len(self.array):
            left = locate*2+1
            right = locate*2+2
            if left>=len(self.array):
                break
            if right==len(self.array):
                if self.array[left]>self.array[locate] and self.isMax:
                    self.array[left], self.array[locate] = self.array[locate], self.array[left]
                break
            if self.isMax:
                if self.array[locate]>=self.array[left] and self.array[locate]>=self.array[right]:
                    break
                if self.array[right]>=self.array[left]:
                    self.array[right], self.array[locate] = self.array[locate], self.array[right]
                    locate = right
                else:
                    self.array[left], self.array[locate] = self.array[locate], self.array[left]
                    locate = left
            else:
                if self.array[locate]<=self.array[left] and self.array[locate]<=self.array[right]:
                    break
                if self.array[right]<=self.array[left]:
                    self.array[right], self.array[locate] = self.array[locate], self.array[right]
                    locate = right
                else:
                    self.array[left], self.array[locate] = self.array[locate], self.array[left]
                    locate = left
        return out

    def asort(self):
        while len(self.array)>0:
            print(self.pop(), end=" ")
        print()
    
    def status(self):
        print("현재 힙 상황")
        print("현재 힙은 {} 힙 입니다.".format("최대" if self.isMax else "최소"))
        slash=1
        for i in range(len(self.array)):
            print(self.array[i], end=' ')
            if i != len(self.array)-1:
                if i == 2**slash-2:
                    print('/', end=' ')
                    slash+=1
                else:
                    print(',', end=' ')
        print('\n총 노드 개수 : {}개'.format(len(self.array)))
    
# Main Part
print("어떤 힙을 실행해보겠습니까?")
isMax = input("1은 최대힙, 2는 최소힙입니다 : ")
isMax = True if isMax=="1" else False
my_heap = Heap(isMax)

while True:
    print('\n====MENU====')
    print('1. 데이터 추가')
    print('2. 데이터 삭제 (최상 노드만 가능)')
    print('3. 현제 힙 상태 보기')
    print('4. 데이터 모두 삭제 - 정렬 결과 확인 후 프로그램 종료')
    choice = int(input(' => '))
    print('\n'+'='*12+'\n')

    if choice==1:
        data = int(input("추가할 데이터를 입력하세요 (자연수) : "))
        my_heap.insert(data)
        print("추가되었습니다.\n")
    elif choice==2:
        data = my_heap.pop()
        if data == -1:
            print("빈 힙이기 때문에 데이터를 꺼낼 수 없습니다.")
        else:
            print("삭제된 데이터는 {}입니다.\n".format(data))
    elif choice==3:
        my_heap.status()
    elif choice==4:
        print('최종 힙 정렬은')
        my_heap.asort()
        print('입니다.')
        break
