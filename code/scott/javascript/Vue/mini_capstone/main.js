const App = {
    data() {
      return {
        searchTerm: "",
        searchResults: [],
      };
    },
  
    methods: {
      searchValid() {
        console.log(this.searchTerm);
        this.newHeader = "Search Results:";
        this.quotes = [];
        axios({
          method: "get",
          url: "https://api.gsa.gov/technology/digital-registry/v1/agencies",
          headers: {
            Authorization: 'VIuNIA5XU3PoRj8jK8cViP8LAWRACLml1Put4DbU',
            "Content-Type": "application/json",
          },
          params: {
            description: this.searchTerm,
            type: this.searchType,
            page: this.pageCounter,
          },
        }).then((response) => {
          console.log(response.data.quotes);
          this.searchResults = response.data.quotes;
        });
      },
    },
  };
  Vue.createApp(App).mount("#app");
  