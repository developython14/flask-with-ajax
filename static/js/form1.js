$(document).ready(function() {
    $('form').on('submit', function(event) {
        $.ajax({
            data : {
                name : $('#nameInput').val(),
                email : $('#emailInput').val()
            },
            type : 'POST',
            url : '/process1'
        })
        .done(function(data) {
            if (data.error) {
                $('#errorAlert').text(data.error).show();
                $('#successAlert').hide();
            }
            else {
                $('#successAlert').text(data.sum).show();
                $('#errorAlert').hide();
            }
        });
        event.preventDefault();
    });
});