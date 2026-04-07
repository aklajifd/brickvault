<template>
  <div class="home-view">
    <div class="hero">
      <div class="hero-text">
        <h1>Welcome to BrickVault</h1>
        <p class="tagline">Your personal LEGO collection tracker.</p>
        <p class="description">
          Add sets by number, track your piece count, and organize your
          collection by theme — all in one place.
        </p>
        <div class="hero-actions">
          <RouterLink to="/collection" class="btn-primary">
            View Collection
          </RouterLink>
          <RouterLink to="/stats" class="btn-secondary">
            View Stats
          </RouterLink>
        </div>
      </div>
      <div class="hero-graphic">
        <div class="big-brick">
          <div class="big-studs">
            <div class="big-stud" v-for="n in 8" :key="n" />
          </div>
          <div class="big-brick-face">
            🧱
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home-view {
  min-height: 70vh;
  display: flex;
  align-items: center;
}

.hero {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 4rem;
  width: 100%;
}

.hero-text {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.hero-text h1 {
  font-size: 2.5rem;
  font-weight: 700;
  color: #242424;
  line-height: 1.2;
}

.tagline {
  font-size: 1.25rem;
  color: #f59e0b;
  font-weight: 500;
}

.description {
  font-size: 1rem;
  color: #666;
  line-height: 1.6;
  max-width: 480px;
}

.hero-actions {
  display: flex;
  gap: 1rem;
  margin-top: 0.5rem;
}

.btn-primary {
  padding: 0.75rem 1.75rem;
  background: #f59e0b;
  color: white;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 500;
  font-size: 1rem;
  transition: background 0.2s;
}

.btn-primary:hover {
  background: #d97706;
}

.btn-secondary {
  padding: 0.75rem 1.75rem;
  background: white;
  color: #242424;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 500;
  font-size: 1rem;
  transition: border-color 0.2s;
}

.btn-secondary:hover {
  border-color: #f59e0b;
}

.hero-graphic {
  flex: 0 0 auto;
}

.big-brick {
  position: relative;
  background: #f59e0b;
  border-radius: 10px;
  padding-top: 36px;
  width: 240px;
  box-shadow:
    0 10px 0 #d97706,
    0 14px 20px rgba(0,0,0,0.2);
  transform: rotateX(4deg) rotate(-4deg);
}

.big-studs {
  position: absolute;
  top: -18px;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  gap: 10px;
  flex-wrap: wrap;
  padding: 0 16px;
}

.big-stud {
  width: 28px;
  height: 28px;
  background: #f59e0b;
  border-radius: 50%;
  border: 2px solid #d97706;
  box-shadow:
    0 -4px 0 #d97706,
    inset 0 2px 4px rgba(255,255,255,0.3);
}

.big-brick-face {
  background: rgba(255,255,255,0.08);
  border-radius: 0 0 10px 10px;
  padding: 2rem;
  font-size: 5rem;
  text-align: center;
}
</style>