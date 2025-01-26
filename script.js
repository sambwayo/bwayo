document.addEventListener('DOMContentLoaded', function () {
    const text = " let's come make disciples of all nations so that  our master jesus christ be known allover the world!";
    let index = 0;
    const typingSpeed = 50; // Adjust typing speed here

    function type() {
        if (index < text.length) {
            document.getElementById('typing-text').innerHTML += text.charAt(index);
            index++;
            setTimeout(type, typingSpeed);
        }
    }

    type();
});