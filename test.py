# 데이터 초기화
cart = {'user_menu': '', 'user_size': '', 'qty': ''}
cart_list = []
membership_dict = {}

menu_list = ['초코', '바닐라', '딸기', '우유', '말차', '민트초코']
size_price = {'S': 2000, 'M': 3000, 'L': 4000}
size_list = list(size_price.keys())

# 멤버십 적립 함수
def handle_membership():
    while True:
        member = input("멤버십을 적립하시겠습니까? (yes/no): ").strip().lower()
        if member not in ['yes', 'no']:
            print("yes 또는 no만 입력해주세요.")
            continue
        if member == 'no':
            print("멤버십 적립을 건너뜁니다.\n")
            return
        else:
            print("멤버십 적립을 선택하셨습니다.")
            while True:
                phone = input("전화 번호를 11자리를 입력하세요: ").strip()
                if len(phone) != 11 or not phone.isdigit():
                    print("전화번호가 올바르지 않습니다. 11자리 숫자만 입력해주세요.")
                    continue
                if phone in membership_dict:
                    print(f"기존 ({phone}) 번호의 멤버십이 있으므로 포인트를 적립했습니다.\n")
                else:
                    membership_dict[phone] = {}
                    print(f"새로운 ({phone}) 번호로 멤버십이 생성되었습니다.\n")
                return

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

# 장바구니 보기 및 결제
def function5():
    if not cart_list:
        print("\n장바구니가 비어 있습니다.")
        return
    print_cart()
    while True:
        choice = input("\n1. 결제하기  2. 계속 쇼핑하기  0. 종료\n선택: ")
        if choice == '1':
            total = sum(item['total_price'] for item in cart_list)
            print(f"\n총 결제 금액: {total:,}원")

            # 결제 여부 확인
            while True:
                answer = input("결제하시겠습니까? (yes/no): ").strip().lower()
                if answer not in ['yes', 'no']:
                    print("yes 또는 no만 입력해주세요.")
                    continue
                if answer == 'no':
                    print("주문이 취소되었습니다.\n")
                    return
                else:
                    break

            # 멤버십 적립 처리
            handle_membership()

            print("결제가 완료되었습니다. 감사합니다! 🍦\n")
            cart_list.clear()
            start()
            return

        elif choice == '2':
            function_1()
            return
        elif choice == '0':
            print("\n이용해주셔서 감사합니다! 좋은 하루 되세요! 👋")
            exit()
        else:
            print("⛔ 올바른 번호를 입력하세요 ⛔")

# 장바구니 상품 삭제
def function4():
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

# 장바구니에 추가 및 장바구니 기능 선택
def function_3():
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

    while True:
        choice = input("\n1. 계속 쇼핑하기  2. 장바구니 보기 및 결제  3. 장바구니에서 상품 삭제  0. 종료\n선택: ")
        if choice == '1':
            function_1()
            return
        elif choice == '2':
            function5()
            return
        elif choice == '3':
            function4()
        elif choice == '0':
            print("\n이용해주셔서 감사합니다! 좋은 하루 되세요! 👋")
            exit()
        else:
            print("⛔ 올바른 번호를 입력하세요 ⛔")

# 수량 선택
def function_2():
    while True:
        print("\n🍨 사이즈 및 가격\n")
        for i, (size, price) in enumerate(size_price.items()):
            print(f'{i + 1}. 사이즈: {size}, 가격: {price:,}원')
        size_index = int(input(f"\n원하시는 사이즈를 선택해주세요. (1~{len(size_price)}, 0:뒤로가기): "))

        if size_index == 0:
            print('\n뒤로 돌아갑니다 ⬅️')
            function_1()
            return
        if 1 <= size_index <= len(size_price):
            cart['user_size'] = size_list[size_index - 1]
            break
        else:
            print('⛔ 유효한 사이즈 번호를 입력하세요 ⛔')

    while True:
        qty = int(input("🤟 원하시는 개수를 적어주세요 (0:뒤로가기): "))
        if qty == 0:
            print('\n사이즈 선택으로 돌아갑니다 ⬅️')
            function_2()
            return
        if qty > 0:
            cart['qty'] = qty
            break
        else:
            print("⛔ 1개 이상 입력해주세요 ⛔")

    print('-' * 50)
    function_3()

# 메뉴 선택
def function_1():
    while True:
        print("\n📋 메뉴판\n")
        for index, name in enumerate(menu_list):
            print(f'{index + 1}. {name}')
        try:
            menu_index = int(input(f"\n원하시는 메뉴를 선택해주세요. (1~{len(menu_list)}, 0:처음으로): "))
        except ValueError:
            print("⛔ 숫자를 입력해주세요.")
            continue

        if menu_index == 0:
            print('\n보고싶을거예요 😭😭\n')
            start()
            return
        if 1 <= menu_index <= len(menu_list):
            cart['user_menu'] = menu_list[menu_index - 1]
            print('-' * 50)
            function_2()
            return
        else:
            print('⛔ 유효한 메뉴 번호를 입력하세요 ⛔')

# 시작 화면
def start():
    print('=' * 50)
    store_name = 'I Miss You Cram!🍦'
    print(f'        보고싶었어요! {store_name}')
    print('=' * 50)
    function_1()

# main
start()
