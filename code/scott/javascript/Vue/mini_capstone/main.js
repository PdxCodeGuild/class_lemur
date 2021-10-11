const App = {
    data() {
      return {
        searchTerm: "",
        searchResults: [],
      };
    },
  
    methods: {
      searchAnime() {
        console.log(this.searchTerm);
        axios({
          method: "POST",
          url: "https://graphql.anilist.co/",
          headers: {
            Accept: 'application/vnd.api+json',
            'Content-Type': 'application/vnd.api+json',
          },
          params: {
            query: this.searchTerm,
            variables: {page: 1, perPage: 10},
          },
        }).then((response) => {
          console.log(response.data);
        });
      },
    },
  };
  Vue.createApp(App).mount("#app");
  