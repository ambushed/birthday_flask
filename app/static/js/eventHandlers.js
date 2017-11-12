function passKey(e) {

    var keyCode = e.keyCode;
    alert('KeyDown')

    $.ajax({
        type : "POST",
        url : "{{ url_for('mod.load_ajax') }}",
        data: JSON.stringify(keyCode, null, '\t'),
        contentType: 'application/json;charset=UTF-8',
        success: function(result) {
            console.log(result);
        }
    });
}


