const App = {
  data() {
    return {
      searchTerm: "",
      singleTerm: "",
      searchResults: [],
    };
  },

  methods: {
    searchCountry() {
      console.log(this.searchTerm);
      axios({
        method: "GET",
        url: "https://restcountries.com/v3/name/" + this.searchTerm,
      }).then((response) => {
        console.log(response.data);
        this.searchResults = response.data;
        this.searchTerm = "";
      });
    },
    searchSingle() {
      console.log(this.searchTerm);
    },
  },
};
Vue.createApp(App).mount("#app");
