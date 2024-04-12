def solution(dots):
    # 각 꼭짓점의 x, y 좌표를 변수로 저장합니다.
    x1, y1 = dots[0]
    x2, y2 = dots[1]
    x3, y3 = dots[2]
    x4, y4 = dots[3]
    
    # 직사각형의 넓이를 계산합니다. 넓이 = 가로 길이 * 세로 길이
    width = max(x1, x2, x3, x4) - min(x1, x2, x3, x4)  # 가로 길이는 x 좌표의 최대값과 최소값의 차이입니다.
    height = max(y1, y2, y3, y4) - min(y1, y2, y3, y4)  # 세로 길이는 y 좌표의 최대값과 최소값의 차이입니다.
    
    # 넓이를 반환합니다.
    return width * height