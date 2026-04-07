<template>
  <div class="set-grid-wrapper">
    <div v-if="loading" class="state-message">
      Loading your collection...
    </div>
    <div v-else-if="sets.length === 0" class="state-message">
      <p>No sets yet!</p>
      <p class="hint">Add your first set using the button above.</p>
    </div>
    <div v-else class="set-grid">
      <SetCard
        v-for="entry in sets"
        :key="entry.id"
        :set="entry"
        @remove="emit('remove', $event)"
      />
    </div>
  </div>
</template>

<script setup>
import SetCard from './SetCard.vue'

defineProps({
  sets: {
    type: Array,
    required: true,
  },
  loading: {
    type: Boolean,
    default: false,
  },
})

const emit = defineEmits(['remove'])
</script>

<style scoped>
.set-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 1.5rem;
}

.state-message {
  text-align: center;
  padding: 4rem 2rem;
  color: #888;
  font-size: 1.1rem;
}

.hint {
  font-size: 0.9rem;
  margin-top: 0.5rem;
}
</style>