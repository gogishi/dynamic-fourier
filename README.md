На левом холсте пользователь может рисовать мышкой график функции, масштаб которой задаётся посередине вверху.  График можно переделывать, не захваченные промежутки остаются нулевыми. Внизу находится кнопка обновления.

К функции можно применить какой-нибудь метод сглаживания с силой, вводимой пользователем, а можно ничего не применять. График показывается справа при нажатии на кнопку "Go!". Будьте осторожны с логарифмами размахов сглаживаний (длин промежутков, влияющих на значение сглаживания в одной точке) — их имеет смысл назначать только очень малыми числами.

Интерполяционное сглаживание выбирает в качестве опорных точки, идущие через каждые 2^n, и проводит через них гладкую кривую (то есть интерполирует их) по авторскому методу, сохраняющему уровень пиков, но не вызывающему чрезмерных заскоков. Сглаживание умным усреднением с параметром n — это (...((элементарное сглаживание)^2)^2...)^2, где возведения в квадрат композиционные, а всего их n. Элементарное сглаживание — замена значения в каждой точке на полусумму значения в ней и в соседней (то есть свёртка с [1, 1], а его квадрат — свёртка с [1, 2, 1] = [1, 1] * [1, 1] — уже симметричен).

Вишенка на торте — применение преобразования Фурье к сконструированной функции. Правда, вишенка ещё не выросла, декабрь-месяц на дворе, какие вишни, подснежников и то ещё не покушаешь.
