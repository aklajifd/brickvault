<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal">
      <div class="modal-header">
        <h2>Add a Set</h2>
        <button class="close-btn" @click="$emit('close')">✕</button>
      </div>
      <div class="modal-body">
        <p class="modal-hint">Enter a LEGO set number to automatically fetch its details from Rebrickable.</p>
        <div class="input-row">
          <input
            v-model="setNumber"
            placeholder="e.g. 75192"
            class="set-input"
            @keyup.enter="handleAdd"
          />
          <button
            class="add-btn"
            @click="handleAdd"
            :disabled="loading || !setNumber.trim()"
          >
            {{ loading ? 'Adding...' : 'Add Set' }}
          </button>
        </div>
        <p class="error-msg" v-if="error">{{ error }}</p>
        <p class="success-msg" v-if="success">Set added successfully!</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCollectionStore } from '../../stores/collection'

const store = useCollectionStore()
const setNumber = ref('')
const loading = ref(false)
const error = ref(null)
const success = ref(false)

const emit = defineEmits(['close'])

async function handleAdd() {
  if (!setNumber.value.trim()) return
  loading.value = true
  error.value = null
  success.value = false
  try {
    await store.addSet(setNumber.value.trim())
    success.value = true
    setNumber.value = ''
    setTimeout(() => emit('close'), 1000)
  } catch (err) {
    error.value = 'Could not find that set number. Please try again.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  width: 100%;
  max-width: 480px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.modal-header h2 {
  font-size: 1.25rem;
  font-weight: 600;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.2rem;
  cursor: pointer;
  color: #888;
}

.close-btn:hover {
  color: #242424;
}

.modal-hint {
  font-size: 0.9rem;
  color: #888;
  margin-bottom: 1rem;
}

.input-row {
  display: flex;
  gap: 0.75rem;
}

.set-input {
  flex: 1;
  padding: 0.6rem 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 1rem;
  outline: none;
}

.set-input:focus {
  border-color: #f59e0b;
}

.add-btn {
  padding: 0.6rem 1.2rem;
  background: #f59e0b;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
  font-weight: 500;
}

.add-btn:hover:not(:disabled) {
  background: #d97706;
}

.add-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.error-msg {
  margin-top: 0.75rem;
  color: #dc2626;
  font-size: 0.9rem;
}

.success-msg {
  margin-top: 0.75rem;
  color: #16a34a;
  font-size: 0.9rem;
}
</style>