let formFile = document.getElementById("FormImageFile")
formFile.onchange = function (e) {
    let image = document.getElementById('outputImage');
    image.src = URL.createObjectURL(e.target.files[0]);

    $('#alert-error').hide();
    $('#result').html('');

}

$(document).ready(function (e) {
    $('#progress-spinner').hide()
    $('#alert-error').hide();
    $('#result').html('');
    $('#predictButton').on('click', function () {
        let file_data = $('#FormImageFile')[0].files[0];
        let form_data = new FormData();
        form_data.append('file', file_data);
        $('#progress-spinner').show()
        $('#result').html('');
        $('#alert-error').hide();
        $.ajax({
            url: '/predict',
            cache: false,
            contentType: false,
            processData: false,
            data: form_data,
            type: 'post',
            success: function (response) {
                if (response === false) {
                    $('#alert-error').show();
                } else {
                    $('#alert-error').hide();
                    response[1] = response[1].replace("_", " ")
                    if (response[0] === 'dog') {
                        var message = `<div class="alert alert-success" role="alert">
                        Dog breed of the image is ${response[1]}
                    </div>`
                    } else if (response[0] === "human") {
                        var message = `<div class="alert alert-success" role="alert">
                        The person in the image is most similar to dog breed ${response[1]}
                    </div>`
                    }

                    $('#result').html(message);
                }
            },
            complete: function (response) {
                $('#progress-spinner').hide();
            },
            error: function (response) {
                $('#result').html("Failed to predict");
            }
        });
    });
});