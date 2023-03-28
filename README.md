# bot_quiz

#### Опрос 
Этот бот поможет вам в изучении одного или нескольких иностранных языков. Он может формировать опрос на основе вашего __.xlsx__ файла. 
<img src="images/2.jpg" 
    width="32%" height="32%" vspace="2" hspace="3"><img src="images/3.jpg" 
    width="32%" height="32%" vspace="2" hspace="3"><img src="images/4.jpg" 
    width="32%" height="32%" vspace="2" hspace="3">

После завершения опроса, выводится результат со словами на всех языках. Так же отображаются и неправильные варианты ответа, если они есть.
<img src="images/5.jpg" 
    width="32%" height="32%"
  vspace="4" hspace="3"> 

---

#### Режимы работы опроса 

* С фильтрацией по типу (с любого языка на любой язык)
* Без фильтрации
* Тестовый с фильтрацией по типу
* С ответом на "первый" язык с фильтрацией по типу 
* С ответом на "второй" язык с фильтрацией по типу
* С ответом на "третий" язык с фильтрацией по типу
* С ответом на "четвертый" язык с фильтрацией по типу


---

#### Работа с .xlsx файлом

Для начала работы необходимо отправить боту таблицу с расширением .xlsx. 1-4 колонка - соответствуют любым четырем языкам, заполнить нужно хотя бы две из них. В 5-7 колонку можно указать тип данного слова, по которому и будет происходить фильтрация при выборе варианта ответа, то есть все варианты ответа будут одного типа. Структура таблицы выглядит следующим образом:

lng | lng | lng | lng | type | type | type
:----|:----------:|:----------:|:----------:|:----------:|:----------:|--------:
просыпаться | wake | våkne | | verb
есть | eat | spise | | verb
хотеть | want | vil | | verb
далеко | far | langt | | adjective
около | near | nær | | adjective
далеко | far | langt | | adjective