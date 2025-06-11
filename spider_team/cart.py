
from data import cart, cart_list, size_price
from utils import get_valid_number_input


def print_cart():
    print("\n🛒 현재 장바구니:")
    for i, item in enumerate(cart_list, 1):
        print(f"{i}. {item['user_menu']} ({item['user_size']}) x{item['qty']} = {item['total_price']}원")

def show_cart_with_payment():
    from main import start
    from menu import menu_choice
    from data import cart_list, membership_dict
    from utils import get_valid_number_input
    from datetime import datetime
    import time
    from wcwidth import wcswidth

    def align_text(text, width, align='left'):
        text_width = wcswidth(text)
        space = width - text_width
        if space <= 0:
            return text
        if align == 'left':
            return text + ' ' * space
        elif align == 'right':
            return ' ' * space + text
        elif align == 'center':
            left = space // 2
            right = space - left
            return ' ' * left + text + ' ' * right

    def print_receipt(store_name, cart_list, member=None):
        print("=" * 42)
        print(align_text(store_name, 42, 'center'))
        print("-" * 42)
        now = datetime.now()
        print(f"주문일시 : {now.strftime('%Y-%m-%d %H:%M:%S')}")
        print("-" * 42)
        print(f"{align_text('메뉴', 18)}{align_text('수량', 6, 'right')}"
              f"{align_text('단가', 9, 'right')}{align_text('금액', 9, 'right')}")
        print("-" * 42)
        print("""⠀⠀⠀⠀
            。　 ඞ 。　 . •⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀
    ⠀🍨⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣿⣶⡄⠀⠀🍦
    ⠀⠀⠀⠀⠤⢀⠀⢸⠛⠋⠘⠛⠃⠙⢻⣿⣿⠀⠀⠀
    ⠀⠀⡌⠀⠀⠀⢣⢸⠀⠘⠀⠀⠘⠀⠀⢁⡹⠀⠀⠀     🍧
    ⠀⠀⠲⡖⠒⠒⡷⠀⡱⠤⣀⣁⣀⠤⠤⡈⠀⠀⠀⠀
    ⠀⠀⠀⠹⡄⡼⡀⣻⡜⠀⠀⠀⢀⠴⠦⢌⡆⠀⠀⠀🍫
    ⠀⠀⠀⠀⠙⠁⠈⠉⣷⣶⣶⣶⣾⣦⣤⠎⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠘⠒⠒⠈⠓⠒⠊⠀⠀⠀⠀⠀
  결제 감사합니다 😍 보고싶으니까 또와유~
            """)
        print("-" * 42)

        total = 0
        for item in cart_list:
            name = f"{item['user_menu']} ({item['user_size']})"
            qty = item['qty']
            price = item['price_per_item']
            amount = item['total_price']
            total += amount

            print(f"{align_text(name, 18)}"
                  f"{align_text(str(qty), 6, 'right')}"
                  f"{align_text(f'{price:,}', 9, 'right')}"
                  f"{align_text(f'{amount:,}', 9, 'right')}")

        vat = int(total * 0.1)

        print("-" * 42)
        print(f"{align_text('합계', 33)}{align_text(f'{total - vat:,}', 9, 'right')}")
        print(f"{align_text('부가세(10%)', 33)}{align_text(f'{vat:,}', 9, 'right')}")
        print(f"{align_text('총 결제금액', 33)}{align_text(f'{total:,}', 9, 'right')}")
        print("-" * 42)

        if member:
            print(f'적립번호 뒷자리:{member[-4:]}  적립포인트:{membership_dict[member]} Point')
        else:
            print('membership 번호가 없어서 아ship😭')
            print("=" * 42)
            print("""⠀⠀⠀⠀
            。　 ඞ 。　 . •⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀
    ⠀🍨⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣿⣶⡄⠀⠀🍦
    ⠀⠀⠀⠀⠤⢀⠀⢸⠛⠋⠘⠛⠃⠙⢻⣿⣿⠀⠀⠀
    ⠀⠀⡌⠀⠀⠀⢣⢸⠀⠘⠀⠀⠘⠀⠀⢁⡹⠀⠀⠀     🍧
    ⠀⠀⠲⡖⠒⠒⡷⠀⡱⠤⣀⣁⣀⠤⠤⡈⠀⠀⠀⠀
    ⠀⠀⠀⠹⡄⡼⡀⣻⡜⠀⠀⠀⢀⠴⠦⢌⡆⠀⠀⠀🍫
    ⠀⠀⠀⠀⠙⠁⠈⠉⣷⣶⣶⣶⣾⣦⣤⠎⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠘⠒⠒⠈⠓⠒⠊⠀⠀⠀⠀⠀
  결제 감사합니다 😍 보고싶으니까 또와유~
            """)
 

        print("=" * 42)

    if not cart_list:
        print("\n장바구니가 비어 있습니다.")
        print('-' * 50)
        start()
        return

    print_cart()
    print('-' * 50)

    while True:
        ask_mul = '1. 결제하기  2. 계속 쇼핑하기  0. 종료하기 '
        choice = get_valid_number_input(ask_mul, 0, 2)
        if choice == 1:
            total = sum(item['total_price'] for item in cart_list)
            print(f"\n총 결제 금액: {total:,}원")

            answer = input("결제하시겠습니까? (yes/no): ").strip().lower()
            if answer != 'yes':
                print("주문이 취소되었습니다.\n")
                return start()

            # 멤버십 적립
            member = input("멤버십 번호(전화번호 11자리): ").strip()
            if len(member) == 11 and member.isdigit():
                membership_dict[member] = membership_dict.get(member, 0) + 1
                print(f"{member}님 적립 완료! 총 {membership_dict[member]} 포인트\n")
            else:
                print("멤버십 정보 없음 또는 잘못된 번호")

            time.sleep(1)
            print_receipt("I Miss You Cram!🍦", cart_list, member)
            cart_list.clear()
            return start()

        elif choice == 2:
            return menu_choice()
        elif choice == 0:
            print("\n이용해주셔서 감사합니다! 좋은 하루 되세요! 👋")
            return start()



def del_cart():
    print_cart()
    idx = get_valid_number_input("삭제할 항목 번호 입력: ", 1, len(cart_list))
    if idx:
        del cart_list[idx - 1]
        print("🗑️ 삭제 완료!")

def cart_function():
    from menu import menu_choice  # ✅ 함수 내부에서 import
    from main import start        # ✅ 함수 내부에서 import

    try:
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
            choice = get_valid_number_input(cho_mul, 0, 3)
            if choice == 1:
                menu_choice()
                return
            elif choice == 2:
                show_cart_with_payment()
                return
            elif choice == 3:
                del_cart()
            elif choice == 0:
                print("\n이용해주셔서 감사합니다! 좋은 하루 되세요! 👋")
                print('-' * 50)
                start()
    except KeyError as e:
        print(f"⚠️ 키 오류: {e}")
    except Exception as e:
        print(f"⚠️ 오류 발생: {e}")
