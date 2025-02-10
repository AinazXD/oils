
# Примерные данные для расходов и соответствующих суммарных напоров для n=6,7,8
flows = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]

# Примерные параметры насоса
H_0 = 271  # Напор насоса при нулевом расходе (примерное значение)
a_0 = 43.9  # Коэффициент (примерное значение)
h_1 =59.9
b_0= 0.89
# Параметры подпорного насоса
N_3 = 2  # Количество подпорных насосов
# Расчет суммарных напоров для каждого расхода и количества станций
sum_h_n6_calculated = []
sum_h_n7_calculated = []
sum_h_n8_calculated = []

for Q in flows:
    # Расчет напора одного основного насоса (h_mn_main1)
    h_mn_main1 = H_0 - (a_0 * 10 ** -6 * Q ** 2)
    h2_booster = h_1 - (b_0 * 10 ** -5 * Q ** 2)

    # Расчет напора одной станции (H_st)
    H_st = 3 * h_mn_main1

    # Расчет суммарного напора для n=6,7,8
    sum_h_n6_calculated.append(N_3 * h2_booster + 6 * H_st)
    sum_h_n7_calculated.append(N_3 * h2_booster + 7 * H_st)
    sum_h_n8_calculated.append(N_3 * h2_booster + 8 * H_st)

# Вывод результатов
print("Суммарный напор для n=6:", sum_h_n6_calculated)
print("Суммарный напор для n=7:", sum_h_n7_calculated)
print("Суммарный напор для n=8:", sum_h_n8_calculated)
