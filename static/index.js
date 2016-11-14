var current_player = 'N';
var ai_turn = false;


function change_board(x) {
    if(x == 'disable') {

    }
}

function make_move(pos) {

    if(ai_turn == false) {

        // mark move in board
            // $(this).addClass("filled");
            // $(this).css('opacity', 1);
            // $(this).text(current_player)
        // --------------------------------------

        //setup board for ai
        $('.tbl .status').html(" AI's Turn! Thinking...")
        change_board('disable');
        // --------------------------------------

        // get user's move
        $.ajax({
            url: "/move/" + pos
        });
        // --------------------------------------

        // check game status
        // --------------------------------------

        // change player for ai
        ai_turn = true;
        if (current_player == 'X') {
            current_player = 'O'
        } else {
            current_player = 'X'
        }
        // --------------------------------------

    }

    if(ai_turn == true) {
        // get best minimax move for ai

            // get data from ajax

        // --------------------------------------

        // mark data on board
            // $(this).addClass("filled");
            // $(this).css('opacity', 1);
            // $(this).text(current_player)
        // --------------------------------------

        // check game status
        // --------------------------------------

        // setup board for user
        change_board('enable');
        $('.tbl .status').html(' Your Turn!')
        // --------------------------------------

        // change player for user
        ai_turn = false;
        if (current_player == 'X') {
            current_player = 'O'
        } else {
            current_player = 'X'
        }
        // --------------------------------------
    }
}


$(document).ready(function() {
    $(".btn").click(function() {

        // handle choice of user
        if ($(this).hasClass("btn-o") == true) {
            current_player = 'O';
            ai_turn = false;
            $('.tbl .status').html(' Your Turn!')
        } else if ($(this).hasClass("btn-x") == true) {
            current_player = 'X';
            ai_turn = true;
            //setup board for ai
            $('.tbl .status').html(" AI's Turn! Thinking...")
            change_board('disable');
            make_move(-1);
        }
        $.ajax({
            url: "/choose/" + user_player
        });
        // --------------------------------------

        // add placeholder values
        $('td').each(function() {
            $(this).text(current_player);
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
            $(this).text(current_player)
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
            make_move($(this).id());
        }
    });
});
