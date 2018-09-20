    new Vue({
      el: '#app-main',
      delimiters: ['${','}'],
      data: {
        sites: [],
        next_page: null,
        prev_page: null,
        total_page: 1,
        message: null,
        site_details: {},
        newSite: {'site_name': null, 'site_url': null},
        token: localStorage.getItem('access_token') || null,

        member_dir: {
            members: [],
            newMember: {'member_name': null, 'email': null, 'mobile': null},
            member_details: {}
        },

        roles: {
            roles: [],
            newRole: {'role_name': null, 'alert_diff': null},
            role_details: {}
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
        getSiteData: function() {
          let url = '/site/';
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
                this.total_page = data.count;
              })
              .catch((err) => {
                if(err.status == 401){
                    window.location = '/auth/login'
                }
              })
        },
        getSiteDetails: function(id) {
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
                }
              })
        },
        addNewSite: function(id) {
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
                }
              })
        },
        userLogout: function() {
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
        },
        getMemberData: function() {
          let url = '/memberdir/member/';
          this.$http.get(url, {
                headers: {
                'Authorization': this.token
              }
              })
              .then((response) => {
                let data = response.data;
                this.member_dir.members = data.results;
                this.next_page = data.next;
                this.prev_page = data.previous;
                this.total_page = data.count;
              })
              .catch((err) => {
                if(err.status == 401){
                    window.location = '/auth/login'
                }
              })
        },
        addNewMember: function(id) {
          this.$http.post(`/memberdir/member/`, this.member_dir.newMember, {
                headers: {
                'Authorization': this.token
              }
              })
              .then((response) => {
                this.member_dir.member_details = response.data;
                $("#addMemberModal").modal('hide');
                this.member_details.newMember = {};
                this.getMemberData();

              })
              .catch((err) => {
                if(err.status == 401){
                    window.location = '/auth/login'
                }
              })
        },
        getMemberDetails: function(id) {
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
                }
              })
        },

        getRoleData: function() {
          let url = '/roles/role/';
          this.$http.get(url, {
                headers: {
                'Authorization': this.token
              }
              })
              .then((response) => {
                let data = response.data;
                this.roles.roles = data.results;
                this.next_page = data.next;
                this.prev_page = data.previous;
                this.total_page = data.count;
              })
              .catch((err) => {
                if(err.status == 401){
                    window.location = '/auth/login'
                }
              })
        },
        addNewRole: function(id) {
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
                }
              })
        },
        getRoleDetails: function(id) {
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
                }
              })
        },
      }
    });