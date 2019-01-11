'use strict';

const MOD = (() => {

    // Global namespacing for easy future adjustment
    let DOM = {
        name: '.details__name',
        category: '.category',
        description: '.description',
        price: '.price',
        stock: '.stock',
        button: '.submit'
    }

    let name = document.querySelector(DOM.name).value;
    let category = document.querySelector(DOM.category);
    let btn = document.querySelector(DOM.button);

    let calc = () => {
        if(name !== null) {
            console.log('Error James');
        } else {
            console.log('Well done');
        }
    }

    let sumAll = () => {
        btn.addEventListener('click', function() {
            calc();
        })
    }

    return {
        init: () => {
            sumAll();
        }
    }

})()

MOD.init();