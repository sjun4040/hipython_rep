
from data import menu_list, cart
from utils import get_valid_number_input
from select_quantity import size_count

def menu_choice():
    if not menu_list:
        print("⚠️ 메뉴가 없습니다.")
        return

    while True:
        print("\n📋 메뉴판\n")
        for index, name in enumerate(menu_list):
            print(f'{index + 1}. {name}')

        try:
            menu_mul = f"\n원하시는 메뉴를 선택해주세요. (1~{len(menu_list)}, 0:처음으로): "
            user_input = input(menu_mul)
            menu_index = int(user_input)

            if menu_index == 0:
                print('\n보고싶을거예요😭\n')
                print('-' * 50)
                return
            elif 1 <= menu_index <= len(menu_list):
                cart['user_menu'] = menu_list[menu_index - 1]
                print('-' * 50)
                size_count()
                return
            else:
                print("⚠️ 메뉴 범위 내 숫자를 입력해주세요.")
        except ValueError:
            print("⚠️ 숫자만 입력해주세요.")
        except Exception as e:
            print(f"⚠️ 알 수 없는 오류: {e}")
