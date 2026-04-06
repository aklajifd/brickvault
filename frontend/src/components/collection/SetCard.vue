<template>
  <div class="set-card">
    <img
      v-if="set.lego_set.image_url"
      :src="set.lego_set.image_url"
      :alt="set.lego_set.name"
      class="set-image"
    />
    <div v-else class="set-image-placeholder">🧱</div>
    <div class="set-info">
      <h3 class="set-name">{{ set.lego_set.name }}</h3>
      <p class="set-number"># {{ set.lego_set.set_number }}</p>
      <p class="set-theme" v-if="set.lego_set.theme_name">
        {{ set.lego_set.theme_name }}
      </p>
      <p class="set-pieces" v-if="set.lego_set.piece_count">
        {{ set.lego_set.piece_count.toLocaleString() }} pieces
      </p>
    </div>
    <button class="remove-btn" @click="$emit('remove', set.id)">Remove</button>
  </div>
</template>

<script setup>
defineProps({
  set: {
    type: Object,
    required: true,
  },
});

defineEmits(["remove"]);
</script>

<style scoped>
.set-card {
  background: white;
  border-radius: 12px;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transition: transform 0.2s;
}

.set-card:hover {
  transform: translateY(-4px);
}

.set-image {
  width: 100%;
  height: 160px;
  object-fit: contain;
  border-radius: 8px;
  background: #f9f9f9;
}

.set-image-placeholder {
  width: 100%;
  height: 160px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
  background: #f9f9f9;
  border-radius: 8px;
}

.set-name {
  font-size: 1rem;
  font-weight: 600;
  color: #242424;
}

.set-number {
  font-size: 0.85rem;
  color: #888;
}

.set-theme {
  font-size: 0.85rem;
  color: #f59e0b;
  font-weight: 500;
}

.set-pieces {
  font-size: 0.9rem;
  color: #555;
}

.remove-btn {
  margin-top: auto;
  padding: 0.4rem 0.8rem;
  background: #fee2e2;
  color: #dc2626;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.85rem;
}

.remove-btn:hover {
  background: #fecaca;
}
</style>