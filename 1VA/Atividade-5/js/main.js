(function() {
    var framesArray = Array.from(window.parent.frames);
    var form1 = framesArray[0].document.getElementsByTagName('form')[0];
    var form2 = framesArray[1].document.getElementsByTagName('form')[0];

    form1.addEventListener('submit', function($event) {
        $event.preventDefault();
        var myForm = $event.target;
        var event = new CustomEvent('message', { detail: myForm });
        window.parent.document.dispatchEvent(event);
    });

    form2.addEventListener('submit', function($event) {
        $event.preventDefault();
        var myForm = $event.target;
        var event = new CustomEvent('message', { detail: myForm });
        window.parent.document.dispatchEvent(event);
    });
    
    window.parent.document.addEventListener('message', function($event) {
        var formElement = $event.detail;
        var textoArea = formElement.querySelector('input').value;

        if(formElement.id === 'frame1') {
            framesArray[1].document.querySelector('form input').value = textoArea;
        } else {
            framesArray[0].document.querySelector('form input').value = textoArea;
        }
    });
})();
