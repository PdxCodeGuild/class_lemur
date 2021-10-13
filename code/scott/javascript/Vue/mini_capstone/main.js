const App = {
  data() {
    return {
      searchTerm: "",
      singleTerm: "",
      googleLink:"https://www.google.com/search?q=",
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
        this.flagLink = this.searchResults[0].flags[0];
      });
    },
    searchSingle(newSearch) {
      this.searchTerm = newSearch;
      this.searchCountry();
    },
    searchGoogle(city) {
      window.open(this.googleLink + city)
    }
  },
};
Vue.createApp(App).mount("#app");
