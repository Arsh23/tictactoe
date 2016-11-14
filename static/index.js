var current_player = 'N';
var ai_turn = false;
var ai_player = 'N'
var user_player = 'N'


function change_board(x) {
    if (x == 'disable') {
        $('table').animate({
            opacity: 0.3
        }, 30);
    } else if (x == 'enable') {
        $('table').animate({
            opacity: 1
        }, 30);
    }
}

function make_move(pos) {
    if (ai_turn == false) {
        // mark user's move on board
        var id = '#' + pos
        $(id).addClass("filled");
        $(id).css('opacity', 1);
        $(id).text(user_player)
        // --------------------------------------

        // get user's move
        $.ajax({
            url: "/move/" + pos
        }).done(function(result) {

            // check game status
            // --------------------------------------

            // make ai's move after user's move is made
            ai_turn = true;
            make_move(-1)
        });
    } else if (ai_turn == true) {

        //setup board for ai
        $('.tbl .status').html(" AI's Turn! Thinking...")
        change_board('disable');
        // --------------------------------------

        // get best move for ai
        $.ajax({
            url: "/move_minimax"
        }).done(function(result) {
            // mark ai's move on board
            id = '#' + result.move
            $(id).addClass("filled");
            $(id).css('opacity', 1);
            $(id).text(ai_player)

            // check game status
            // --------------------------------------

            // setup board for user
            ai_turn = false;
            change_board('enable');
            $('.tbl .status').html(' Your Turn!')
            // --------------------------------------
        });
    }
}


$(document).ready(function() {
    $(".btn").click(function() {
        // handle choice of user
        if ($(this).hasClass("btn-o") == true) {
            user_player = 'O'
            ai_player = 'X'
            $.ajax({
                url: "/choose/" + user_player
            });
            ai_turn = false;
            $('.tbl .status').html(' Your Turn!')

        } else if ($(this).hasClass("btn-x") == true) {
            user_player = 'X'
            ai_player = 'O'
            ai_turn = true;
            $.ajax({
                url: "/choose/" + user_player
            }).done(function() {
                // make ai move first
                make_move(-1);
            });
        }
        // --------------------------------------

        // add placeholder values
        $('td').each(function() {
            $(this).text(user_player);
        });
        // --------------------------------------

        // show board and hide choice
        $('.subbox').css('z-index', -1)
        $(".tbl").animate({
            opacity: 1
        }, 500);
        $(".subbox").animate({
            opacity: 0
        }, 500);
        // --------------------------------------
    });

    $('td').hover(function() {
        // show ghost move on hover
        if ($(this).hasClass("filled") == false && ai_turn == false) {
            $(this).text(user_player)
            $(this).animate({
                opacity: 0.3
            }, 30);
        }
    }, function() {
        // remove ghost move
        if ($(this).hasClass("filled") == false && ai_turn == false) {
            $(this).animate({
                opacity: 0
            }, 30);
        }
    });

    $('td').click(function() {
        // run when user clicks a block
        if ($(this).hasClass("filled") == false && ai_turn == false) {
            // make user's move
            make_move($(this).attr('id'));
        }
    });
});
