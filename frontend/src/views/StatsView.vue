<template>
  <div class="stats-view">
    <h1>Stats</h1>

    <div v-if="store.loading" class="state-message">
      Loading stats...
    </div>

    <template v-else-if="store.stats">
      <div class="bricks-grid">
        <StatsBrick
          label="Total Sets"
          :value="store.stats.total_sets"
          icon="📦"
          color="#f59e0b"
          darkColor="#d97706"
          :studs="4"
        />
        <StatsBrick
          label="Total Pieces"
          :value="store.stats.total_pieces"
          icon="🧱"
          color="#ef4444"
          darkColor="#dc2626"
          :studs="4"
        />
        <StatsBrick
          label="Avg Pieces per Set"
          :value="store.stats.avg_pieces"
          icon="📊"
          color="#3b82f6"
          darkColor="#2563eb"
          :studs="4"
          format="decimal"
        />
        <StatsBrick
          label="Largest Set"
          :value="store.stats.largest_set_pieces"
          icon="🏆"
          color="#10b981"
          darkColor="#059669"
          :studs="4"
        />
      </div>

      <ThemeChart :data="themeChartData" />
    </template>

    <div v-else class="state-message">
      Add some sets to your collection to see stats!
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useCollectionStore } from '../stores/collection'
import { useStatsStore } from '../stores/stats'
import StatsBrick from '../components/stats/StatsBrick.vue'
import ThemeChart from '../components/stats/ThemeChart.vue'

const store = useCollectionStore()
const themeStore = useStatsStore()

const themeChartData = computed(() => {
  const themeCounts = {}
  store.collection.forEach(entry => {
    const theme = entry.lego_set.theme_name || 'Unknown'
    themeCounts[theme] = (themeCounts[theme] || 0) + 1
  })
  return Object.entries(themeCounts)
    .map(([theme, count]) => ({ theme, count }))
    .sort((a, b) => b.count - a.count)
})

onMounted(async () => {
  await store.loadCollection()
  await store.loadStats()
  await themeStore.loadThemes()
})
</script>

<style scoped>
.stats-view {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.stats-view h1 {
  font-size: 1.75rem;
  font-weight: 700;
  color: #242424;
}

.bricks-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 2rem;
  padding-top: 1rem;
}

.state-message {
  color: #888;
  text-align: center;
  padding: 4rem;
}
</style>