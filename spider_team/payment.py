# 장바구니 보기 및 결제
def show_cart():
    if not cart_list:
        print("\n장바구니가 비어 있습니다.")
        print('-' * 50)
        start()
        return
    print_cart()
    print('-' * 50)

    while True:
        ask_mul = '1. 결제하기  2. 계속 쇼핑하기  0. 종료하기 '
        choice = get_valid_number_input(ask_mul, 0, 2) ## 예외처리 (0~3)
        if choice == 1:
            total = sum(item['total_price'] for item in cart_list)
            print(f"\n총 결제 금액: {total:,}원")

            answer = get_yes_or_no_input("결제하시겠습니까? (yes/no): ") #예외처리 (yes or no)
            if answer not in ['yes', 'no']:
                print("yes 또는 no만 입력해주세요.")
                continue
            elif answer == 'no':
                print("주문이 취소되었습니다.\n")
                return start()

            # 멤버십 적립 처리
            handle_membership()
            print("결제가 완료되었습니다. 감사합니다! 🍦\n")
            print("ඞඞඞඞඞඞඞ 로딩중 ඞඞඞඞඞඞඞ")
            print("""⠀
            로딩중~~⠀⠀⠀
            。　 ඞ 。　 . •⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀
    ⠀🍨⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣿⣶⡄⠀⠀🍦
    ⠀⠀⠀⠀⠤⢀⠀⢸⠛⠋⠘⠛⠃⠙⢻⣿⣿⠀⠀⠀
    ⠀⠀⡌⠀⠀⠀⢣⢸⠀⠘⠀⠀⠘⠀⠀⢁⡹⠀⠀⠀     🍧
    ⠀⠀⠲⡖⠒⠒⡷⠀⡱⠤⣀⣁⣀⠤⠤⡈⠀⠀⠀⠀
    ⠀⠀⠀⠹⡄⡼⡀⣻⡜⠀⠀⠀⢀⠴⠦⢌⡆⠀⠀⠀🍫
    ⠀⠀⠀⠀⠙⠁⠈⠉⣷⣶⣶⣶⣾⣦⣤⠎⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠘⠒⠒⠈⠓⠒⠊⠀⠀⠀⠀⠀
  결제 중입니다 😍
    """)

            time.sleep(3)
            print('=' * 50)


            print("결제가 완료되었습니다. 감사합니다! 🍦\n")
            print_receipt("I Miss You Cram!🍦", cart_list)
            cart_list.clear()
            start()
            return

        elif choice == 2:
            return menu_choice()
        elif choice == 0:
            print("\n이용해주셔서 감사합니다! 좋은 하루 되세요! 👋")
            start()