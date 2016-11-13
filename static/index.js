var current_player = 'N';

$(document).ready(function() {
    $(".btn").click(function() {
        // current_player = $(this).html();

        if ($(this).hasClass("btn-o") == true) {
            current_player = 'O'
        }

        if ($(this).hasClass("btn-x") == true) {
            current_player = 'X'
        }

        $('.subbox').css('z-index', -1)
        $('td').each(function() {
            $(this).text(current_player)
        });

        $(".tbl").animate({
            opacity: 1
        }, 500);
        $(".subbox").animate({
            opacity: 0
        }, 500);
    });

    $('td').mouseenter(function() {
        if ($(this).hasClass("filled") == false) {
            $(this).text(current_player)
            $(this).animate({
                opacity: 0.3
            }, 30);
        }
    });

    $('td').mouseleave(function() {
        if ($(this).hasClass("filled") == false) {
            $(this).text(current_player)
            $(this).animate({
                opacity: 0
            }, 30);
        }
    });

    $('td').click(function() {
        if($(this).hasClass("filled") == false) {
            $(this).addClass("filled");
            $(this).css('opacity',1);
            $(this).text(current_player)

            if(current_player == 'X'){
                current_player = 'O'
            } else {
                current_player = 'X'
            }
        }
    });
});
