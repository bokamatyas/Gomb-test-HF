import math
from typing import List


def gömb_kalkulál(sugár: float) -> List:
    alap_tőke = 4 * math.pi
    felszín = alap_tőke * math.pow(sugár, 2)
    térfogat = (alap_tőke * math.pow(sugár, 3)) / 3
    if sugár <= 0:
        print('============================================')
        print('A sugár értéke nem lehet 0 vagy negatí érték!')
        exit()
    return [round(felszín, 3), round(térfogat, 3)]


print('Gömb felszín-térfogat számító program')
print('============================================')


def main() -> None:
    sugár = float(input('Kérem a gömb sugarát cm-ben: '))
    eredmény = gömb_kalkulál(sugár)
    print('============================================')
    print(f'A gömb felszíne/térfogata: {eredmény}')


if __name__ == '__main__':
    main()
