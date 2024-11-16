import sys

def main():
    input = sys.stdin.read  # 전체 입력을 한 번에 읽기
    data = input().splitlines()  # 각 라인마다 분리하여 저장
    
    command_number = int(data[0])  # 첫 번째 줄은 명령의 수
    stack = []  # 스택 초기화
    output = []  # 출력 결과를 저장할 리스트
    
    # 1번부터 command_number까지 처리
    for i in range(1, command_number + 1):
        cmd = data[i].split()  # 각 명령을 공백으로 분리
        if cmd[0] == '1':  # '1 X' 명령
            stack.append(cmd[1])  # 스택에 값 추가
        elif cmd[0] == '2':  # '2' 명령
            if stack:
                output.append(stack.pop())  # 스택에서 값 제거하고 출력
            else:
                output.append('-1')  # 스택이 비어있으면 -1 출력
        elif cmd[0] == '3':  # '3' 명령
            output.append(str(len(stack)))  # 스택의 크기 출력
        elif cmd[0] == '4':  # '4' 명령
            if not stack:
                output.append('1')  # 스택이 비어있으면 1 출력
            else:
                output.append('0')  # 스택이 비어있지 않으면 0 출력
        elif cmd[0] == '5':  # '5' 명령
            if stack:
                output.append(stack[-1])  # 스택의 맨 위 값 출력
            else:
                output.append('-1')  # 스택이 비어있으면 -1 출력

    # 결과를 한 번에 출력 (입출력 최적화)
    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == "__main__":
    main()