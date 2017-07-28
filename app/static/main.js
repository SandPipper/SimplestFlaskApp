import './main.css';
import './del';
//export {blink};

'use strict'

window.addEventListener("load",  function() {
    var form = document.querySelector('form');
    var output = document.querySelector('p');
    var input = document.getElementById('inputer');


    form.addEventListener('submit', function(event) {
        event.preventDefault();

        var data = new FormData(form);
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/form');
        xhr.send(data);

        function blink(elem, color) {
            elem.style.backgroundColor = color;
            elem.style.transition = "all 1s";
            setTimeout(function() {
                elem.style.backgroundColor = "white";
                elem.style.transition = "all 1s";
            }, 1000)
        }

        xhr.onreadystatechange = function() {
            if (xhr.readyState == XMLHttpRequest.DONE) {

                var jsonResponse = JSON.parse(xhr.responseText)

                if (xhr.status == 200) {
                    blink(input, "lightgreen");
                    output.innerHTML += 'Response: ' + jsonResponse['message'] + "</br>";
                    form.reset();
                    if (jsonResponse['status'] != 1) {
                        blink(input, "red");
                    }

                } else {
                output.innerHTML += 'Error: ' + xhr.statusText + "</br>";
                }
            }
        }
    });
})
