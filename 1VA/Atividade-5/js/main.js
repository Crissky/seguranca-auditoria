(function() {
    var framesArray = Array.from(window.parent.frames);
    var form1 = framesArray[0].document.getElementsByTagName('form')[0];
    var form2 = framesArray[1].document.getElementsByTagName('form')[0];

    form1.addEventListener('submit', function($event) {
        $event.preventDefault();
        window.parent.document.dispatchEvent(
            new CustomEvent('message', { detail: $event.target })
        );
    });

    form2.addEventListener('submit', function($event) {
        $event.preventDefault();
        window.parent.document.dispatchEvent(
            new CustomEvent('message', { detail: $event.target })
        );
    });
    
    window.parent.document.addEventListener('message', function($event) {
        var formElement = $event.detail;
        var textArea = formElement.querySelector('input').value;

        if(formElement.id === 'frame1') {
            framesArray[1].document.querySelector('form input').value = textArea;
        } else {
            framesArray[0].document.querySelector('form input').value = textArea;
        }
    });
})();
