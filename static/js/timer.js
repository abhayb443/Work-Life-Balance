$(document).ready(function() {
    // timer function
    function startTimer(duration, display) {
        var timer = duration, minutes, seconds;
        var refresh = setInterval(function () {
            minutes = parseInt(timer / 60, 10)
            seconds = parseInt(timer % 60, 10);

            minutes = minutes < 10 ? "0" + minutes : minutes;
            seconds = seconds < 10 ? "0" + seconds : seconds;

            var output = minutes + " : " + seconds;
            display.text(output);
            $("title").html(output + " - Work Life Balance");

            if (--timer < 0) {
                display.text("Time's Up! Pencils down...!");
                clearInterval(refresh);  // exit refresh loop
                var music = $("#over_music")[0];
                music.play();
                alert("Yay, time's up...!");
            }
        }, 1000);

    }

    // start timer
    jQuery(function ($) {
        var display = $('#time');
        startTimer(Seconds, display);
    });

    // show help information
    $('#help-info').hide();
    $('#help-btn').hover( function() { $('#help-info').toggle(); } );
})
