from math import *


def Calculation_of_the_discriminant_and_the_roots_of_the_equation(a,b,c):
    D = b**2-4*a*c
    if D > 0:
        x1 = -b-sqrt(D)/2*a
        x2 = -b+sqrt(D)/2*a
        return print("Корни уравнения x1=", x1, "x2=", x2, "Дискрименант D=", D)
    elif D < 0:
        print("Коней нет так как Дискрименант D=", D)
    elif D == 0:
        x = -b/2*a
        return print("Корень уравнения x=", x, "Дискрименант D=", D)


def Calculation_of_the_probability_of_joint_events_and_non_joint_events(Am,An,Bm,Bn):
    PA = Am/An
    PB = Bm/Bn
    PA_plus_B_not_S = PA+PB # теорема сложения вероятностей несовместимых событий
    PA_plus_B_S = PA+PB-PA*PB # теорема сложения вероятностей совместимых событий
    return print("P(A)=", PA, "P(B)=", PB, "теорема сложения вероятностей несовместимых событий = ",
                 PA_plus_B_not_S, "теорема сложения вероятностей совместимых событий", PA_plus_B_S)
