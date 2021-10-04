const todoApp = {
  data() {
    return {
      newTodo: "",
      completeItems: [
        {
          id: 1,
          name: "test",
          completed: true,
        },
      ],
      items: [
        {
          id: 1,
          name: "test",
          completed: false,
        },
      ],
    };
  },
  methods: {
    addTodo: function () {
      this.items.push({
        id: this.items.length + 1,
        name: this.newTodo,
        completed: false,
      });
      this.newTodo = "";
    },
    toggleCompleted: function (item) {
      item.completed = true;
      this.completeItems.push({
        id: this.length + 1,
        name: item.name,
        completed: item.completed,
      });
      this.items = this.items.filter((newItem) => newItem.name !== item.name);
    },
    toggleIncomplete: function (item) {
      item.completed = false;
      this.items.push({
        id: this.length + 1,
        name: item.name,
        completed: item.completed,
      });
      this.completeItems = this.completeItems.filter((newItem) => newItem.name !== item.name);
    },
    removeTodo: function (item) {
      this.items = this.items.filter((newItem) => newItem.name !== item.name);
    },
  },
};

Vue.createApp(todoApp).mount("#app");
