import { defineStore } from 'pinia'
import { ref } from 'vue'
import { fetchThemes, fetchSetsByTheme } from '../services/api'

export const useStatsStore = defineStore('stats', () => {
    const themes = ref([])
    const setsByTheme = ref({})
    const loading = ref(false)
    const error = ref(null)

    async function loadThemes() {
        loading.value = true
        try {
            const response = await fetchThemes()
            themes.value = response.data
        } catch (err) {
            error.value = 'Failed to load themes'
        } finally {
            loading.value = false
        }
    }

    async function loadSetsByTheme(themeId) {
        try {
            const response = await fetchSetsByTheme(themeId)
            setsByTheme.value[themeId] = response.data
        } catch (err) {
            error.value = 'Failed to load sets for theme'
        }
    }

    return {
        themes, setsByTheme, loading, error,
        loadThemes, loadSetsByTheme
    }
})