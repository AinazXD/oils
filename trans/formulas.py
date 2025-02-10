import math

# Справочник плотностей и температурных поправок
DENSITY_CORRECTIONS = {
    "700-709": {"temperature_correction": 0.897},
    "710-719": {"temperature_correction": 0.884},
    "720-729": {"temperature_correction": 0.870},
    "730-739": {"temperature_correction": 0.857},
    "740-749": {"temperature_correction": 0.844},
    "750-759": {"temperature_correction": 0.831},
    "760-769": {"temperature_correction": 0.818},
    "770-779": {"temperature_correction": 0.805},
    "780-789": {"temperature_correction": 0.792},
    "790-799": {"temperature_correction": 0.778},
    "800-809": {"temperature_correction": 0.765},
    "810-819": {"temperature_correction": 0.752},
    "820-829": {"temperature_correction": 0.738},
    "830-839": {"temperature_correction": 0.725},
    "840-849": {"temperature_correction": 0.712},
    "850-859": {"temperature_correction": 0.669},
    "860-869": {"temperature_correction": 0.686},
    "870-879": {"temperature_correction": 0.673},
    "880-889": {"temperature_correction": 0.660},
    "890-899": {"temperature_correction": 0.647},
    "900-909": {"temperature_correction": 0.638},
    "910-919": {"temperature_correction": 0.620},
    "920-929": {"temperature_correction": 0.607},
    "930-939": {"temperature_correction": 0.594},
    "940-949": {"temperature_correction": 0.581},
    "950-959": {"temperature_correction": 0.567},
    "960-969": {"temperature_correction": 0.554},
    "970-979": {"temperature_correction": 0.541},
    "980-989": {"temperature_correction": 0.528},
    "990-999": {"temperature_correction": 0.515},
    "1000-1009": {"temperature_correction": 0.502},
    "1010-1019": {"temperature_correction": 0.489},
    "1020-1029": {"temperature_correction": 0.476},
    "1030-1039": {"temperature_correction": 0.463},
    "1040-1049": {"temperature_correction": 0.450},
    "1050-1059": {"temperature_correction": 0.437},
    "1060-1069": {"temperature_correction": 0.424},
    "1070-1079": {"temperature_correction": 0.411},
}




def get_temperature_correction(density_293):
    """
    Возвращает температурную поправку для заданной плотности при 293 К.
    """
    for range_, data in DENSITY_CORRECTIONS.items():
        start, end = map(int, range_.split('-'))
        if start <= density_293 <= end:
            return data["temperature_correction"]
    raise ValueError(f"Плотность {density_293} вне диапазона справочника")

def calculate_density_at_temperature(density_293, temperature):
    """
    Рассчитывает плотность при заданной температуре.
    """
    temperature_correction = get_temperature_correction(density_293)
    density_at_temperature = density_293 + temperature_correction * (293 - temperature)
    return round(density_at_temperature, 2)

def calculate_u(T1, T2, v1, v2):
    """
    Рассчитывает коэффициент крутизны вискограммы.
    """
    if T1 == T2:
        raise ValueError("Температуры T1 и T2 не должны быть равны.")
    if v1 <= 0 or v2 <= 0:
        raise ValueError("Вязкости v1 и v2 должны быть положительными числами.")
    return (1 / (T1 - T2)) * math.log(v2 / v1)

def calculate_viscosity_at_temperature(v_e, u, T, T_e=273):
    """
    Рассчитывает вязкость при заданной температуре.
    """
    if v_e <= 0:
        raise ValueError("Вязкость \( v_e \) должна быть положительным числом.")
    return v_e * math.exp(-u * (T - T_e))

def calculate_hourly_rate(products):
    """
    Рассчитывает часовой расход (О_{час}).
    """
    total = sum(
        (product['quantity'] * 10**9) / product['density_at_temperature']
        for product in products
        if product['density_at_temperature'] is not None
    )
    return total / 8400

def flow_rate(hourly_rate):
    """
    Рассчитывает расход \( Q \) в \( \text{м}^3/\text{с} \).
    """
    return hourly_rate / 3600

def calculate_reynolds_number(v, d, nu_p):
    """
    Рассчитывает число Рейнольдса.
    """
    return (v * d) / nu_p

def calculate_relative_roughness(delta, d):
    """
    Рассчитывает относительную шероховатость.
    """
    return delta / d

def calculate_transition_reynolds_numbers(epsilon):
    """
    Рассчитывает переходные числа Рейнольдса.
    """
    return 10 / epsilon, 500 / epsilon

def calculate_hydraulic_resistance(Re, epsilon):
    """
    Рассчитывает коэффициент гидравлического сопротивления в зависимости от режима течения.
    """
    if Re < 2320:
        # Ламинарный режим (формула Стокса)
        return 64 / Re
    elif 2320 <= Re <= 10 / epsilon:
        # Гидравлически гладкие трубы (формула Блазиуса)
        return 0.3164 / Re**0.25
    elif 10 / epsilon < Re <= 500 / epsilon:
        # Зона смешанного трения (формула Альтшуля)
        return 0.11 * (epsilon + 68 / Re)**0.25
    else:
        # Зона квадратичного трения (зависит только от шероховатости)
        return 0.11 * epsilon**0.25

def calculate_velocity(Q, d):
    """
    Рассчитывает среднюю скорость потока.
    """
    return (4 * Q) / (math.pi * d**2)

import math

def calculate_friction_head_loss(lambda_value, length_m, diameter_m, v, g=9.81):
    """
    Рассчитывает потерю напора на трение по формуле Дарси — Вейсбаха:
    \[
    h = \lambda \frac{L}{d} \frac{v^2}{2g}
    \]
    где:
    - \( \lambda \) — коэффициент гидравлического сопротивления,
    - \( L \) — длина трубопровода (м),
    - \( d \) — диаметр трубопровода (м),
    - \( v \) — средняя скорость потока (м/с),
    - \( g \) — ускорение свободного падения (м/с², по умолчанию 9.81).
    """
    return lambda_value * (length_m / diameter_m) * (v**2 / (2 * g))



def calculate_total_head_loss(friction_head_loss, elevation_difference, residual_head, N=2):
    """
    Рассчитывает полные потери напора в трубопроводе по формуле (5.28):
    \[
    H = 1,02 \cdot h_f + \Delta z + N \cdot H_{кп}
    \]
    где:
    - \( h_f \) — потери напора на трение (м),
    - \( \Delta z \) — перепад высот (м) (elevation_difference),
    - \( N \) — количество использований напора \( H_{кп} \),
    - \( H_{кп} \) — напор на станциях (м) (residual_head).
    """
    # Преобразуем elevation_difference в float, если это строка
    delta_z = float(elevation_difference)
    return 1.02 * friction_head_loss + delta_z + N * residual_head




