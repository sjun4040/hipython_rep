
from data import cart, size_list, size_price
from utils import get_valid_number_input
from cart import cart_function

def size_count():
    while True:
        print("\n📏 사이즈 선택")
        for idx, size in enumerate(size_list):
            print(f"{idx + 1}. {size} - {size_price[size]}원")
        choice = get_valid_number_input("사이즈를 선택해주세요 (1~3): ", 1, 3)
        if choice:
            cart['user_size'] = size_list[choice - 1]
            break

    while True:
        qty = get_valid_number_input("수량을 입력해주세요 (1~10): ", 1, 10)
        if qty:
            cart['qty'] = qty
            break

    cart_function()
