/**
 * Created by ljd on 2016/8/26.
 */

$(document).ready(function(){

    $("#online-1").click(function(){
        $.ajax({
            type: "get",
            url: "/deploy_online",
            success: function(data){
                for (var i in data)
                    {
                        txt = txt + i;
                        $("#console").val(txt);
                    }
            },
            error: function(jqXHR){
                alert("错误:" + jqXHR.status);
            }

        });
    });
});