function update_talbe(data) {
    let row = '';
    let all_rows = '';

    Object.keys(data).forEach(key => {
        elem = data[key];
        row += "<tr><td>" + elem['name'] + "</td><td>" + "<a href='/company/" + elem['pk'] + "/'>" + elem['pk'] + "</a>" + "</td></tr>"
    });
    all_rows = all_rows + row;
    $('#showtable tbody').html(all_rows);
}

$(document).ready(function () {
    $.ajax({
        method: 'GET',
        url: 'http://127.0.0.1:8000/company/',
        dataType: "json",
        beforeSend: function () {
            console.log('Before send')
        },
        success: function (data) {
            update_talbe(data);
            console.log(data);
        },
        error: function (error) {
            console.log(error)
        },
    });
});

$('#detai').click( function (pk) {
    $.ajax({
        method: 'GET',
        url: `http://127.0.0.1:8000/company/${pk}/`,
        dataType: 'json',
        contentType: 'application/json',
        success: function (data) {
            console.log(data);
        },
        error: function(error) {
            console.log(error);
        },
    });
});
