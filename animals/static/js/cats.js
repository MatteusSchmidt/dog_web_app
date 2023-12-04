function send_request(param) {
    $.ajax({
        method: 'GET',
        url: 'api/get_cats?' + param,
        beforeSend: function() {
                console.log('before send');
        },
        success: function(result) {
                update_table(result);
                console.log('after send');
        },
        error: function() {
                console.log('error');
        }
    });
}