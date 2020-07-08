var url = document.location.toString();
var arrUrl = url.split("//");
//当前访问的博客博主
var blog_username = arrUrl[1].split("/")[1];

token = window.localStorage.getItem('dnblog_token');
username = window.localStorage.getItem('dnblog_user');
function showLike() {
    // 每个部分需要设置一个z-index,在上面的z-index = 0, 下面的z-index = -1

    $.ajax({
        type: "GET",
        // http://127.0.0.1:8000/v1/users/bernard?like=1
        url: "http://127.0.0.1:8000/v1/users/" + blog_username + "?like=1",
        beforeSend: function(request) {
             request.setRequestHeader("Authorization", token);
         },
        success: function (result) {
            if (result.code == 200) {
                // 喜欢
                var html_show = ""
                    html_show = "<table class='table table-striped'>"
                    html_show += "<tr>"
                        html_show += "<th>"
                            html_show += "id"
                        html_show += "</th>"
                        html_show += "<th>"
                            html_show += "sing"
                        html_show += "</th>"
                        html_show += "<th>"
                            html_show += "singer"
                        html_show += "</th>"
                        html_show += "<th>"
                            html_show += "status"
                        html_show += "</th>"
                    html_show += "</tr>"
                    html_show += "<tr>"
                        html_show += "<td>"
                            html_show += result.data.id
                        html_show += "</td>"
                        html_show += "<td>"
                            html_show += result.data.sing
                        html_show += "</td>"
                        html_show += "<td>"
                            html_show += result.data.singer
                        html_show += "</td>"
                        html_show += "<td>"
                            html_show += result.data.sstatus
                        html_show += "</td>"
                    if (result.data.id) {$(".like_show").html(html_show)
                    }else{
                        html_show_n = "<table class='table table-striped'>"
                    html_show_n += "<tr>"
                        html_show_n += "<th>"
                            html_show_n += "id"
                        html_show_n += "</th>"
                        html_show_n += "<th>"
                            html_show_n += "sing"
                        html_show_n += "</th>"
                        html_show_n += "<th>"
                            html_show_n += "singer"
                        html_show_n += "</th>"
                        html_show_n += "<th>"
                            html_show_n += "status"
                        html_show_n += "</th>"
                    html_show_n += "</tr>"
                        $(".like_show").html(html_show_n)
                    }
                }else{
                alert(result.error);
            }
        }

    })
}

function listendShow() {
    $.ajax({
        type: "GET",
        // http://127.0.0.1:8000/v1/users/bernard?listend=1
        url: "http://127.0.0.1:8000/v1/users/" + blog_username + "?listend=1",
        beforeSend: function(request) {
             request.setRequestHeader("Authorization", token);
         },
        success: function (result) {
            if (result.code == 200) {
                // 喜欢
                var html_show = ""
                    html_show = "<table class='table table-striped'>"
                    html_show += "<tr>"
                        html_show += "<th>"
                            html_show += "id"
                        html_show += "</th>"
                        html_show += "<th>"
                            html_show += "sing1"
                        html_show += "</th>"
                        html_show += "<th>"
                            html_show += "singer"
                        html_show += "</th>"
                        html_show += "<th>"
                            html_show += "status"
                        html_show += "</th>"
                    html_show += "</tr>"

                    if (result.data.id ) {
                        html_show += "<tr>"
                        html_show += "<td>"
                            html_show += result.data.id
                        html_show += "</td>"
                        html_show += "<td>"
                            html_show += result.data.sing
                        html_show += "</td>"
                        html_show += "<td>"
                            html_show += result.data.singer
                        html_show += "</td>"
                        html_show += "<td>"
                            html_show += result.data.sstatus
                        html_show += "</td>"
                        $(".like_show").html(html_show)
                    }else{
                        $(".like_show").html("空空如也")
                    }
                }else{
                alert(result.error);
            }
        }
    })

}

function boughtShow() {
    $.ajax({
        type: "GET",
        // http://127.0.0.1:8000/v1/users/bernard?bought=1
        url: "http://127.0.0.1:8000/v1/users/" + blog_username + "?bought=1",
        beforeSend: function(request) {
             request.setRequestHeader("Authorization", token);
         },
        success: function (result) {
            if (result.code == 200) {
                var html_show = "";
                html_show = "<table class='table table-striped'>"
                html_show += "<tr>"
                html_show += "<th>"
                html_show += "id"
                html_show += "</th>"
                html_show += "<th>"
                html_show += "sing"
                html_show += "</th>"
                html_show += "<th>"
                html_show += "singer"
                html_show += "</th>"
                html_show += "<th>"
                html_show += "bought time"
                html_show += "</th>"
                html_show += "</tr>"
                $(".bought_show").html(html_show);
            }else{
                alert(result.error)
            }
        }

    })
}