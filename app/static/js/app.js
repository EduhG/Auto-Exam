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
                console.log('obtained data' + data)
                if(data.length > 0){
                    $('#marks_tbl_body').html(data);
                } else {
                    $( "#marks_tbl_body" ).html('');
                }
            },
            error: function(data) {
                $( "#marks_tbl_body" ).html('');
                console.log(data);
            }
        });
        return false
    });

    $('#marksTable tbody').on( 'keyup', 'td', function () {
        var marks = $(this).html();
        var row_index = $(this).parent().index() + 1;
        var col_index = $(this).index() + 1;

        if (marks < 40) {
            $(this).closest('tr').find('td:eq(3)').html('E');
        } else if (marks < 45) {
            $(this).closest('tr').find('td:eq(3)').html('D-');
        } else if (marks < 50) {
            $(this).closest('tr').find('td:eq(3)').html('D');
        } else if (marks < 55) {
            $(this).closest('tr').find('td:eq(3)').html('D+');
        } else if (marks < 60) {
            $(this).closest('tr').find('td:eq(3)').html('C-');
        } else if (marks < 65) {
            $(this).closest('tr').find('td:eq(3)').html('C');
        } else if (marks < 70) {
            $(this).closest('tr').find('td:eq(3)').html('C+');
        } else if (marks < 75) {
            $(this).closest('tr').find('td:eq(3)').html('B-');
        } else if (marks < 80) {
            $(this).closest('tr').find('td:eq(3)').html('B');
        } else if (marks < 85) {
            $(this).closest('tr').find('td:eq(3)').html('B+');
        } else if (marks < 90) {
            $(this).closest('tr').find('td:eq(3)').html('A-');
        } else if (marks < 100) {
            $(this).closest('tr').find('td:eq(3)').html('A');
        }

    } );

    function GetCellValues() {
        var table = document.getElementById('marksTable');
        for (var r = 0, n = table.rows.length; r < n; r++) {
            for (var c = 0, m = table.rows[r].cells.length; c < m; c++) {
                alert(table.rows[r].cells[c].innerHTML);
            }
        }
    }

    $('#save_table_marks').click(function () {
        convertTAbleToJson();

        return false
    });

    function convertTAbleToJson() {
        var table = $('#marksTable').tableToJSON();
        var table_data = JSON.stringify(table);

        var student_id = $('#marks_search_id').val();
        var term = $('#term').val();
        var year = $('#year').val();
        var form = $('#form').val();

        my_data = {
            student_id: student_id,
            term: term,
            year: year,
            form: form,
            table_data: JSON.stringify(table)
        };

        console.log(my_data)

        $.ajax({
            url: '/autoExam/save_marks_data',
            dataType: 'html',
            type: 'post',
            data: my_data,
            success: function( data){
                alert('Records saved successfully');
            },
            error: function( jqXhr, textStatus, errorThrown ){
                console.log( errorThrown );
            }
        });
    }

});

