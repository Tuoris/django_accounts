<template>
  <div class="container mt-2" id="app">
    <div class="row">
      <Account
        v-for="account in accounts"
        v-bind:account="account"
        v-bind:key="account.id"
        v-on:edit="editAccount"
        v-on:delete="deleteAccount"
      />
    </div>
  </div>
</template>

<script>
import Account from "./components/Account.vue";

export default {
  name: "app",
  data: function() {
    return {
      accounts: []
    };
  },

  components: {
    Account,
    AddAccount,
  },

  methods: {
    editAccount: function(account) {
      console.log(account);
    },

    deleteAccount: function(account) {
      this.accounts = this.accounts.filter(
        existing_account => existing_account.id !== account.id
      );
      fetch("api/accounts/" + account.id, { method: "DELETE" }).then(
        response => {
          if (!response.ok) {
            this.accounts.push(account);
          }
        }
      );
    },

    fetchAccounts: function() {
      fetch("api/accounts")
        .then(response => response.json())
        .then(json_data => (this.accounts = json_data));
    }
  },

  mounted() {
    this.fetchAccounts();
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
