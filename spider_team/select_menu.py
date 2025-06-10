# 메뉴 및 데이터 초기화
menu_list = ['초코', '바닐라', '딸기', '우유', '말차', '민트초코']
size_price = {'S': 2000, 'M': 3000, 'L': 4000}
size_list = list(size_price.keys())

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

# 메뉴 선택
def menu_choice():
    while True:
        print("\n📋 메뉴판\n")
        for index, name in enumerate(menu_list):
            print(f'{index + 1}. {name}')

        menu_mul = f"\n원하시는 메뉴를 선택해주세요. (1~{len(menu_list)}, 0:처음으로): "
        menu_index = get_valid_number_input(menu_mul, 0, len(menu_list))  # 예외처리

        if menu_index is None:
            continue  # None일 경우 아무 처리 없이 다시 메뉴 선택

        if menu_index == 0:
            print('\n보고싶을거예요😭\n')
            print('-' * 50)
            start()
            return

        if 1 <= menu_index <= len(menu_list):
            cart['user_menu'] = menu_list[menu_index - 1]
            print('-' * 50)
            size_count()
            return