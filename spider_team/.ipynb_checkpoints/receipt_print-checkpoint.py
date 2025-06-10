# 영수증 프린트 함수
def print_receipt(store_name, cart_list):
    print("=" * 42)
    print(align_text(store_name, 42, 'center'))
    print("-" * 42)
    now = datetime.now()
    print(f"주문일시 : {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 42)
    print(f"{align_text('메뉴', 18)}{align_text('수량', 6, 'right')}"
          f"{align_text('단가', 9, 'right')}{align_text('금액', 9, 'right')}")
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
    print(f"{align_text('합계', 33)}{align_text(f'{total-vat:,}', 9, 'right')}")
    print(f"{align_text('부가세(10%)', 33)}{align_text(f'{vat:,}', 9, 'right')}")
    print(f"{align_text('총 결제금액', 33)}{align_text(f'{total:,}', 9, 'right')}")
    print("-" * 42)
    if last_membership :
      print(f'적립번호 뒷자리:{last_membership[-4:]}  적립포인트:{membership_dict[last_membership]} Point')
    else:
      print('    membership 번호가 없어서 아ship😭')

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