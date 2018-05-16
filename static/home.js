function del(id) {
    $.ajax({
        url: '/delete/',
        type: 'GET',
        data: {'id': id},
        success: function () {
            console.log("Data deleted.");
            window.location.href = '/';
        },
        error: function () {
            console.log("Data could not be deleted.");
        }
    });
}
