<template>
  <div class="theme-chart">
    <h3 class="chart-title">Sets by theme</h3>
    <div v-if="!data || data.length === 0" class="empty">
      No theme data yet.
    </div>
    <div v-else class="chart-body">
      <div
        v-for="(item, index) in data"
        :key="item.theme"
        class="chart-row"
      >
        <div class="row-label">{{ item.theme }}</div>
        <div class="bar-track">
          <div
            class="bar-fill"
            :style="{
              width: barWidth(item.count) + '%',
              background: colors[index % colors.length]
            }"
          />
        </div>
        <div class="row-count">{{ item.count }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  data: {
    type: Array,
    required: true,
  },
})

const colors = [
  '#f59e0b',
  '#ef4444',
  '#3b82f6',
  '#10b981',
  '#8b5cf6',
  '#f97316',
  '#06b6d4',
  '#ec4899',
]

function barWidth(count) {
  const max = Math.max(...props.data.map(d => d.count))
  return max === 0 ? 0 : (count / max) * 100
}
</script>

<style scoped>
.theme-chart {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.chart-title {
  font-size: 1rem;
  font-weight: 600;
  color: #242424;
  margin-bottom: 1.25rem;
}

.chart-body {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.chart-row {
  display: grid;
  grid-template-columns: 120px 1fr 32px;
  align-items: center;
  gap: 0.75rem;
}

.row-label {
  font-size: 0.875rem;
  color: #555;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.bar-track {
  height: 20px;
  background: #f3f4f6;
  border-radius: 10px;
  overflow: hidden;
}

.bar-fill {
  height: 100%;
  border-radius: 10px;
  transition: width 0.6s ease;
}

.row-count {
  font-size: 0.875rem;
  font-weight: 600;
  color: #242424;
  text-align: right;
}

.empty {
  color: #888;
  text-align: center;
  padding: 2rem;
}
</style>