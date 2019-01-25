/*
CODE LOGIC:
val__category() deserves a reason. I was unable to successfully use a loop(for OR forEach) to iterature through
the radio buttons for the purpose of generating an error message if one or none were selected.
It is not KISS logic nor DRY code, and I hope to revisit in the future so I can figure a most likley overlooked easy solution to my problem.
In the meantime, I used 4 separate classes one for each radio button and passed their values in as parameters in the sumAll() function
Enjoy...
*/

'use strict';

const MOD = (() => {

    // Global namespacing for easy future adjustment
    let DOM = {
        name: '.details__name',
        category_1: '.category1',
        category_2: '.category2',
        category_3: '.category3',
        category_4: '.category4',
        description: '.description',
        price: '.price',
        stock: '.stock',
        button: '.submit',
        form: '.form-details',
        element: '.element'
    }

    let name = document.querySelector(DOM.name);
    let sports = document.querySelector(DOM.category_1);
    let photo = document.querySelector(DOM.category_2);
    let lit = document.querySelector(DOM.category_3);
    let elect = document.querySelector(DOM.category_4);
    let desc = document.querySelector(DOM.description);
    let stock = document.querySelector(DOM.stock);
    let price = document.querySelector(DOM.price);
    let btn = document.querySelector(DOM.button);
    let form = document.querySelector(DOM.form);
    let element = document.querySelector(DOM.element);

    let val__name = (x) => {
        if(x.value && x.value.length >= 3 && x.value.length <= 20) {
            x.classList.add('success');
            x.classList.remove('error');
            return true;
        } else {
            x.classList.add('error');
            x.classList.remove('success');
            return false;
        }
    }

    let val__category = (x, y, z, a) => {
        if(x.checked === true || y.checked === true || z.checked === true || a.checked === true) {
            element.innerHTML = ' ';
            return true;
        } else {
            element.innerHTML = 'Please select a category!';
            return false;
        }
    }

    let val__description = (x) => {
        if(x.value && x.value.length >= 5 && x.value.length <= 100) {
            x.classList.add('success');
            x.classList.remove('error');
            return true;
        } else {
            x.classList.add('error');
            x.classList.remove('success');
            return false;
        }
    }

    let val__price = (x) => {
        let reg = /^(\d*([.,](?=\d{3}))?\d+)+((?!\2)[.,]\d\d)?$/;
        if(reg.test(x.value)) {
            x.classList.add('success');
            x.classList.remove('error');
            return true;
        } else {
            x.classList.add('error');
            x.classList.remove('success');
            return false;
        }
    }

    let val__stock = (x) => {
        if(x.value && !isNaN(x.value)) {
            x.classList.add('success');
            x.classList.remove('error');
            return true;
        } else {
            x.classList.add('error');
            x.classList.remove('success');
            return false;
        }
    }

    let sumAll = () => {
        form.addEventListener('submit', function(e) {
            if(val__name(name) === true && val__category(sports, photo, lit, elect) === true && val__description(desc) === true && val__price(price) === true && val__stock(stock) === true) {
                return true;
            } else {
                val__name(name);
                val__category(sports, photo, lit, elect);
                val__description(desc);
                val__price(price);
                val__stock(stock);
                e.preventDefault();
            }
        })
    }

    return {
        init: () => {
            sumAll();
        }
    }

})()

MOD.init();