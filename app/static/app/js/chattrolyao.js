$(document).ready(function() {
    $('#chat-form').on('submit', function(event) {
        event.preventDefault();
        var message = $('#message-input').val();
        $.ajax({
            url: '/ai_assistant/', // URL của view
            method: 'POST', // Thay đổi phương thức thành POST
            data: {
                'q': message,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val() // Thêm CSRF token
            },
            dataType: 'json',
            success: function(data) {
                $('#chatbox').append('<p>You: ' + message + '</p>');
                $('#chatbox').append('<p>AI: ' + data.response + '</p>');
                
                // Chuyển hướng đến URL tìm kiếm với từ khóa là tham số truy vấn
                if (data.redirect_url) {
                    var searchKeyword = message.split('tìm kiếm')[1].trim();
                    window.location.href = data.redirect_url;
                }
                
                // Trợ lý ảo nói
                var AI_noi = new SpeechSynthesisUtterance(data.response);
                window.speechSynthesis.speak(AI_noi);
            }
        });
        $('#message-input').val('');
    });
});