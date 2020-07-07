function login() {
        var username = $("#username").val();
        var password = $("#password").val();

        var post_data = {"username": username, "password": password};

        $.ajax({
            url: "http://127.0.0.1:8000/v1/tokens",
            type: "POST",
            dataType: "json",
            data: JSON.stringify(post_data),
            contentType: "application/json",
            success: function (res) {
                if (res.code == 200){
                    alert("登录成功!")
                    window.localStorage.setItem("bcmusic_token", res.data.token);
                    window.localStorage.setItem("bcmusic_user", res.username);
                    window.location.href = username + "/info"
                }else{
                    alert(res.error)
                }
            }
        })
}