<template>
    <div class="footer">
        <p>Connection State: {{ connected }}</p>
    </div>
</template>

<style scoped>
</style>

<script>
import { state } from "@/socket";

export default {
  name: "Footer",

  computed: {
    connected() {
      return state.connected;
    }
  }
}
</script>