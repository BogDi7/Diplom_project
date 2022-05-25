


const cartBtn = document.getElementsByClassName('cart-btn');
const price = document.getElementsByClassName('price');
const slug = document.getElementsByTagName("button")[0].getAttribute('data-price');


$(document).ready(function () {
    $(".cartBtn").click(function () {
        for (var i = 0; i < cartBtn.length; i++) {
            var addItem = cartBtn[i];

            addItem.addEventListener('click', function () {
                console.log(slug)
            });
        }
    });

    ///////////////////////////
});

const itemPrice = $("#itemPrice");

const cartBtn = document.getElementsByClassName('cart-btn');
const slug = document.getElementsByTagName('span').getAttribute('data-price');


cartBtn.addEventListener('click', function () {

    for (let i = 0; i < cartBtn.length; i++) {
        const element = cartBtn[i];

        console.log('clicked')
    }

});


///////////////////////////////////////////////////
// dropdown
///////////////////////////////////////////////////