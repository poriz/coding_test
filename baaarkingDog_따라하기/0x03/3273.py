# 문제의 key는 서로 다른 양의 정수이다...
n = int(input())
l1 = list(map(int, input().split()))
x = int(input())

l1.sort() # 리스트를 오름차순으로 정렬
left, right = 0, n - 1 # 두 포인터 초기화
answer = 0

while left < right: # 두 포인터가 만나지 않을 때까지 반복
    current_sum = l1[left] + l1[right]
    if current_sum == x: # 두 수의 합이 x와 같으면, 쌍의 수를 증가시키고 포인터 이동
        answer += 1
        left += 1
        right -= 1
    elif current_sum < x: # 두 수의 합이 x보다 작으면, 왼쪽 포인터를 증가
        left += 1
    else: # 두 수의 합이 x보다 크면, 오른쪽 포인터를 감소
        right -= 1

print(answer)