<template>
  <div class="card col-sm-6 col-md-3 p-0">
    <div class="avatar-image-container">
      <img v-if="account.avatar" v-bind:src="account.avatar" class="avatar-image card-img-top" />
      <img v-else src="/static/no-avatar.png" class="avatar-image card-img-top" />
    </div>
    <div class="card-body">
      <h5 class="card-title">{{ account.first_name }} {{ account.last_name }}</h5>
      <p class="card-text">Created {{ account.creation_date }}</p>
      <div class="btn-group mr-1 ml-1">
        <button v-on:click="deleteAccount" class="btn btn-danger">Delete</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Account",
  props: {
    account: Object
  },
  methods: {
    deleteAccount: function(event) {
      this.$emit('delete', this.account);
    }
  }
};
</script>

<style scoped>
.avatar-image-container {
  overflow: hidden;
  padding-bottom: 80%;
  position: relative;
}

.avatar-image {
  position: absolute;
  top: 0;
  left: 0;
}
</style>
