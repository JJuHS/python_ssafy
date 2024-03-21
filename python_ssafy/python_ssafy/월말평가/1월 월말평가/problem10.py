############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_position_safe(N, M, current):
    move_x = [-1,1,0,0]
    move_y = [0,0,-1,1]
    current_x, current_y = current
    
    if 0 <= (current_x + move_x[M]) < N and 0 <= (current_y + move_y[M]) < N:
        return True

    else:
        return False
    # 여기에 코드를 작성하여 함수를 완성합니다.



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(is_position_safe(3, 1, (0, 0))) # True
print(is_position_safe(3, 0, (0, 0))) # False

#####################################################
