function edit() {
    if($("#id").val() == '')
    {
        alert("Id cannot be blank.");
    }
    else if ($("#name").val() == '') {
        alert("Name cannot be blank.");
    }
    else if ($("#city").val() == '') {
        alert("City cannot be blank.");
    }
    else if ($("#state").val() == '') {
        alert("State cannot be blank.");
    }
    else {
        edit_record();
    }
}

function edit_record() {
    $.ajax({
        type: 'POST',
        url: '/modify/',
        data: {'name': $("#name").val(), 'city': $("#city").val(), 'state': $("#state").val(), 'id': $("#id").val()},
        success: function () {
            window.location.href = '/';
            console.log("Data edited successfully.");
            $("#name").val("");
            $("#id").val("");
            $("#city").val("");
            $("#state").val("");
        },
        error: function () {
            console.log("Data could not be added.");
        }
    });
}