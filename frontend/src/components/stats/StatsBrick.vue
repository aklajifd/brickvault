<template>
  <div class="brick-wrapper">
    <div class="brick" :style="{ '--brick-color': color, '--brick-dark': darkColor }">
      <div class="studs-row">
        <div class="stud" v-for="n in studs" :key="n" />
      </div>
      <div class="brick-face">
        <div class="brick-icon">{{ icon }}</div>
        <div class="brick-value">{{ formattedValue }}</div>
        <div class="brick-label">{{ label }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  label: {
    type: String,
    required: true,
  },
  value: {
    type: [Number, String],
    required: true,
  },
  icon: {
    type: String,
    default: '🧱',
  },
  color: {
    type: String,
    default: '#f59e0b',
  },
  darkColor: {
    type: String,
    default: '#d97706',
  },
  studs: {
    type: Number,
    default: 4,
  },
  format: {
    type: String,
    default: 'number',
  },
})

const formattedValue = computed(() => {
  if (props.format === 'decimal') {
    return Number(props.value).toLocaleString(undefined, {
      minimumFractionDigits: 1,
      maximumFractionDigits: 1,
    })
  }
  return Number(props.value).toLocaleString()
})
</script>

<style scoped>
.brick-wrapper {
  perspective: 600px;
}

.brick {
  position: relative;
  background: var(--brick-color);
  border-radius: 6px;
  padding-top: 28px;
  cursor: default;
  transform: rotateX(4deg);
  transition: transform 0.2s;
  box-shadow:
    0 6px 0 var(--brick-dark),
    0 8px 6px rgba(0,0,0,0.2);
}

.brick:hover {
  transform: rotateX(2deg) translateY(-4px);
  box-shadow:
    0 10px 0 var(--brick-dark),
    0 14px 10px rgba(0,0,0,0.2);
}

.studs-row {
  position: absolute;
  top: -12px;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  gap: 10px;
}

.stud {
  width: 22px;
  height: 22px;
  background: var(--brick-color);
  border-radius: 50%;
  border: 2px solid var(--brick-dark);
  box-shadow:
    0 -3px 0 var(--brick-dark),
    inset 0 2px 4px rgba(255,255,255,0.3);
}

.brick-face {
  background: rgba(255, 255, 255, 0.08);
  border-radius: 0 0 6px 6px;
  padding: 1.25rem 1rem 1.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.4rem;
}

.brick-icon {
  font-size: 1.75rem;
  line-height: 1;
}

.brick-value {
  font-size: 2rem;
  font-weight: 700;
  color: white;
  line-height: 1;
  text-shadow: 0 1px 2px rgba(0,0,0,0.2);
}

.brick-label {
  font-size: 0.8rem;
  color: rgba(255, 255, 255, 0.85);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: 500;
}
</style>