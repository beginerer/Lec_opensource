def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculator():
    print("덧셈/뺄셈 계산기")
    
    # 사용자로부터 두 숫자 입력받기
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))
    
    # 연산 선택
    operation = input("덧셈은 +, 뺄셈은 - 를 입력하세요: ")
    
    # 연산 수행 및 결과 출력
    if operation == '+':
        print(f"결과: {num1} + {num2} = {add(num1, num2)}")
    elif operation == '-':
        print(f"결과: {num1} - {num2} = {subtract(num1, num2)}")
    else:
        print("잘못된 연산입니다.")

# 계산기 실행
calculator()
