import axios from 'axios'
import { useAuthStore } from '../stores/auth'

const api = axios.create({
    baseURL: 'http://localhost:8000',
    headers: {
        'Content-Type': 'application/json',
    }
})

api.interceptors.request.use((config) => {
    const authStore = useAuthStore()
    if (authStore.accessToken) {
        config.headers.Authorization = `Bearer ${authStore.accessToken}`
    }
    return config
})

// Sets
export const fetchSets = () => api.get('/sets/')
export const fetchSetById = (id) => api.get(`/sets/${id}`)
export const lookupSet = (setNumber) => api.post(`/sets/lookup/${setNumber}`)

// Themes
export const fetchThemes = () => api.get('/themes/')
export const getThemeByid = (id) => api.get(`/themes/${id}`)
export const fetchSetsByTheme = (id) => api.get(`/themes/${id}/sets`)
export const createTheme = (data) => api.post('/themes/', data)

// Collection
export const fetchCollection = () => api.get('/collection/me')
export const fetchCollectionStats = () => api.get('/collection/me/stats')
export const fetchWishList = () => api.get('/collection/me/wishlist')
export const addToCollection = (data) => api.post('/collection/me', data)
export const removeFromCollection = (id) => api.delete(`/collection/me/${id}`)