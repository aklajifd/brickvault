<template>
  <nav class="navbar">
    <div class="navbar-brand">🧱 BrickVault</div>
    <div class="navbar-links">
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/collection">Collection</RouterLink>
      <RouterLink to="/themes">Themes</RouterLink>
      <RouterLink to="/stats">Status</RouterLink>
    </div>
    <button class="signout-btn" @click="handleSignOut">
      Sign Out
    </button>
  </nav>
</template>

<script setup>
import { useAuthStore } from '../../stores/auth';
import { useRouter } from 'vue-router'

const authStore = useAuthStore()
const router = useRouter()

async function handleSignOut() {
  await authStore.signOut()
  router.push('/login')
}
</script>

<style scoped>
.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 2rem;
  background-color: #242424;
  color: white;
}

.navbar-brand {
  font-size: 1.5rem;
  font-weight: bold;
}

.navbar-links {
  display: flex;
  gap: 2rem;
}

.navbar-links a {
  color: white;
  text-decoration: none;
  font-size: 1rem;
}

.navbar-links a.router-link-active {
  color: #f59e0b;
  font-weight: bold;
}

.signout-btn {
  background: transparent;
  border: 1px solid rgba(255, 255, 255, 0.3);
  color: white;
  padding: 0.4rem 1rem;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: background 0.2s;
}

.signout-btn:hover {
  background: rgba(255, 255, 255, 0.1);
}
</style>