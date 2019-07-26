p = Progress(value=10); // создаем сущность объекта Progress (default in 'Normal' state)
p.setNode(document.getElementsByClassName('main__progress')); // обознаечем нод, внутри которого расположим диаграмму
 // ставим значение, которое собираемся отобразить
var valueInput = document.getElementById("valueInput"); // input элемент, принимающий значения
var hidden = document.getElementById("hidden"); // checkbox для скрытия блока
var animated = document.getElementById("animated"); // checkbox для создания анимации
var control = document.getElementsByClassName("control")[0]; // панель управления, на которую повесим eventListener
p.setValue(valueInput.value*100);
animated.checked = true;
// p.checked = true;
p.setMod('animated', 'yes')
control.addEventListener('change', function(e) { // в случае изменения
    const { target } = e; // получаем событие
      if (!target.id) { // предотвращаем ошибки
        e.stopPropagation();
    } else {
        if(target.id == 'animated') {
            if(target.checked==true) {
                hidden.checked = false;
                p.setMod('animated', 'yes'); // ставим диаграмму в состояние 'Animated'
            }
            else {
                p.setMod('animated', ''); // ставим диаграмму в состояние 'Normal'
                p.setValue(valueInput.value);
            }
        }
        else if(target.id == 'hidden') {
            if(target.checked==true) {
                animated.checked = false;
                p.setMod('hidden', 'yes'); // ставим диаграмму в состояние 'Hidden'
            }
            else {
                p.setMod('hidden', ''); // ставим диаграмму в состояние 'Hidden'
            }
        }
        else if(target.id == 'valueInput') {
            hidden.checked = false;
            animated.checked = false;
            p.setMod('animated', ''); // переключаем в 'Normal state' в случае изменения значения
            p.setValue(target.value); // ставим значение
        }
        else {
            throw('EventListener Error');
        }
        }
});
