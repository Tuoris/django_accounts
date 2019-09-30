<template>
  <div>
    <div class="add-account-modal-background"></div>
    <div class="modal add-account-modal" tabindex="-1" role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h3 class="modal-title">Add account</h3>
            <button
              type="button"
              v-on:click="close"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <div v-for="error in errors" v-bind:key="error[0]" class="alert alert-danger" role="alert">
              {{ error[0] }}: {{ error[1][0] }}
            </div>
            <form>
              <div class="form-group">
                <img v-bind:src="account.avatar" class="avatar-preview">
                <br>
                <button v-on:click="removeImage" class="btn btn-primary" v-if="account.avatar">Remove image</button>
              </div>
              <div class="form-group">
                <label for="avatar">Avatar</label><br>
                <input type="file" id="avatar" v-on:change="loadAccountImage" class="btn btn-primary" accept="image/x-png,image/gif,image/jpeg"/>
              </div>
              <div class="form-group">
                <label for="first_name">First name</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="account.first_name"
                  id="first_name"
                />
              </div>
              <div class="form-group">
                <label for="last_name">Last name</label>
                <input type="text" class="form-control" v-model="account.last_name" id="last_name" />
              </div>
              <div class="form-group btn-toolbar justify-content-center">
                <div class="btn-group mr-2">
                  <button v-on:click="reset" type="button" class="btn btn-primary">Cancel</button>
                </div>
                <div class="btn-group mr-2">
                  <button type="button" v-on:click="addAccount" class="btn btn-primary" :disabled="disabled">Add</button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const default_data = function() {
  return {
    account: {
      first_name: null,
      last_name: null,
      avatar: null
    }
  };
};

export default {
  name: "AddAccount",
  props: {
    errors: Array,
    disabled: Boolean
  },
  data: function() {
    return default_data();
  },
  methods: {
    close: function(event) {
      this.$emit("close");
    },
    reset(event) {
      document.querySelector("#avatar").value = null;
      this.account = default_data().account;
      this.$emit("reset");
      this.close(event);
    },
    addAccount: function(event) {
      this.$emit("add", this.account);
    },

    loadAccountImage: function(event) {
      var files = event.target.files || event.dataTransfer.files;
      if (!files.length) return;
      this.createImage(files[0]);
    },

    createImage(file) {
      var vm = this;
      var image = new Image();
      var reader = new FileReader();

      reader.onload = event => {
        vm.account.avatar = event.target.result;
      };
      reader.readAsDataURL(file);
    },

    removeImage: function(e) {
      this.account.avatar = null;
    }
  }
};
</script>

<style scoped>
.add-account-modal-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.6);
  z-index: 10;
}
.add-account-modal {
  display: block;
}

.avatar-preview {
  max-width: 6em;
  max-height: 6em;
}
</style>
