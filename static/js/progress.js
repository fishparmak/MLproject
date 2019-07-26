(function(global, factory){ // Создание JS модуля для API
    'use strict'; //strict mode
   
    global.Progress = factory; //присоединить апи к global (в нашем случае - к Window)
   })(this, function () {
       return new Progress(parentNode = [], state = 'normal'); // возвращаем новую сущность Progress
       function Progress(parentNode= [], state = 'normal') {
           this.state = state; //состояние чарта
           this.value; // значение прогресса в процентах
           this.parentNode = parentNode; // node, внутри которого создаем наш чарт
           var progressRunner; // бегунок, отображающий значение диаграммы
           var progressBlock; //вся диаграмма

           this.drawChart = function (rad=9) { // метод для рендеринга диаграммы
               var circumference = 2*Math.PI*rad; // расчитываем длину окружности по небезыствестной формуле
               var strokeLength = (this.value*circumference)/100; // сколько нужно заполнить, чтобы отобразить процент
               this.parentNode[0].innerHTML = '<svg class="progress" viewbox="0 0 20 20" width="200" height="200">' +
               '<circle class="progress__field" stroke="#bfbfbf" stroke-width="1" fill="none" cx="10" cy="10" r='+rad+' />' +
               '<circle class="progress__runner" stroke="#fce112" stroke-width="1" stroke-dasharray="' + strokeLength +',' + circumference + '" stroke-linecap="round" fill="none" cx="10" cy="10" r='+rad+' /></svg>';
               // в место назначения добавляем html код (рендерим саму диаграмму)    
               var child = this.parentNode[0].childNodes[0]; // достаем детей в родительском ноде(диаграмму и бегунок)
                if(child.className.baseVal=='progress'){  // чтобы не затронуть другие диаграммы вне родительского нода(использующие эту же библиотеку) 
                    progressRunner = child.childNodes[1];
                    progressBlock = child;
                }
               return this; // возвращаем эту же сущность (Progress) для возможности использования цепи(ex: p.drawChart().setMod('animated))
           }
           this.setMod = function (state, prm) { // метод для установки состояния
               state = state.toLowerCase(); 
               prm = prm.toLocaleLowerCase();
              switch(state){
                  case 'animated':
                      progressBlock.style.display = 'inline-block'; // отображаем диаграмму
                      if(prm=='yes'){
                          this.state = state;
                          this.drawChart(); //рендерим анимацию
                          addAnimation(); // добавляем класс в html код для создания анимации
                        }
                        else {
                            // console.log('here');
                            progressBlock.style.display = 'inline-block';
                            hideAnimation();
                            this.drawChart();
                            this.state='normal' // переводим диаграмму в 'нормальное' состояние, в котором можно регулировать значение
                        }
                        break;
                  case 'hidden':
                      if(prm=='yes') {
                        progressBlock.style.display = 'none'; // скрываем видимость нашей диаграммы
                        this.state = state;
                      }
                      else {
                        this.state = 'normal';
                        progressBlock.style.display = 'inline-block'; // отображаем диаграмму
                      }
                      break;
                  default: throw('Error');
              }
               return this;
           }
           this.setValue = function (value) {
               if(this.state != 'normal') { // проверяем в нормальном ли состоянии (так как мы не можем менять значение в других случаях)
                   throw('Value can be changed only in the Normal state.') 
                   return this;
               }
               if(value>=0 && value<=100) { // проверяем валидность значения
                    this.value = value;
                    this.drawChart();
               }
               else {
                   throw('Invalid Value');
               }
                return this;
           }
           this.setNode = function (node) {
               this.parentNode = node;
               return this;
           }
           var addAnimation = function() {
               progressRunner.classList.add('progress__runner_animated'); // добавляем класс в html для создания анимации  
           }
           var hideAnimation = function() {
            progressRunner.classList.remove('progress__runner_animated'); // добавляем класс в html для создания анимации  
        }
       }
   })
   
