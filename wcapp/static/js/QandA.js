var qParams = {};

var sliders;
var cheks = new Array();
var selectes = new Array();


//Init function
$(function () {
    var dType;

    $("input[type=radio],input[type=checkbox]").uniform();

    //Change questions depending on the device type
    $("#type_computer").click(function () {
        $(".notebook").fadeOut();
        $(".computer").fadeIn();
        for (var i = 0, max = sliders.length; i < max; i++) {
            $(sliders[i]).slider().update();
        }
    });
    $("#type_notebook").click(function () {
        $(".computer").fadeOut();
        $(".notebook").fadeIn();
        for (var i = 0, max = sliders.length; i < max; i++) {
            $(sliders[i]).slider().update();
        }
    });

    //Default button
    $("#defaultButton").click(function () {
        setValues(qParams);
    });

    //Show/hide trigger
    $("#trigger").click(function () {
        $("#questions").slideToggle("middle");
    });

    //Set checked values
    var urlParams = getUrlParams();
    if (urlParams === null) {
        setValues(qParams, 'first');
    } else {
        setValues(recognizeElements(urlParams), 'first');
        scrollToAnswerList();

    }

    function scrollToAnswerList(){
                destination = $("#goButton").offset().top;
        if($.browser.safari){
          $('body').animate( { scrollTop: destination }, 1100 );
        }else{
          $('html').animate( { scrollTop: destination }, 1100 );
      }
    }

    function doPagination(event){
        var page = event.target;
        if (page.className.split(' ')[0] === "select") {
            return
        }
        var lastPage = parseInt($(".paginationHref:last").text()),
            currentPage = parseInt(page.text),
            url = $SCRIPT_ROOT + '/getPage/' + currentPage + '/' + dType + '/';

        $.getJSON(url, function (data) {
            var html = "",
                picture = "<li> <a href = \"/<%=type%>/<%=id%>/<%=comp_dss%>\" target=\"_blank\"><div class=\"compOpenButton\"></div></a></li>";
            var compImageTmplate = tmpl("<li class=\"answer\">" +
                "<div class = \"image\">" +
                "<a class = \"fancybox\" rel = \"gallery<%=id%>\" href = \"../static/img/<%=type%>s/<%=id%>_img/<%=gallery[0]%>\">" +
                "<img src=\"../static/img/<%=type%>s/<%=id%>_img/main.jpg\" alt = \"Рисунок\"/></a>")
            var compImagesTmplate = tmpl("<a class = \"fancybox\" rel = \"gallery<%=id%>\"" +
                "href = \"../static/img/<%=type%>s/<%=id%>_img/<%=img%>\"></a>")
            var compTmplate = tmpl(
                "</div>" +
                "<div class = \"descriptionSection\">" +
                "<div class=\"title\">" +
                "<div class = \"name\"><a href = \"/<%=type%>/<%=id%>/<%=comp_dss%>\" target=\"_blank\"> <%=name%> &nbsp; <%=model%> </a></div>" +
                "<div class=\"classification\">" +
                "<div class=\"cover\"></div>" +
                "<div class=\"progress\" style=\"width: <%=comp_dss%>%;\"></div>" +
                "</div>" +
                "</div>" +
                "<ul class = \"description\">" +
                "<li>" +
                "<div class=\"paramName\">Процессор:</div>" +
                "<div class=\"paramValue\"> <%=cpu_name%> <%=cpu_model%>, <%=cpu_frequency%> Ггц</div>" +
                "<div class=\"paramStars\">" +
                "<div class=\"cover\"></div>" +
                "<div class=\"progress\" style=\"width: <%=cpu_dss%>%;\"></div>" +
                "</div>" +
                "</li>" +
                "<li>" +
                "<div class=\"paramName\">Оперативная память:</div>" +
                "<div class=\"paramValue\"> <%=ram_amount%> Gb </div>" +
                "<div class=\"paramStars\">" +
                "<div class=\"cover\"></div>" +
                "<div class=\"progress\" style=\"width: <%=ram_dss%>%;\"></div>" +
                "</div>" +
                "</li>" +
                "<li>" +
                "<div class=\"paramName\">Жесткий диск:</div>" +
                "<div class=\"paramValue\"> <%=hdd_capacity%> Gb <%=hdd_type%></div>" +
                "<div class=\"paramStars\">" +
                "<div class=\"cover\"></div>" +
                "<div class=\"progress\" style=\"width: <%=hdd_dss%>%;\"></div>" +
                "</div>" +
                "</li>" +
                "<li>" +
                "<div class=\"paramName\">Видеокарта:</div>" +
                "<div class=\"paramValue\"> <%=vga%> <%=vga_amount%> </div>" +
                "<div class=\"paramStars\">" +
                "<div class=\"cover\"></div>" +
                "<div class=\"progress\" style=\"width: <%=vga_dss%>%;\"></div>" +
                "</div>" +
                "</li>" +
                "<li>" +
                "<div class=\"paramName\"> Операционная система: </div>" +
                "<div class=\"paramValue\"> <%=os%></div>" +                
                "</li>")
            var compDisplay = tmpl(
                "<li>" +
                "<div class=\"paramName\">Дисплей:</div>" +
                "<div class=\"paramValue\"> <%=display%> \" <%=resolution%> </div>" +
                "</li>")
            var compTmplateEnd = tmpl(    
                "<li>" +
                "<div class=\"paramName\">Другие параметры:</div>" +
                "<div class=\"paramStars\">" +
                "<div class=\"cover\"></div>" +
                "<div class=\"progress\" style=\"width: <%=other_dss%>%;\"></div>" +
                "</div>" +
                "</li>" +
                "</ul>" +
                "</div>" +
                "<ul class = \"answerButtons\">" +
                "<li> " +
                "<div class = \"price\"><%=price%> грн</div> " +
                "<div class = \"priceRange\"><%=max_price%> - <%=min_price%> </div>" +
                "</li>" +
                picture +
                "</ul>" +
                "</li>");
            $.each(data["pretty_devices"], function (key, comp) {
                html += compImageTmplate(comp);
                for(var i = 1; i < comp.gallery.length; i++){
                    img = comp.gallery[i];
                    html += compImagesTmplate(comp,img);
                }
                html += compTmplate(comp);
                if(comp.display) html += compDisplay(comp);
                html += compTmplateEnd(comp);
            });
            $('#answerList').fadeOut("slow", function () {
                $('#answerList').html(html);
                $('#answerList').show();
                scrollToAnswerList();
            });
        });


        function addPage(number, isSelect) {
            var tmp = "<li><a href=\"javascript:void(0)\" class = '"
            if (isSelect) {
                tmp += "select "
            }
            tmp += "paginationHref'>" + number + "</a></li>"
            return tmp;
        }

        var html = "<ul>";
        if (currentPage === 1) {
            html += addPage(1, true);
        } else {
            html += addPage(1);
        }
        var isInterval = false;
        for (var i = 2; i <= lastPage; i++) {
            if ((currentPage - 1 <= i) && (currentPage + 1 >= i) ||
                (lastPage - 1 <= i) || (2 >= i)) {
                if (isInterval){
                    html += "...";
                    isInterval = false;
                }
                if (currentPage === i) {
                    html += addPage(i, true);
                } else {
                    html += addPage(i);
                }
            } else {
                isInterval = true;
            }
        }
        html += "</ul>";
        $('#pagination').html(html);
        $(".paginationHref").each(function () {
            $(this).click(doPagination);
        });
    }

    $(".paginationHref").each(function () {
        $(this).click(doPagination);
    });

    function getUrlParams() {
        var rez = {};
        var Params = decodeURI(location.search.substring(1)).split("&");
        if (Params[0] == "")
            return null;
        for (var i = 0; i < Params.length; i++) {
            if (Params[i].split("=").length > 1){
                rez[Params[i].split("=")[0]] = Params[i].split("=")[1];
            }
        }
        return rez;
    }

    function recognizeElements(params) {
        rez = {};
        for (key in params) {
            if (key == "type") {
                dType = params[key];
            }
            if ($.inArray(key, cheks) != -1) {
                if (key.indexOf(params[key]) != -1){
                    rez[key] = "checked";
                } else {
                    rez[key + "_" + params[key]] = "checked";
                }
            } else {
                if ($.inArray(key, selectes) != -1) {
                    rez[key + "_select"] = params[key].replace(/\+/g, " ");
                } else {
                    rez[key] = params[key].replace("%3B", ";");
                }
            }
        }
        return rez;
    }

    function setValues(params, type) {
        //alert(JSON.stringify(params))
        sliders = new Array();
        var twoParts = new Array();
        var inputs = document.qForm.getElementsByTagName("input");
        for (i = 0; i < inputs.length; i++) {
            if ((inputs[i].type == "radio") || (inputs[i].type == "checkbox"))
                inputs[i].checked = false;
        }
        for (key in params) {
            if (key == "type_computer") {
                $(".computer").fadeIn();
                $(".notebook").hide();
            }
            if (key == "type_notebook") {
                $(".notebook").fadeIn();
                $(".computer").hide();
            }
            var sKey = "#" + key;
            if (params[key] == "checked") {
                $(sKey).attr("checked", true);
            } else {
                if (key.split('_')[1] == "hi") {
                    twoParts.push(key);
                } else {
                    if (key.split('_')[1] == "select") {
                        console.log(params[key]);
                        $("#" + key.split('_')[0]).selectbox("change", params[key], params[key]);
                    } else {
                        var param = params[key].split(';');
                        if (param.length > 1) {
                            $(sKey).slider("value", param[0], param[1]);
                        }
                        else
                            $(sKey).slider("value", param[0]);
                        sliders.push(sKey);
                    }
                }
            }
        }

        for (j = 0; j < twoParts.length; j++) {
            var key = twoParts[j];
            var sKey = "#" + key;
            if (params[key] == 1) {
                if (type == 'first') {
                    $("#" + key.split('_')[0]).css('marginLeft', '-800px');
                }
                else {
                    $("#" + key.split('_')[0]).animate({ marginLeft: '-800px' }, 800);
                }
                $(sKey).val(1);
                $("#rArrow" + key.split('_')[0]).hide();
                $("#lArrow" + key.split('_')[0]).show();
            }
            else {
                if (type == 'first') {
                    $("#" + key.split('_')[0]).css('marginLeft', '0');
                }
                else {
                    $("#" + key.split('_')[0]).animate({ marginLeft: '0' }, 800);
                }
                $(sKey).val(0);
                $("#lArrow" + key.split('_')[0]).hide();
                $("#rArrow" + key.split('_')[0]).show();
            }
        }

        $.uniform.update();
        if (type != "first") {
            for (var i = 0, max = sliders.length; i < max; i++) {
                $(sliders[i]).slider().update();
            }
        }
    }
});


