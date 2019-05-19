$(function() {
    // 侧边二级菜单
    $(".has_submenu > a").click(function(e) {

        var menu = $(this).parent("li");
        var sunMenu = $(this).next("ul");

        if (menu.hasClass("open")) {
            sunMenu.slideUp(350, function() {
                menu.removeClass("open");
            });

        } else {
            $(".navi > li > ul").slideUp(350);

            setTimeout(function() {
                $(".navi > li").removeClass("open");
                sunMenu.slideDown(350);
                menu.addClass("open");
            }, 350);

        }

        return false;
    });
});

$(document).ready(function(){
    $.get("/user_info",function(data){
        $("#nick").text(data.nick);
        $("#avatar").attr("src", data.avatar);
        if (data.permission.indexOf('admin')==-1){
            $("#system_management").hide();
        }
        if (data.permission.indexOf('reviewer')==-1){
            $("#my_review").hide();
        }
    });
});