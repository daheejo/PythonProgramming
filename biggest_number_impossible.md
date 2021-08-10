# 7, 11, 17로 구성할 수 없는 가장 큰 수를 찾기 

## 어떤 수 N이 7, 11, 17을 조합하여 구성할 수 없는 최대의 수라면, N+1, N+2, N+3…은 모두 7, 11, 17을 조합하여 구성 가능한 숫자다.

- 30은 구성할 수 없음
- 31 ~ 36은 구성할 수 있음 (직접 해봤을 때)
- 37 구성 불가능
- '38~44' 구성 가능 ('31~36'이 구성 가능하기 때문에 7을 각각 하나씩 더 써서)
- 45 구성 가능
- 따라서 이후의 모든 수가 7, 11, 17을 조합하여 구성할 수 있으므로 정답은 37 

## 1. 단순 반복(Iteration)을 통한 해결

위 풀이를 적용한 가장 쉬운 알고리즘은 0부터 시작해서 하나씩 체크하면서 세 개의 input 중 가장 작은 수에 대해 그 수만큼의 연속한 숫자가 세 개의 input의 조합으로 구성 가능할 때까지 반복해 보는 것

1. 자연수 3개를 받을 함수 solver를 만든 다음, 그 중 가장 작은 수 minimum을 찾는다.

2. check_list가 minimum 이하일 때까지 while loop을 설정한다.

3. possible_range로 구성 가능한지 체크해 볼 조합의 범위를 각 input들에 대해 num을 각각 input1, input2, input3으로 나눈 몫으로 둔다.2

4. 기본적으로 구성 가능한지(feasibility)를 False로 두고, input1, input2, input3을 범위 내에서 조합하여 num을 구성할 수 있는지를 확인한다.

5. 확인하여 구성 가능하다면 feasibility를 True로 두고, check_list에 넣는다.

6. 모든 가능한 조합에서 num을 조합할 수 없다면 그대로 False로 두고, check_list를 비운다.3

7. 다음 num의 크기를 1씩 더해주며 계속 while loop을 돌리고, check_list에 minimum 수만큼 채워지면 check_list의 첫 번째 수보다 1 작은 값을 답으로 리턴한다.
```
def solver(input1, input2, input3):
    minimum = min([input1, input2, input3])
    check_list = []
    num = 0
    while len(check_list) <= minimum:
        possible_range = [num//input1, num//input2, num//input3]
        feasibility = False
        for i in range(0, possible_range[0] + 1):
            for j in range(0, possible_range[1] + 1):
                for k in range(0, possible_range[2] + 1):
                    if input1 * i + input2 * j + input3 * k == num:
                        check_list.append(num)
                        feasibility = True
                        break
                else:
                    continue
                break
            else:
                continue
            break
        if feasibility == False:
            check_list = []
        num += 1
    answer = check_list[0] - 1
    return answer

solution = solver(7, 11, 17)
print(solution)
```


## 2. 동적계획법(DP, Dynamic Programming)을 이용한 코드

위의 1번 코드는 생각하기는 쉽지만 연산 속도가 너무 오래 걸린다. 
예를 들어 100이 구성 가능한지를 7, 11, 17의 조합으로 확인하려면 최대 14*9*5 = 630번의 연산을 해야 하고, 101, 102, 103... 언제 끝날 지 모르는 연산을 계속해서 해야 한다면 연산 수는 엄청나게 늚

동적계획법(Dynamic Programming)을 사용한다면 더 쉽게 문제를 해결할 수 있습니다. 

7, 11, 17의 경우, 0부터 17까지만 체크해서 구성 가능 여부를 기록해 둔 다음, 18부터는 -7, -11, -17을 해 보았을 때 구성가능했는지를 확인해보면 됩니다. 이 때 구성 가능하다면, 그 뺀 수를 한 번 더 사용하면 구성 가능하다는 의미니까요. 그리고 계속해서 기록해 나가면 됩니다.

이 경우, 17까지만 체크하고 나니 그 뒤에는 기록했던 것을 체크해 보고 다시 기록을 추가하기만 하면 되니 연산이 아주 빨라지게 되겠죠?

1. memoization_table을 만들고 True를 하나 넣어 놓는다. (왜냐하면 0은 항상 조합 가능)

2. 1번 코드의 for문을 적용하여 세 개의 input 중 가장 큰 수까지 구성가능한지를 체크하며 memoization_table에 기록한다.

3. check_list가 다 채워질 때까지 while문을 1번 코드처럼 적용하되, 구성가능한지를 memoization_table을 이용해 판단한다.

*현재 num에서 input1 or input2 or input3를 뺀 수가memoization_table에서 구성 가능하다고 되어 있다면 거기서 input1or input2 or input3를 한 번 더 쓰면 현재 num이 나오므로 마찬가지로 구성 가능하다고 기록한다.

4. 다음 num의 크기를 1씩 더해주며 계속 while loop을 돌리고, check_list에 minimum수만큼 채워지면 check_list의 첫 번째 수보다 1 작은 값을 답으로 리턴한다.

```
def solver_DP(input1, input2, input3):
    minimum = min([input1, input2, input3])
    maximum = max([input1, input2, input3])
    memoization_table = [True]
    check_list = []

    for num in range(maximum):
        possible_range = [num//input1, num//input2, num//input3]
        memoization_table.append(False)
        for i in range(0, possible_range[0] + 1):
            for j in range(0, possible_range[1] + 1):
                for k in range(0, possible_range[2] + 1):
                    if input1 * i + input2 * j + input3 * k == num:
                        memoization_table[num] = True
                    break
            else:
                continue
            break
        else:
            num += 1
            continue
            break

    while len(check_list) <= minimum:
        memoization_table.append(False)
        if memoization_table[num - input1] \
            or memoization_table[num - input2] \
            or memoization_table[num - input3]:
            memoization_table[num] = True
            check_list.append(num)
        else:
            memoization_table[num] = False
            check_list = []
        num += 1

    answer = check_list[0] - 1
    return answer

solution = solver_DP(7, 11, 17)
print(solution)
```

위 방법의 경우 7, 11, 17일 때는 연산 속도가 크게 차이가 나지 않을 수 있지만 만약 큰 수에 대해 연산해야 한다면 어떨까요? 
예를 들어 553, 757, 901로 구성 불가능한 가장 큰 수를 찾아 볼까요?

solver(553, 757, 901)
solver_DP(553, 757, 901)

[출처] 실전편 ② 나를 먹어요 케이크 해답|작성자 엘리스코딩
