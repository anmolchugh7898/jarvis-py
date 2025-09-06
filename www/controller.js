$(document).ready(function () {
    // Display animated message using Textillate.js
    eel.expose(DisplayMessage);
    function DisplayMessage(message) {
        $('.siri-message li:first').text(message);
        $('.siri-message').textillate('start');
    }

    // Display siri listening wave and hide mic button
    eel.expose(showHood)
    function showHood() {
        $('#oval').attr("hidden", false);
        $('#siriWave').attr("hidden", true);
    }
});