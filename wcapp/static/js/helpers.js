function validateEmail(email) { 
    var reg = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return reg.test(email);
}


$(function(){
//Tooltips
  $('a[rel]').each(function()
   {
      $(this).qtip(
      {
         content: {
            // Set the text to an image HTML string with the correct src URL to the loading image you want to use
            text: '<img class="throbber" src="../static/img/throbber.gif" alt="Loading..." />',
            url: $(this).attr('rel'), // Use the rel attribute of each element for the url to load
            title: {
               text: $(this).attr('text'), // Give the tooltip a title using each elements text
               button: 'Закрыть' // Show a close link in the title
            }
         },
         position: {
            corner: {
               target: 'rightMiddle', // Position the tooltip above the link
               tooltip: 'leftMiddle'
            },
            adjust: {
               screen: true // Keep the tooltip on-screen at all times
            }
         },
         show: { 
            when: 'click', 
            solo: true // Only show one tooltip at a time
         },
         hide: 'unfocus',
         style: {
            title: {
              'font-family': "'Ubuntu',sans-serif",
               color: '#3399CC',
               'font-size' : '14px'
            },
            button: {
               'font-family': "'Ubuntu',sans-serif"
            },
            tip: true, // Apply a speech bubble tip to the tooltip at the designated tooltip corner
            border: {
               width: 0,
               radius: 4
            },
            color: '#145571',            
            name: 'light', // Use the default light style
            width: 570 // Set the tooltip width
         }
      })
   });

//Feedback
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