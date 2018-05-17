function del() {
    var sel = [];
    $('.select_data:checked').each(function () {
        sel.push($(this).val());
    });
    $.ajax({
        contentType: 'application/json; charset=utf-8',
        url: '/delete/',
        type: 'GET',
        data: {'id':JSON.stringify({'ids': sel})},
        success: function () {
            console.log(sel);
            console.log("Data deleted.");
            window.location.href = '/';
        },
        error: function () {
            console.log(sel);
            console.log("Data could not be deleted.");
        }
    });
}
