# divisor로 나누어 떨어지는 값을 리스트로반환, 나누어 떨어지는 값이 없다면 [-1] 반환.

def solution(arr, divisor):
    answer = []

    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    if len(answer) == 0:
        answer.append(-1)

    return answer

arr = [1,5,20,33]
divisor = 5
print(solution(arr, divisor))