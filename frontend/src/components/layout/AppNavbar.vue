<template>
  <nav class="navbar">
    <div class="navbar-brand">🧱 BrickVault</div>
    <div class="navbar-links">
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/collection">Collection</RouterLink>
      <RouterLink to="/themes">Themes</RouterLink>
      <RouterLink to="/stats">Status</RouterLink>
    </div>
  </nav>
</template>

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
</style>