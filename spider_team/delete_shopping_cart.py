# 장바구니 상품 삭제
def del_cart():
    if not cart_list:
        print("\n장바구니가 비어 있습니다.")
        return
    print_cart()
    try:
        idx = int(input("삭제할 상품 번호를 입력하세요 (취소하려면 0 입력): "))
        if idx == 0:
            print("삭제를 취소했습니다.")
            return
        if 1 <= idx <= len(cart_list):
            removed = cart_list.pop(idx - 1)
            print(f"{removed['user_menu']} ({removed['user_size']}) x {removed['qty']}개가 장바구니에서 삭제되었습니다.")
        else:
            print("⛔ 유효한 번호를 입력하세요.")
    except ValueError:
        print("⛔ 숫자를 입력해주세요.")