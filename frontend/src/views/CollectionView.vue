<template>
  <div class="collection-view">
    <div class="collection-header">
      <div class="header-text">
        <h1>My Collection</h1>
        <p class="subtitle" v-if="store.stats">
          {{ store.stats.total_sets }} sets · {{ store.stats.total_pieces.toLocaleString() }} total pieces
        </p>
      </div>
      <button class="add-btn" @click="showModal = true">
        + Add Set
      </button>
    </div>

    <div class="filter-bar" v-if="store.collection.length > 0">
      <input
        v-model="search"
        placeholder="Search your collection..."
        class="search-input"
      />
    </div>

    <SetGrid
      :sets="filteredCollection"
      :loading="store.loading"
      @remove="handleRemove"
    />

    <AddSetModal
      v-if="showModal"
      @close="showModal = false"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useCollectionStore } from '../stores/collection'
import SetGrid from '../components/collection/SetGrid.vue'
import AddSetModal from '../components/collection/AddSetModal.vue'

const store = useCollectionStore()
const showModal = ref(false)
const search = ref('')

const filteredCollection = computed(() => {
  if (!search.value.trim()) return store.collection
  const query = search.value.toLowerCase()
  return store.collection.filter(entry =>
    entry.lego_set.name.toLowerCase().includes(query) ||
    entry.lego_set.set_number.includes(query) ||
    entry.lego_set.theme_name?.toLowerCase().includes(query)
  )
})

onMounted(async () => {
  await store.loadCollection()
  await store.loadStats()
})

async function handleRemove(entryId) {
  await store.removeSet(entryId)
}
</script>

<style scoped>
.collection-view {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.collection-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.header-text h1 {
  font-size: 1.75rem;
  font-weight: 700;
  color: #242424;
}

.subtitle {
  font-size: 0.95rem;
  color: #888;
  margin-top: 0.25rem;
}

.add-btn {
  padding: 0.6rem 1.4rem;
  background: #f59e0b;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
}

.add-btn:hover {
  background: #d97706;
}

.filter-bar {
  display: flex;
  gap: 1rem;
}

.search-input {
  flex: 1;
  max-width: 400px;
  padding: 0.6rem 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 0.95rem;
  outline: none;
}

.search-input:focus {
  border-color: #f59e0b;
}
</style>