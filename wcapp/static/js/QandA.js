
var qParams = {};

var sliders;
var cheks = new Array();
var selectes = new Array();

//Init function
$(function(){        
    $("input[type=radio],input[type=checkbox]").uniform();
    $( "[title]" ).tooltip({
      track: true,
      delay: 0,
      showURL: false,
      showBody: " - ",
      extraClass: "pretty",
      fixPNG: true,
      left: -120
    });

    //Change questions depending on the device type
    $("#type_computer").click(function() {
      $(".notebook").fadeOut();                    
      $(".computer").fadeIn();
      for (i = 0; i < sliders.length;i++){
                    $(sliders[i]).slider().update();
                                }
    });
    $("#type_notebook").click(function() {
      $(".computer").fadeOut();                    
      $(".notebook").fadeIn();
      for (i = 0; i < sliders.length;i++){
                    $(sliders[i]).slider().update();
                                }
    });

    //Show/hide trigger
    $("#trigger").click( function(){        
      $("#questions").slideToggle("middle");        
    });

    //Set checked values
    if (getUrlParams() == null){
      setValues(qParams, 'first');
    }else{       
      setValues(recognizeElements(getUrlParams()), 'first');
    }     
});

function getUrlParams(){
  var rez = {};        
  var Params = decodeURI(location.search.substring(1)).split("&");
  if (Params[0] == "")
    return null;
  for (var i = 0; i < Params.length; i++){
      if (Params[i].split("=").length > 1)
                    rez[Params[i].split("=")[0]] = Params[i].split("=")[1]; 
  }
   return rez;
}

function recognizeElements(params)
{
  rez = {};
    for(key in params)
      {
          if ($.inArray(key, cheks) != -1) {
              rez[key + "_" + params[key]] = "checked";
          } else {
              if ($.inArray(key, selectes) != -1) {
                  rez[key + "_select"] = params[key].replace("+", " ");
              } else {
                  rez[key] = params[key].replace("%3B", ";");
              }
          }
      }
  return rez;
}  

function setValues(params, type)
{
  //alert(JSON.stringify(params))
    sliders = new Array();
    var twoParts = new Array();
    var inputs = document.qForm.getElementsByTagName("input");
         for (i = 0; i < inputs.length;i++){
          if((inputs[i].type == "radio") || (inputs[i].type == "checkbox"))
                          inputs[i].checked = false; 
                      }
    for(key in params)
      {
        if (key == "type_computer"){
          $(".computer").fadeIn();
          $(".notebook").hide();
        }
        if (key == "type_notebook"){
          $(".notebook").fadeIn();
          $(".computer").hide();
        }               
         var sKey = "#"+key;
         if (params[key] == "checked") {
            $(sKey).attr("checked", true);                                                     
         }else{               
           if (key.split('_')[1] == "hi")
           {
              twoParts.push(key); 
           }else{ 
            if (key.split('_')[1] == "select"){
                $("#"+key.split('_')[0]).selectbox("change", 'value', params[key]);
            } else{              
               var param = params[key].split(';');                   
               if (param.length > 1){                        
                  $(sKey).slider("value", param[0], param[1]);
                }
                else     
                  $(sKey).slider("value", param[0]);                   
               sliders.push(sKey);
             }
           }
         }                      
      }
      for (i = 0; i < sliders.length;i++){
        $(sliders[i]).slider().update();
      }
    for (j = 0; j < twoParts.length;j++){
        var key = twoParts[j];
        var sKey = "#"+key;
        if(params[key] == 1){                
                if (type == 'first') {$("#" + key.split('_')[0]).css('marginLeft','-800px');}
                else {$("#" + key.split('_')[0]).animate({ marginLeft: '-800px' }, 800);}
                $(sKey).val(1);
                $("#rArrow"+ key.split('_')[0]).hide();
                $("#lArrow"+ key.split('_')[0]).show();
              }
              else{
                if (type == 'first') {$("#" + key.split('_')[0]).css('marginLeft','0');}
                else {$("#" + key.split('_')[0]).animate({ marginLeft: '0' }, 800);}
                $(sKey).val(0);
                $("#lArrow"+ key.split('_')[0]).hide();
                $("#rArrow"+ key.split('_')[0]).show();
              }
      }  
      
    $.uniform.update();       
}      
function restoreDefValues()
{            
    setValues(qParams);          
}