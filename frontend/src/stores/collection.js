import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import {
    fetchCollection,
    fetchCollectionStats,
    fetchWishList,
    addToCollection,
    removeFromCollection,
    lookupSet
} from '../services/api'

export const useCollectionStore = defineStore('collection', () => {
    const collection = ref([])
    const wishlist = ref([])
    const stats = ref(null)
    const loading = ref(false)
    const error = ref(null)

    const totalSets = computed(() => collection.value.length)
    const ownedSets = computed(() => collection.value.filter(e => !e.is_wishlist))

    async function loadCollection() {
        loading.value = true
        error.value = null
        try {
            const response = await fetchCollection()
            collection.value = response.data
        } catch (err) {
            error.value = 'Failed to load collection'
        } finally {
            loading.value = false
        }
    }

    async function loadStats() {
        try {
            const response = await fetchCollectionStats()
            stats.value = response.data
        } catch (err) {
            error.value = 'Failed to load stats'
        }
    }

    async function loadWishlist() {
        try {
            const response = fetchWishList()
            wishlist.value = response.data
        } catch (err) {
            error.value = 'Failed to load wishlist'
        }
    }

    async function addSet(setNumber) {
        loading.value = true
        error.value = null
        try {
            const lookupResponse = await lookupSet(setNumber)
            const legoSet = lookupResponse.data
            await addToCollection({ lego_set_id: legoSet.id, is_wishlist: false, quantity: 1 })
            await loadCollection()
            await loadStats()
        } catch (err) {
            error.value = 'Failed to add set'
        } finally {
            loading.value = false
        }
    }

    async function removeSet(entryId) {
        try {
            await removeFromCollection(entryId)
            await loadCollection()
            await loadStats()
        } catch (err) {
            error.value = 'Failed to remove set'
        }
    }

    return {
        collection, wishlist, stats, loading, error,
        totalSets, ownedSets,
        loadCollection, loadStats, loadWishlist, addSet, removeSet,
    }
})