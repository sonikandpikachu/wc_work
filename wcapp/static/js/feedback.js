function validateEmail(email) { 
    var reg = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return reg.test(email);
}

//Feedback form send
$(function(){
  $(".feedback").fancybox({
        helpers : {
            overlay : {
                css : {
                    'background' : 'rgba(255, 255, 255, 0.98)'
                }
            }
        }
    });
  $("#contact").submit(function() { return false; });

  
  $("#send").on("click", function(){
    var emailval  = $("#email").val();
    var msgval    = $("#msg").val();
    var msglen    = msgval.length;
    var mailvalid = validateEmail(emailval);
    
    if(mailvalid == false) {
      $("#email").addClass("error");
    }
    else if(mailvalid == true){
      $("#email").removeClass("error");
    }
    
    if(msglen < 4) {
      $("#msg").addClass("error");
    }
    else if(msglen >= 4){
      $("#msg").removeClass("error");
    }
    
    if(mailvalid == true && msglen >= 4) {
      // if both validate we attempt to send the e-mail
      // first we hide the submit btn so the user doesnt click twice
      $("#send").replaceWith("<p>отправляю...</p>");
      $.ajax({
        type: 'GET',
        url: $SCRIPT_ROOT + '/feedback/',
        data: $("#contact").serialize(),
        success: function() {
            $("#contact").fadeOut("fast", function(){
              $(this).before("<p>Спасибо! Ваше письмо успешно доставлено :)</p>");
              setTimeout("$.fancybox.close()", 1000);
              $("#feedbackBlock").height(70);
            });
        }
      });
    }
  });
});