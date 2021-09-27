const App = {
  data() {
    return {
      addTodoInput: "",
      tdList: [],
    };
  },
  methods: {
    addTodo: function () {
      this.tdList.push({
        id: this.tdList.length + 1,
        title: this.addTodoInput,
        isComplete: false,
      });
      this.usrInput = "";
    },
  },
  todoComplete: function (tdList) {
    tdList.isComplete = !tdList.isComplete;
    
  },
  todoRemove: function(tdList) {
      let index = this.tdList.id
  }
};

Vue.createApp(App).mount("#todoapp");
