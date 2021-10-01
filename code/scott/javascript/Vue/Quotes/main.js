const App = {
  data() {
    return {
      searchTerm: "",
      searchResults: [],
      pageCounter: 0,
    };
  },

  methods: {
    searchValid() {
      console.log(this.searchTerm);
      this.newHeader = "Search Results:";
      this.quotes = [];
      this.pageCounter = 0;
      this.pageCounter++;
      axios({
        method: "get",
        url: "https://favqs.com/api/quotes/",
        headers: {
          Authorization: 'Token token="9ecb9bcc0aaac8e9d8ab9e20455ab648"',
          "Content-Type": "application/json",
        },
        params: {
          filter: this.searchTerm,
          type: this.searchType,
          page: this.pageCounter,
        },
      }).then((response) => {
        console.log(response.data.quotes);
        this.searchResults = response.data.quotes;
      });
    },
    pageLow() {
      this.pageCounter--;
      axios({
        method: "get",
        url: "https://favqs.com/api/quotes/",
        headers: {
          Authorization: 'Token token="9ecb9bcc0aaac8e9d8ab9e20455ab648"',
          "Content-Type": "application/json",
        },
        params: {
          filter: this.searchTerm,
          type: this.searchType,
          page: this.pageCounter,
        },
      }).then((response) => {
        console.log(response.data.quotes);
        this.searchResults = response.data.quotes;
      });
    },
    pageHigh() {
      this.pageCounter++;
      axios({
        method: "get",
        url: "https://favqs.com/api/quotes/",
        headers: {
          Authorization: 'Token token="9ecb9bcc0aaac8e9d8ab9e20455ab648"',
          "Content-Type": "application/json",
        },
        params: {
          filter: this.searchTerm,
          type: this.searchType,
          page: this.pageCounter,
        },
      }).then((response) => {
        console.log(response.data.quotes);
        this.searchResults = response.data.quotes;
      });
    },
  },
  created() {
    this.randomQuotes();
  },
};
Vue.createApp(App).mount("#app");
