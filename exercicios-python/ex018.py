from math import sin, cos, tan, radians
ang = int(input('Digite um ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print(
    f'\033[96mSeno\033[m de {ang}º é \033[1;96m{sen:.4f} '
    f'\033[m \n\033[94mCosseno\033[m de {ang}º é \033[1;94m{cos:.4f}\033[m '
    f'\n\033[95mTangente\033[m de {ang}º é \033[1;95m{tan:.4f}\033[m')
