    Vue.filter('timeStampToDateTime', function(value) {
      if (value) {
        return moment.unix(value).format('DD-MM-YYYY hh:mm:ss')
      }else{
        return "-"
      }
    });

    new Vue({
      el: '#app-main',
      delimiters: ['${','}'],
      data: {
        sites: [],
        next_page: null,
        prev_page: null,
        total_page: 1,
        current_page: 1,
        error_msg: null,
        site_details: {},
        newSite: {'site_name': null, 'site_url': null},
        token: localStorage.getItem('access_token') || null,

        member_dir: {
            members: [],
            newMember: {'member_name': null, 'email': null, 'mobile': null},
            member_details: {},
            next_page: null,
            prev_page: null,
            total_page: 1,
            current_page: 1,
        },

        roles: {
            roles: [],
            newRole: {'role_name': null, 'alert_diff': null},
            role_details: {},
            next_page: null,
            prev_page: null,
            total_page: 1,
            current_page: 1,
        }
      },
      mounted: function() {
        if (!this.token){
            window.location = '/auth/login'
        }
        this.getSiteData();
        this.getMemberData();
        this.getRoleData();
      },
      methods: {
        getSiteData: function(url_) {
          this.error_msg = null
          let url = '/site/';
          if (url_){
            url = url_
          }
          this.$http.get(url, {
                headers: {
                'Authorization': this.token
              }
              })
              .then((response) => {
                let data = response.data;
                this.sites = data.results;
                this.next_page = data.next;
                this.prev_page = data.previous;
                this.total_page = data.last_page;
                this.current_page = data.current_page;
              })
              .catch((err) => {
                if(err.status == 401){
                    window.location = '/auth/login'
                }
              })
        },
        getSiteDetails: function(id) {
          this.error_msg = null
          let url = `/site/${id}/`;
          this.$http.get(url, {
                headers: {
                'Authorization': this.token
              }
              })
              .then((response) => {
                this.site_details = response.data;
                $("#editSiteModal").modal('show');

              })
              .catch((err) => {
                if(err.status == 401){
                    window.location = '/auth/login'
                }
              })
        },
        updateSiteDetails: function(id) {
          this.error_msg = null
          this.$http.put(`/site/${this.site_details.id}/`, this.site_details, {
                headers: {
                'Authorization': this.token
              }
              })
              .then((response) => {
                this.site_details = response.data;
                $("#editSiteModal").modal('hide');
                this.getSiteData();

              })
              .catch((err) => {
                if(err.status == 401){
                    window.location = '/auth/login'
                }else{
                    try{
                        this.error_msg = err.body.non_field_errors[0]
                    }catch{
                        this.error_msg = err.body.detail
                    }

                }
              })
        },
        addNewSite: function(id) {
          this.error_msg = null
          this.$http.post(`/site/`, this.newSite, {
                headers: {
                'Authorization': this.token
              }
              })
              .then((response) => {
                this.site_details = response.data;
                $("#addSiteModal").modal('hide');
                this.newSite = {};
                this.getSiteData();

              })
              .catch((err) => {
                if(err.status == 401){
                    window.location = '/auth/login'
                }else{
                    try{
                        this.error_msg = err.body.non_field_errors[0]
                    }catch{
                        this.error_msg = err.body.detail
                    }

                }
              })
        },
        userLogout: function() {
            this.error_msg = null
            swal({
              title: 'Are you sure?',
              text: "You will be returned to login screen.",
              type: 'warning',
              showCancelButton: true,
              confirmButtonColor: '#3085d6',
              cancelButtonColor: '#d33',
              confirmButtonText: 'Logout'
            }).then((result) => {
              if (result.value) {
                    this.$http.post(`/rest-auth/logout/`, {
                    headers: {
                    'Authorization': this.token
                  }
                  })
                  .then((response) => {
                    localStorage.removeItem('access_token')
                    this.token = null
                    window.location = '/auth/login'
                  })
                  .catch((err) => {
                    if(err.status == 401){
                        window.location = '/auth/login'
                    }
                  })
              }
            })
        },
        getMemberData: function(url_) {
          this.error_msg = null
          let url = '/memberdir/member/';
          if (url_){
            url = url_
          }
          this.$http.get(url, {
                headers: {
                'Authorization': this.token
              }
              })
              .then((response) => {
                let data = response.data;
                this.member_dir.members = data.results;
                this.member_dir.next_page = data.next;
                this.member_dir.prev_page = data.previous;
                this.member_dir.total_page = data.last_page;
                this.member_dir.current_page = data.current_page;
              })
              .catch((err) => {
                if(err.status == 401){
                    window.location = '/auth/login'
                }
              })
        },
        addNewMember: function(id) {
          this.error_msg = null
          this.$http.post(`/memberdir/member/`, this.member_dir.newMember, {
                headers: {
                'Authorization': this.token
              }
              })
              .then((response) => {
                this.member_dir.member_details = response.data;
                $("#addMemberModal").modal('hide');
                this.member_dir.newMember = {};
                this.getMemberData();

              })
              .catch((err) => {
                if(err.status == 401){
                    window.location = '/auth/login'
                }else{
                    try{
                        this.error_msg = err.body.non_field_errors[0]
                    }catch{
                        this.error_msg = err.body.detail
                    }

                }
              })
        },
        getMemberDetails: function(id) {
          this.error_msg = null
          let url = `/memberdir/member/${id}/`;
          this.$http.get(url, {
                headers: {
                'Authorization': this.token
              }
              })
              .then((response) => {
                this.member_dir.member_details = response.data;
                $("#editMemberModal").modal('show');

              })
              .catch((err) => {
                if(err.status == 401){
                    window.location = '/auth/login'
                }
              })
        },
        updateMemberDetails: function(id) {
          this.error_msg = null
          this.$http.put(`/memberdir/member/${this.member_dir.member_details.id}/`, this.member_dir.member_details, {
                headers: {
                'Authorization': this.token
              }
              })
              .then((response) => {
                this.member_dir.member_details = response.data;
                $("#editMemberModal").modal('hide');
                this.getMemberData();

              })
              .catch((err) => {
                if(err.status == 401){
                    window.location = '/auth/login'
                }else{
                    try{
                        this.error_msg = err.body.non_field_errors[0]
                    }catch{
                        this.error_msg = err.body.detail
                    }

                }
              })
        },

        getRoleData: function(url_) {
          this.error_msg = null
          let url = '/roles/role/';
          if (url_){
            url = url_
          }
          this.$http.get(url, {
                headers: {
                'Authorization': this.token
              }
              })
              .then((response) => {
                let data = response.data;
                this.roles.roles = data.results;
                this.roles.next_page = data.next;
                this.roles.prev_page = data.previous;
                this.roles.total_page = data.last_page;
                this.roles.current_page = data.current_page;
              })
              .catch((err) => {
                if(err.status == 401){
                    window.location = '/auth/login'
                }
              })
        },
        addNewRole: function(id) {
          this.error_msg = null
          this.$http.post(`/roles/role/`, this.roles.newRole, {
                headers: {
                'Authorization': this.token
              }
              })
              .then((response) => {
                this.roles.role_details = response.data;
                $("#addRoleModal").modal('hide');
                this.roles.newRole = {}
                this.getRoleData();

              })
              .catch((err) => {
                if(err.status == 401){
                    window.location = '/auth/login'
                }else{
                    try{
                        this.error_msg = err.body.non_field_errors[0]
                    }catch{
                        this.error_msg = err.body.detail
                    }

                }
              })
        },
        getRoleDetails: function(id) {
          this.error_msg = null
          let url = `/roles/role/${id}/`;
          this.$http.get(url, {
                headers: {
                'Authorization': this.token
              }
              })
              .then((response) => {
                this.roles.role_details = response.data;
                $("#editRoleModal").modal('show');

              })
              .catch((err) => {
                if(err.status == 401){
                    window.location = '/auth/login'
                }
              })
        },
        updateRoleDetails: function(id) {
          this.error_msg = null
          this.$http.put(`/roles/role/${this.roles.role_details.id}/`, this.roles.role_details, {
                headers: {
                'Authorization': this.token
              }
              })
              .then((response) => {
                this.roles.role_details = response.data;
                $("#editRoleModal").modal('hide');
                this.getRoleData();

              })
              .catch((err) => {
                if(err.status == 401){
                    window.location = '/auth/login'
                }else{
                    try{
                        this.error_msg = err.body.non_field_errors[0]
                    }catch{
                        this.error_msg = err.body.detail
                    }

                }
              })
        },
      }
    });