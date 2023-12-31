# Функциональное программирование


# Парадигмы программирования и функциональное программирование

# Парадигма описывает общий подход к решению большой сложной задачи

# - Императивное программирование: описывается последовательность непосредственно инструкций
# /которые изменяют состояние нашей программы, изменяют переменные/,
# а декомпозиция производится с помощью процедур и функций
# /Примерно так мы и писали программы. Мы обрабаытваели последовательностю команд./
#
# - Декларативное программирование: описывается задача и ожидаемый результат,
# но не ее решение
# /Мы не пишем, как добиться результата. Мы ставим задачу и описываем, какой ответ хотим получить/
# /Пример: SQL/
#
# - Объектно-ориентированное программирование: программа манипулирует набором объектов,
# сохраняющих свое состояние на протяжении времени и имеющих набор методов для изменения
# этого состояния
# /В программе существуют объекты /рождаются с помощью конструктора, умирают в результате вызова декструктора,
# на протяжении жизни обладают каким-то состоянием и могут обмениваться информацией со всеми окружающими
# объектами посредством вызова публичных методов/
#
# - Функциональное программирование: решение задачи разбивается на набор функций, которые
# только принимают параметры и возвращают значения, не изменяя состояния объектов
# /Большая задача разбивается на некоторые элементарные функции, сквозь которыъ течет поток данных.
# Таким образом, мы просто описываем небольшую функцию, которыая принимает на вход какие-то данные
# и возвращает какие-то данные. Никакое состояние общее программы при этом не изменяется./
# /Подходит для работы с потоками данных. Например, обработка видео или аудио, гле поток аудио или видео
# течет сквозь разные функции./


# Радикальный функциональный стиль: программа состоит только из вызова функций /даже переменных нет, только параметры/

# Плюсы функционального программирования
# - Легко доказать формальную корректность алгоритма /легко доказать математически/
# - Легко проводить декомпозицию /нарезать на элементарные функции/, отладку и тестирование
# - Легко автоматически проводить распараллеливание /выполнять на нескольких ядрах одновременно; если есть функция от двух
# параметров, один параметр считаем на одном ядре, другой - на другом ядре/, векторизацию /то есть мы посчитали какой-то
# результат выполнения умножения a * b + c, где всё это вектора, и затем мы может посчитать кусочек произведения a * b,
# и уже с этим обработанным кусочком параллельно начать складывать с вектором c/ и конвейеризацию /на конвейер кладем;
# если мы хотим обработать с помощью функций вектор значений, то есть список, по сути, и никак не зависеть от предыдущих значений
# операций, то мы может условно этот списочек нарезать по количеству ядер и каждый кусочек отдать читать отдельно/
#
# Минусы функционального программирования:
# - Сложно и непривычно думать в функциональном стиле
# /Придется думать в обратном порядке - от результата спускаться к исходным данным. Грубо говоря, вы сначала читаете что-то
# от входных данных, затем от этого результата вызываете еще какую-то функцию и так далее./

# Тем не менее приемы работы с векторами данных, с массивами данных с помощью функций очень широко применяются
# в стандартных библиотеках обработки данных и машинном обучении.

# Функциональное программирование подходит для задач, в которых есть "поток данных",
# переходящий из одной функции в другую


'''Языки программирования предлагают различные средства для декомпозиции задачи. 
Существует несколько парадигм программирования:

Императивное (структурное, процедурное) программирование: программы являются последовательностью инструкций, 
которые могут читать и записывать данные из памяти. При изучении предыдущих тем мы пользовались, в основном, 
императивной парадигмой. Ряд языков, такие как Паскаль (не Object Pascal) или C являются яркими предтавителями 
императивных языков.

Декларативное программирование: описывается задача и ожидаемый результат, но не описываются пути её решения. 
Ярким представителем является язык запросов к базам данных SQL: большая часть внутреннего устройства скрыта в СУБД, 
программист описывает только структуру базы данных и ожидаемый результат запросов.

Объектно-ориентированное программирование: программы манипулируют наборами объектов, при этом объекты обладают 
сохраняющимся во времени состоянием и методами для изменения этого состояния (или создания новых объектов). 
Мы познакомимся с ООП подробнее на одной из следующих лекций. Примером языка с объектно-ориентированной парадигмой 
является Java, ООП также поддерживается в Питоне и C++.

Функциональное программирование: задача разбивается на набор функций. В идеале, функции только принимают параметры 
и возвращают значения, не изменяя состояния объектов или программы. Представителем функциональных языков является Haskell.
Иногда, также, выделяют и другие парадигмы программирования.

Некоторые языки предназначены, в основном, для написания программ в рамках одной парадигмы, другие же поддерживают 
несколько парадигм. Например, Питон и C++ поддерживают различные парадигмы программирования. Разные части программы 
можно писать в разных парадигмах, например, использовать функциональный стиль для обработки больших данных, 
объектно-ориентированный подход для реализации интерфейса и императивное программирование для промежуточной логики.'''


'''Функциональное программирование

Несмотря на то, что в функциональном стиле писать достаточно сложно и непривычно, 
функциональное программирование имеет массу плюсов:

- Достаточно легко доказать формальную корректность алгоритмов. Хотя доказательство, даже для функциональных программ, 
часто намного длиннее, чем сама программа, но для фундаментальных алгоритмов, которые широко используются, 
лучше иметь формальное доказательство, чтобы не попадать в глупые ситуации. Строить формальные доказательства 
императивных программ намного сложнее.

- Для программ, написанных в функциональном стиле, легко проводить декомпозицию, отладку и тестирование. 
Когда вся программа разбита на функции, выполняющие элементарные действия, то их разработка и проверка занимает 
намного меньше времени.

- Для функциональных программ легко автоматически проводить распараллеливание, векторизацию и конвейеризацию.'''


'''Задача распараллеливания выполнения программ крайне актуальна сейчас, когда скорости ядер процессоров 
практически перестали расти. Единственным способом ускорить выполнение программ является их параллельное вычисление 
на нескольких устройствах.

Последние успехи в решении задач машинного обучения связаны с использованием большого количества простых 
вычислительных устройств, например, рассчетов на видеокарте.

В функциональных программах не принято вносить изменения в объекты (и, вообще говоря, желательно, 
чтобы все объекты были неизменямыми). Поэтому, если нам нужно посчитать результат вычисления двух функций, 
то во многих случаях можно делать это параллельно на разных ядрах процессора. 
Такое распараллеливание легко сделать автоматически.

Векторизация - это когда одни и те же действия выполномцяются над большим набором данных. 
Тогда данные можно нарезать на куски и раскидать по разным вычислительным устройствам, 
а затем собрать результат вычислений в один объект.

Конвейеризация - это разбиение вычислений на несколько этапов, причём данные поступают на следующий этап обработки 
по времени готовности. Например, если нам нужно попарно перемножить значения в векторах A и B, 
а затем сложить со значениями в векторе C, то мы можем посчитать несколько первых результатов подсчета произведения 
и уже выполнять с ними сложение, не дожидаясь подсчета остальных значений. Это позволяет быстрее получить первые результаты 
и занять еще большое количество вычислительных устройств параллельно.'''


# Подробнее о функциональном програмировании: http://www.intuit.ru/studies/courses/49/49/lecture/27062?page=1

