# 장바구니 출력
def print_cart():
    if not cart_list:
        print("\n장바구니가 비어 있습니다.")
        return
    print("\n🛒 현재 장바구니:")
    for i, item in enumerate(cart_list, 1):
        print(f"{i}. {item['user_menu']} ({item['user_size']}) x {item['qty']}개 - {item['total_price']:,}원")
    total = sum(item['total_price'] for item in cart_list)
    print(f"총 합계: {total:,}원")
    print('-' * 50)
