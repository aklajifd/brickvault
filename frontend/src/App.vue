<template>
  <div>
    <AppNavbar />
    <main class="main-content">
      <RouterView />
    </main>
  </div>
</template>

<script setup>
import AppNavbar from './components/layout/AppNavbar.vue'
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Inter', sans-serif;
  background-color: #f5f5f5;
  color: #242424;
}

.main-content {
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}
</style>