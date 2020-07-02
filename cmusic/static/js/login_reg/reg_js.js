var countdown=60;
function settime(obj) {
    if (countdown == 0) {
        obj.removeAttribute("disabled");
        obj.value="免费获取验证码";
        countdown = 60;
        return;
    } else {
        obj.setAttribute("disabled", true);
        obj.value="重新发送(" + countdown + ")";
        countdown--;
    }
    setTimeout(function() {
        settime(obj) }
    ,1000)
}

function regist() {
    var username = $("#username").val();
    var password_1 = $("#password_1").val();
    var password_2 = $("#password_2").val();
    var phone = $("#phone").val();
    var nickname = $("#nickname").val();

    var post_data = {"username": username, "password_1": password_1, "password_2": password_2, "phone": phone, "nickname": nickname};

    $.ajax({
        url: "http://127.0.0.1:8000/v1/users",
        type: "POST",
        dataType: "json",
        data: JSON.stringify(post_data),
        contentType: "application/json",
        success: function (res) {
            if (res.code == 200) {
                alert("注册成功")
                window.localStorage.setItem("bcmusic_token", res.data.token);
                window.localStorage.setItem("bcmusic_user", res.username);
            }else{
                alert(res.error);
            }


        }
    })








}