function del(id) {
    $.ajax({
        url: '/delete/',
        type: 'GET',
        data: {'id': id},
        success: function () {
            console.log("Data deleted.");
        },
        error: function () {
            console.log("Data could not be deleted.");
        }
    });
}