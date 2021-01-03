#Plus-minus calculator package
## Description (English)
This package allows you to perform calculations on numbers with uncertainty and print them

####Formulas, used for calculations of uncertainties for operations:

#####All equations are written up to the first infinitesimal order

__Legend:__

*A* - first number in operation \
*&Delta;A* - uncertainty of first number \
*B* - second number in operation \
*&Delta;B* - uncertainty of second number

- "&#177;" (*A* &pm; *&Delta;A*) + (*B* &pm; *&Delta;B*) = (*A* &pm; *B*) &pm; (*&Delta;A* + *&Delta;B*)
- "&times;/&div;" (*A* &pm; *&Delta;A*) &times;/&div; (*B* &pm; *&Delta;B*) = (*A* &times;/&div; *B*) &pm; (*&Delta;A* &div; *A* + *&Delta;B* &div; *B* + *&Delta;A* &times; *&Delta;B* &div; (*A* &times; *B*)) &simeq; (*A* &times;/&div; *B*) &pm; (*&Delta;A* &div; *A* + *&Delta;B* &div; *B*)
- "^" (*A* &pm; *&Delta;A*) ^ (*B* &pm; *&Delta;B*) = *A* ^ (*B* &times; (1 &pm; *&Delta;B* &div; *B*)) &times; (1 &pm; *&Delta;A* /&div; *A*) ^ (*B* &times; (1 &pm; *&Delta;B* &div; *B*)) &simeq; (*A* ^ *B* &pm; *A* ^ *B* &times; *B* &times; *&Delta;B* &times; log(*A*)) &times; ((1 &pm; *&Delta;A*) ^ *B* &pm; (1 &pm; *&Delta;A*) ^ *B* &times; *B* &times; &Delta;B &times; log(1 &pm; *&Delta;A*)) &simeq; *A* ^ *B* &pm; (*B* &times; *&Delta;A* &times; *A* ^ (*B* - 1) + *&Delta;B* &times; log(*A*) &times; *A* ^ *B*)

## Описание (Русский)
Эта библиотека позволяет производить вычисления над числами с погрешностями и выводить из в текстовом виде

####Формулы, используемые для вычисления:

#####Все уравнения написаны с точностью до первого порядка малости (включительно)

__Условные обозначения:__

*A* - первое число \
*&Delta;A* - погрешность первого числа \
*B* - второе число \
*&Delta;B* - погрешность второго числа

- "&#177;" (*A* &pm; *&Delta;A*) + (*B* &pm; *&Delta;B*) = (*A* &pm; *B*) &pm; (*&Delta;A* + *&Delta;B*)
- "&times;/&div;" (*A* &pm; *&Delta;A*) &times;/&div; (*B* &pm; *&Delta;B*) = (*A* &times;/&div; *B*) &pm; (*&Delta;A* &div; *A* + *&Delta;B* &div; *B* + *&Delta;A* &times; *&Delta;B* &div; (*A* &times; *B*)) &simeq; (*A* &times;/&div; *B*) &pm; (*&Delta;A* &div; *A* + *&Delta;B* &div; *B*)
- "^" (*A* &pm; *&Delta;A*) ^ (*B* &pm; *&Delta;B*) = *A* ^ (*B* &times; (1 &pm; *&Delta;B* &div; *B*)) &times; (1 &pm; *&Delta;A* /&div; *A*) ^ (*B* &times; (1 &pm; *&Delta;B* &div; *B*)) &simeq; (*A* ^ *B* &pm; *A* ^ *B* &times; *B* &times; *&Delta;B* &times; ln(*A*)) &times; ((1 &pm; *&Delta;A*) ^ *B* &pm; (1 &pm; *&Delta;A*) ^ *B* &times; *B* &times; &Delta;B &times; ln(1 &pm; *&Delta;A*)) &simeq; *A* ^ *B* &pm; (*B* &times; *&Delta;A* &times; *A* ^ (*B* - 1) + *&Delta;B* &times; ln(*A*) &times; *A* ^ *B*)