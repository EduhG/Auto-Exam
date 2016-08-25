$(document).ready(function(){
    $('input').iCheck({
        checkboxClass: 'icheckbox_flat',
        radioClass: 'iradio_flat'
    });


    $("select2").select2({
        /*placeholder: "Select a state",
        allowClear: true*/
    });

    Materialize.updateTextFields();
});