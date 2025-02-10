import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import fsolve

# Данные из таблицы 6.3
расход = np.array([500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500])
потери_ДТ = np.array([1203, 1598, 2051, 2560, 3126, 3747, 4423, 5153, 5937, 6774, 7666])
потери_А76 = np.array([889, 1186, 1536, 1937, 2389, 2893, 3448, 4055, 4713, 5422, 6184])
потери_ТС1 = np.array([965, 1284, 1654, 2077, 2551, 3078, 3656, 4285, 4966, 5699, 6483])
напор_станций_8 = np.array([6356, 6238, 6099, 5938, 5756, 5552, 5327, 5081, 4813, 4524, 4213])

# Интерполяция данных
f_потери_ДТ = interp1d(расход, потери_ДТ, kind='cubic')
f_потери_А76 = interp1d(расход, потери_А76, kind='cubic')
f_потери_ТС1 = interp1d(расход, потери_ТС1, kind='cubic')
f_напор_станций_8 = interp1d(расход, напор_станций_8, kind='cubic')

# Функции для нахождения пересечения
def find_intersection(f1, f2, x_range):
    def difference(x):
        return f1(x) - f2(x)
    return fsolve(difference, x_range)

# Находим точки пересечения
Q_ДТЛ = find_intersection(f_потери_ДТ, f_напор_станций_8, 1000)[0]
Q_А76 = find_intersection(f_потери_А76, f_напор_станций_8, 1000)[0]
Q_ТС1 = find_intersection(f_потери_ТС1, f_напор_станций_8, 1000)[0]

print(f"Расход ДТЛ: {Q_ДТЛ:.1f} м³/ч")
print(f"Расход А-76: {Q_А76:.1f} м³/ч")
print(f"Расход ТС-1: {Q_ТС1:.1f} м³/ч")

# Построение графиков
plt.figure(figsize=(10, 6))
plt.plot(расход, потери_ДТ, label='Потери напора ДТЛ')
plt.plot(расход, потери_А76, label='Потери напора А-76')
plt.plot(расход, потери_ТС1, label='Потери напора ТС-1')
plt.plot(расход, напор_станций_8, label='Суммарный напор станций (n=8)', linestyle='--')

# Отметим точки пересечения на графике
plt.scatter(Q_ДТЛ, f_потери_ДТ(Q_ДТЛ), color='red', zorder=5)
plt.scatter(Q_А76, f_потери_А76(Q_А76), color='green', zorder=5)
plt.scatter(Q_ТС1, f_потери_ТС1(Q_ТС1), color='blue', zorder=5)

# Подписи и легенда
plt.title('Совмещенная характеристика нефтепродуктопровода и насосных станций')
plt.xlabel('Расход, м³/ч')
plt.ylabel('Напор, м')
plt.legend()
plt.grid(True)
plt.show()