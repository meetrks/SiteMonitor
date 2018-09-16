    new Vue({
      el: '#app-main',
      delimiters: ['${','}'],
      data: {
        loginData: {'username': null, 'password': null},
        token: localStorage.getItem('access_token') || null,
        error_msg: null
      },
      mounted: function() {
        if (this.token){
            window.location = '/'
        }
      },
      methods: {
        userLogin: function() {
          let url = '/rest-auth/login/';
          this.$http.post(url, this.loginData)
              .then((response) => {
                let token = response.data.key;
                localStorage.setItem('access_token', 'Token ' + token)
                window.location = '/'
                this.error_msg = null;
              })
              .catch((err) => {
                this.error_msg = err.body.non_field_errors[0]
              })
        },
        userLoginPage: function(){
            window.location = '/auth/login'
        },
      }
    });