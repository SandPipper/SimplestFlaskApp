'use strict'
import {blink} from './main';

window.addEventListener("load", function() {

    var clicker = document.querySelector('table');

    clicker.addEventListener('click', function(event) {
        event.preventDefault();
        Array.prototype.forEach.call(clicker.querySelectorAll('td'),
                                     function(element) {

            if (element === event.target) {

                var forDel = parseInt(event.target.parentNode.firstElementChild
                                      .innerHTML, 10);

                var data = {'string_id': forDel}
                var xhr = new XMLHttpRequest();
                xhr.open('DELETE', '/delete/' + forDel);
                xhr.send(JSON.stringify(data));

                xhr.onreadystatechange = function() {
                    if (xhr.readyState == XMLHttpRequest.DONE) {
                        var jsonResponse = JSON.parse(xhr.responseText);

                        if (xhr.status == 200) {
                            //blink(event.target, "coral")
                                if (jsonResponse['status'] == 1) {
                                    event.target.parentNode.remove()
                                    console.log(jsonResponse)

                                } else {
                                    console.log(jsonResponse)
                                }

                        } else {
                            console.log(jsonResponse)
                        }
                    }
                }
            }
        })
    })
})
