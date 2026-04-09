import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { supabase } from '../services/supabase'

export const useAuthStore = defineStore('auth', () => {
    const user = ref(null)
    const session = ref(null)
    const loading = ref(true)

    const isAuthenticated = computed(() => !!user.value)
    const accessToken = computed(() => session.value?.access_token ?? null)

    async function initialize() {
        const { data } = await supabase.auth.getSession()
        session.value = data.session
        user.value = data.session?.user ?? null
        loading.value = false

        supabase.auth.onAuthStateChange((_event, newSession) => {
            session.value = newSession
            user.value = newSession?.user ?? null
        })
    }

    async function signUp(email, password) {
        const { data, error } = await supabase.auth.signUp({ email, password })
        if (error) throw error
        return data
    }

    async function signIn(email, password) {
        const { data, error } = await supabase.auth.signInWithPassword({
            email,
            password,
        })
        if (error) throw error
        session.value = data.session
        user.value = data.user
        return data
    }

    async function signOut() {
        await supabase.auth.signOut()
        user.value = null
        session.value = null
    }

    return {
        user, session, loading, isAuthenticated, accessToken,
        initialize, signUp, signIn, signOut
    }
})