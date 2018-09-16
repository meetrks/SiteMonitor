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
        newSite: {'site_name': null, 'site_url': null}
      },
      mounted: function() {
        this.getSiteData();
      },
      methods: {
        getSiteData: function() {
          let url = '/site/';
          this.$http.get(url)
              .then((response) => {
                let data = response.data;
                this.sites = data.results;
                this.next_page = data.next;
                this.prev_page = data.previous;
                this.total_page = data.count;
              })
              .catch((err) => {
                console.log(err);
              })
        },
        getSiteDetails: function(id) {
          let url = `/site/${id}/`;
          this.$http.get(url)
              .then((response) => {
                this.site_details = response.data;
                $("#editSiteModal").modal('show');

              })
              .catch((err) => {
                console.log(err);
              })
        },
        updateSiteDetails: function(id) {
          this.$http.put(`/site/${this.site_details.id}/`, this.site_details)
              .then((response) => {
                this.site_details = response.data;
                $("#editSiteModal").modal('hide');
                this.getSiteData();

              })
              .catch((err) => {
                console.log(err);
              })
        },
        addNewSite: function(id) {
          this.$http.post(`/site/`, this.newSite)
              .then((response) => {
                this.site_details = response.data;
                $("#addSiteModal").modal('hide');
                this.getSiteData();

              })
              .catch((err) => {
                console.log(err);
              })
        },

      }
    });