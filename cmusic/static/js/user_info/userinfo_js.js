
var url = document.location.toString();
var arrUrl = url.split("//");
//当前访问的博客博主
var blog_username = arrUrl[1].split('/')[1];

var html_show = ""


function showLike() {
    $.ajax({
        url: "http://127.0.0.1:8000/v1/users/"+ blog_username,

    })
}