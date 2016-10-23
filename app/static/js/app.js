var $menu = $('.has-submenu');

$menu.on('click', function () {
    var $subMenu = $(this).children('ul');
    var $subMenuItem = $subMenu.children('li');
    if (!$subMenu.hasClass('on-view')) {
        $subMenu.addClass('on-view');
        $subMenu.velocity('transition.slideDownIn', {
            duration: 200
        });
        $subMenuItem.velocity('transition.expandIn', {
            delay: 200,
            duration: 300,
            stagger: 100,
        });
    } else {
        $subMenu.removeClass('on-view');
        $subMenu.add($subMenuItem).velocity('reverse');
    }
});

$(document).ready(function () {
    $("#marks_search_id").keyup(function(){
        var search_id = $('#marks_search_id').val();
        console.log(search_id)

        $.ajax({
            url: "/autoexam/search_student",
            method: "GET",
            dataType: 'json',
            data: {
                student_id: search_id
            },
            success: function(data) {
                console.log(data);
                if(data.length >= 1){
                    var fullname = data[0]['fullname']

                    $('#marks_full_name').val(fullname)
                } else {
                    $('#marks_full_name').val("")
                }

            },
            error: function(data) {
                console.log(data);
                $('#marks_full_name').val("")
            }
        });
    });

    $("#search_marks_btn").click(function(){
        var student_id = $('#marks_search_id').val();
        var term = $('#term').val();
        var year = $('#year').val();
        var form = $('#form').val();

        $.ajax({
            url: "/autoexam/search_marks",
            method: "GET",
            dataType: 'html',
            data: {
                student_id: student_id,
                term: term,
                year: year,
                form: form
            },
            success: function(data) {
                if(data.length > 0){
                    $('#marks_tbl_body').html(data);
                } else {
                    $( "#marks_tbl_body" ).html(data);
                }
            },
            error: function(data) {
                console.log(data);
            }
        });
    });
});