# 필요한 라이브러리 import
from datetime import datetime
from wcwidth import wcswidth
import time

# 메뉴 및 데이터 초기화
menu_list = ['초코', '바닐라', '딸기', '우유', '말차', '민트초코']
size_price = {'S': 2000, 'M': 3000, 'L': 4000}
size_list = list(size_price.keys())

cart_list = []
membership_dict = {}
cart = {'user_menu': '', 'user_size': '', 'qty': ''}

#숫자검증
def get_valid_number_input(msg, min_no=0, max_no=5):
    try:
        number = int(input('>>>' + msg).strip())
        if number < min_no:
            print(f'⚠️ {min_no} 이상 숫자를 입력하세요.')
            return None
        elif number > max_no:
            print(f'⚠️ {max_no} 이하 숫자를 입력하세요.')
            return None
        else:
            return number
    except ValueError:
        print('⚠️ 숫자로 입력하세요.')
        return None

# 유틸리티 함수
# yes or no
def get_yes_or_no_input(msg):
    while True:
        user_input = input('>>>' + msg + " (yes/no): ").strip().lower()
        if user_input in ['yes', 'no']:
            return user_input
        else:
            print("⚠️'yes' 또는 'no'만 입력할 수 있어요.")

# 장바구니에 추가 및 장바구니 기능 선택(select_shopping_cart)
from select_shopping_cart import cart_function

# 수량 선택
def size_count():
    while True:
        print("\n🍨 사이즈 및 가격\n")
        for i, (size, price) in enumerate(size_price.items()):
            print(f'{i + 1}. 사이즈: {size}, 가격: {price:,}원')
        size_mul = f"\n원하시는 사이즈를 선택해주세요. (1~{len(size_price)}, 0:뒤로가기): "
        size_index = get_valid_number_input(size_mul, 0,3 )## 예외처리 (0~3)

        if size_index is None:
            print("⛔입력 오류⛔ 사이즈 다시 선택하세요.")

        elif size_index == 0:
            print('\n⬅️ 뒤로 돌아갑니다')
            print('-' * 50)
            menu_choice()
            return
        elif 1 <= size_index <= len(size_price):
            cart['user_size'] = size_list[size_index - 1]
            break
    while True:
        qty_mul = "🤟 원하시는 개수를 적어주세요. (0:뒤로가기) \n 10개 이하만 가능!: "
        qty = get_valid_number_input(qty_mul, 0, 10) ## 예외처리 (0~10) 성공
        if qty == None:
            continue
        if qty == 0:
            print('\n⬅️ 사이즈 선택으로 돌아갑니다')
            print('-' * 50)
            size_count()
            return
        if qty > 0:
            cart['qty'] = qty
            break
    print('-' * 50)
    cart_function()