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


# 장바구니에 추가 및 장바구니 기능 선택
def cart_function():
    item = {
        'user_menu': cart['user_menu'],
        'user_size': cart['user_size'],
        'qty': cart['qty'],
        'price_per_item': size_price[cart['user_size']],
        'total_price': size_price[cart['user_size']] * cart['qty']
    }
    cart_list.append(item)

    print("\n🍦 장바구니에 추가되었습니다! 🍦")
    print_cart()
    print('-' * 50)

    while True:
        cho_mul = "\n1. 계속 쇼핑하기  2. 장바구니 보기 및 결제  3. 장바구니에서 상품 삭제  0. 종료\n선택: "
        choice = get_valid_number_input(cho_mul, 0, 3) ## 예외처리 (0~3)
        if choice == 1:
            menu_choice()
            return
        elif choice == 2:
            show_cart()
            return
        elif choice == 3:
            del_cart()
        elif choice == 0:
            print("\n이용해주셔서 감사합니다! 좋은 하루 되세요! 👋")
            print('-' * 50)
            start()