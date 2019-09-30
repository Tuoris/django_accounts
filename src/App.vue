<template>
  <div class="container mt-2" id="app">
    <AddAccount
      v-on:close="closeAddAccount"
      v-on:reset="resetAddAccount"
      v-show="isAddFormVisible"
      v-on:add="addAccount"
      v-bind:errors="addAccountErrors"
      v-bind:disabled="isAddFormDisabled"
      ref="account-form"
    />
    <button v-on:click="showAddAccount" class="btn btn-primary my-1">Add new Account</button>
    <div class="row">
      <Account
        v-for="account in accounts"
        v-bind:account="account"
        v-bind:key="account.id"
        v-on:delete="deleteAccount"
      />
    </div>
  </div>
</template>

<script>
import Account from "./components/Account.vue";
import AddAccount from "./components/AddAccount.vue";

export default {
  name: "app",
  data: function() {
    return {
      isAddFormVisible: false,
      isAddFormDisabled: false,
      addAccountErrors: [],
      accounts: []
    };
  },

  components: {
    Account,
    AddAccount
  },

  methods: {
    addAccount: function(account) {
      let vm = this;
      vm.isAddFormDisabled = true;

      let response_succeed = false;
      fetch("api/accounts/", {
        method: "POST",
        body: JSON.stringify(account),
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json"
        }
      }).then(response => {
        vm.isAddFormDisabled = false;
        if (!response.ok) {
          if (response.headers.get('Content-Type') != 'application/json') {
            return Promise.reject(null);
          }
        } else {
          response_succeed = true;
          vm.$refs['account-form'].reset();
          vm.resetAddAccount();
          vm.closeAddAccount();
        }
        return response.json();
      }).then(json_data => {
        if (response_succeed) {
          vm.fetchAccounts();
        } else {
          vm.addAccountErrors = Object.entries(json_data);
        }
      });
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

    showAddAccount: function(event) {
      this.isAddFormVisible = true;
    },

    closeAddAccount: function(event) {
      this.isAddFormVisible = false;
    },

    resetAddAccount: function(event) {
      this.addAccountErrors = [];
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
