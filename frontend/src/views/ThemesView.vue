<template>
  <div class="themes-view">
    <h1>Themes</h1>

    <div v-if="store.loading" class="state-message">
      Loading themes...
    </div>

    <div v-else-if="store.themes.length === 0" class="state-message">
      No themes yet. Add some sets to your collection first!
    </div>

    <div v-else class="themes-grid">
      <div
        v-for="theme in store.themes"
        :key="theme.id"
        class="theme-card"
        @click="selectedTheme = selectedTheme?.id === theme.id ? null : theme"
      >
        <div class="theme-name">{{ theme.name }}</div>
        <div class="theme-id" v-if="theme.rebrickable_id">
          Rebrickable #{{ theme.rebrickable_id }}
        </div>
      </div>
    </div>

    <div v-if="selectedTheme" class="theme-sets">
      <h2>{{ selectedTheme.name }} Sets</h2>
      <div v-if="themeLoading" class="state-message">Loading sets...</div>
      <div v-else class="sets-list">
        <div
          v-for="set in themeSets"
          :key="set.id"
          class="set-row"
        >
          <img
            v-if="set.image_url"
            :src="set.image_url"
            :alt="set.name"
            class="set-thumb"
          />
          <div v-else class="set-thumb-placeholder">🧱</div>
          <div class="set-details">
            <span class="set-name">{{ set.name }}</span>
            <span class="set-meta">#{{ set.set_number }} · {{ set.piece_count?.toLocaleString() }} pieces · {{ set.year }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import { useStatsStore } from '../stores/stats'
import { fetchSetsByTheme } from '../services/api'

const store = useStatsStore()
const selectedTheme = ref(null)
const themeSets = ref([])
const themeLoading = ref(false)

onMounted(async () => {
  await store.loadThemes()
})

watch(selectedTheme, async (theme) => {
  if (!theme) {
    themeSets.value = []
    return
  }
  themeLoading.value = true
  try {
    const response = await fetchSetsByTheme(theme.id)
    themeSets.value = response.data
  } finally {
    themeLoading.value = false
  }
})
</script>

<style scoped>
.themes-view {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.themes-view h1 {
  font-size: 1.75rem;
  font-weight: 700;
}

.themes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 1rem;
}

.theme-card {
  background: white;
  border-radius: 12px;
  padding: 1.25rem;
  cursor: pointer;
  border: 2px solid transparent;
  transition: border-color 0.2s, transform 0.2s;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.theme-card:hover {
  border-color: #f59e0b;
  transform: translateY(-2px);
}

.theme-name {
  font-weight: 600;
  font-size: 1rem;
  color: #242424;
}

.theme-id {
  font-size: 0.8rem;
  color: #aaa;
  margin-top: 0.25rem;
}

.theme-sets {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.theme-sets h2 {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.sets-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.set-row {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.5rem;
  border-radius: 8px;
  transition: background 0.15s;
}

.set-row:hover {
  background: #fafafa;
}

.set-thumb {
  width: 60px;
  height: 60px;
  object-fit: contain;
  border-radius: 6px;
  background: #f5f5f5;
}

.set-thumb-placeholder {
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  background: #f5f5f5;
  border-radius: 6px;
}

.set-details {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.set-name {
  font-weight: 500;
  color: #242424;
}

.set-meta {
  font-size: 0.85rem;
  color: #888;
}

.state-message {
  color: #888;
  padding: 2rem;
  text-align: center;
}
</style>