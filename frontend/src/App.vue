<template>
  <div>
    <AppNavbar v-if="useAuthStore.isAuthenticated" />
    <main class="main-content">
      <RouterView />
    </main>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useAuthStore } from './stores/auth';
import AppNavbar from "./components/layout/AppNavbar.vue";

const authStore = useAuthStore()

onMounted(async () => {
  await authStore.initialize()
})
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: "Inter", sans-serif;
  background-color: #f5f5f5;
  color: #242424;
}

.main-content {
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}
</style>