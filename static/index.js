var ai_turn = false;
var ai_player = 'N'
var user_player = 'N'
var game_ended = false
var positions = {
    0: [0, 1, 2],
    1: [3, 4, 5],
    2: [6, 7, 8],
    3: [0, 3, 6],
    4: [1, 4, 7],
    5: [2, 5, 8],
    6: [0, 4, 8],
    7: [2, 4, 6]
}

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

function check_status(x) {
    if (x.status == 'draw') {
        game_ended = true
        change_board('disable');
        $('.tbl .status').html("Its a Draw! <a href='/'>Retry ?</a>")

    } else if (x.status == 'won') {
        game_ended = true
        change_board('enable');
        // color the winning moves
        var j = x.winning_pos[0][1];
        for (i = 0; i < 3; i++) {
            id = '#' + positions[j][i]
            $(id).css('color', '#2BA84A')
        }

        // set the msg
        if (x.winner == 'ai') {
            $('.tbl .status').html("The AI won!! ¯\\_(ツ)_/¯\
            <br><a href='/'>Retry ?</a>")
        } else if (x.winner == 'user') {
            $('.tbl .status').html("You rekt my AI, Congrats!!\
            <br>Do tell me how you did it!<br><a href='/'>Retry ?</a>")
        }
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
            check_status(result)
                // --------------------------------------

            // make ai's move after user's move is made
            if (game_ended == false) {
                ai_turn = true;
                make_move(-1)
            }
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
            check_status(result)
                // --------------------------------------

            if (game_ended == false) {
                ai_turn = false;
                // setup board for user
                change_board('enable');
                $('.tbl .status').html(' Your Turn!')
                    // --------------------------------------
            }
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
            if (game_ended == false) {
                make_move($(this).attr('id'));
            }
        }
    });
});
