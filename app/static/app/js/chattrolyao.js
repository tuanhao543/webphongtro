$(document).ready(function() {
    $('#chat-form').on('submit', function(event) {
      event.preventDefault();
      var message = $('#message-input').val();
      $.ajax({
        url: '/ai_assistant/', // URL của view
        method: 'POST', 
        data: {
          'q': message,
          'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val() 
        },
        dataType: 'json',
        success: function(data) {
          $('#chatbox').append('<p>You: ' + message + '</p>');
          $('#chatbox').append('<p>AI: ' + data.response + '</p>');
  
          // Đảm bảo redirect_url tồn tại và hợp lệ
          if (data.redirect_url && data.redirect_url !== "") {
            // Trích xuất từ khóa tìm kiếm trực tiếp từ data.redirect_url
            var urlParams = new URLSearchParams(data.redirect_url.split('?')[1]);
            var searchKeyword = urlParams.get('search_title');
  
            // Chuyển hướng với timeout để cho phép xử lý
            setTimeout(function() {
              window.location.href = data.redirect_url;
            }, 500); // Điều chỉnh timeout khi cần
          }
  

          if (data.redirect_url && data.redirect_url !== "") {
            // Trích xuất từ khóa tìm kiếm trực tiếp từ data.redirect_url
            var urlParams = new URLSearchParams(data.redirect_url.split('?')[1]);
            var searchKeyword = urlParams.get('search_quan');
  
            // Chuyển hướng với timeout để cho phép xử lý
            setTimeout(function() {
              window.location.href = data.redirect_url;
            }, 500); // Điều chỉnh timeout khi cần
          }

          if (data.redirect_url && data.redirect_url !== "") {
            // Trích xuất từ khóa tìm kiếm trực tiếp từ data.redirect_url
            var urlParams = new URLSearchParams(data.redirect_url.split('?')[1]);
            var searchKeyword = urlParams.get('search_gia');
  
            // Chuyển hướng với timeout để cho phép xử lý
            setTimeout(function() {
              window.location.href = data.redirect_url;
            }, 500); // Điều chỉnh timeout khi cần
          }

          // Trợ lý ảo nói
          var AI_noi = new SpeechSynthesisUtterance(data.response);
            AI_noi.lang = 'vi';
            window.speechSynthesis.speak(AI_noi);
        }
      });
      $('#message-input').val('');
    });
  });




