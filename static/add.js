function add() {
    if ($("#name").val() == '')
    {
        alert("Name cannot be blank.");
    }
    else if($("#city").val() == '')
    {
        alert("City cannot be blank.");
    }
    else if($("#state").val() == '')
    {
        alert("State cannot be blank.");
    }
    else
    {
        add_record();
    }
}
function add_record() {
    $.ajax({
        type: 'POST',
        url: '/add/',
        data: {'name': $("#name").val(), 'city': $("#city").val(), 'state': $("#state").val()},
        success: function () {
            console.log("Data added successfully.");
            $("#name").val("");
            $("#city").val("");
            $("#state").val("");
        },
        error: function () {
            console.log("Data could not be added.");
        }
    });
}
function home() {
        window.location.href = '/';
}