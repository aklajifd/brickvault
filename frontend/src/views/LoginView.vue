<template>
    <div class="auth-wrapper">
        <div class="auth-card">
            <div class="auth-logo">🧱</div>
            <h1>BrickVault</h1>
            <p class="auth-subtitle">{{  isSignUp ? 'Create your account' : 'Welcome back' }}</p>

            <div class="auth-form">
                <input
                    v-model="email"
                    type="email"
                    placeholder="Email address"
                    class="auth-input"
                />
                <input
                    v-model="password"
                    type="password"
                    placeholder="Password"
                    class="auth-input"
                />
                <p class="error-msg" v-if="error">{{  error }}</p>
                <p class="success-msg" v-if="successMsg">{{ successMsg }}</p>
                <button
                    class="auth-btn"
                    @click="handleSubmit"
                    :disabled="loading"
                >
                    {{ loading ? 'Please wait...' : isSignUp ? 'Sign Up' : 'Sign In' }}
                </button>
            </div>

            <p class="auth-toggle">
                {{ isSignUp ? 'Already have an account?' : "Don't have an account?" }}
                <span @click="toggleMode">{{ isSignUp ? 'Sign in' : 'Sign up' }}</span>
            </p>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const router = useRouter()
const authStore = useAuthStore()

const email = ref('')
const password = ref('')
const loading = ref(false)
const error = ref(null)
const successMsg = ref(null)
const isSignUp = ref(false)

function toggleMode() {
    isSignUp.value = !isSignUp.value
    error.value = null
    successMsg.value = null
}

async function handleSubmit() {
    loading.value = true
    error.value = null
    successMsg.value = null
    try {
        if (isSignUp.value) {
            await authStore.signUp(email.value, password.value)
            successMsg.value = 'Account created! Please check your email to confirm your account, then sign in.'
        } else {
            await authStore.signIn(email.value, password.value)
            router.push('/collection')
        }
    } catch (err) {
        error.value = err.message || 'Something went wrong. Please try again.'
    } finally {
        loading.value = false
    }
}
</script>

<style scoped>
.auth-wrapper {
    min-height: 80vh;
    display: flex;
    align-items: center;
    justify-content: center;
}

.auth-card {
    background: white;
    border-radius: 16px;
    padding: 2.5rem;
    width: 100%;
    max-width: 400px;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.08);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
}

.auth-logo {
    font-size: 3rem;
}

.auth-card h1 {
    font-size: 1.75rem;
    font-weight: 700;
    color: #242424;
}

.auth-subtitle {
    color: #888;
    font-size: 0.95rem;
}

.auth-form {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    margin-top: 0.5rem;
}

.auth-input {
    width: 100%;
    padding: 0.75rem 1rem;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 1rem;
    outline: none;
    transition: border-color 0.2s;
}

.auth-input:focus {
    border-color: #f59e0b;
}

.auth-btn {
    width: 100%;
    padding: 0.75rem;
    background: #f59e0b;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 500;
    cursor: pointer;
    margin-top: 0.25rem;
    transition: background 0.2s;
}

.auth-btn:hover:not(:disabled) {
    background: #d97706;
}

.auth-btn:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}

.error-msg {
    color: #dc2626;
    font-size: 0.875rem;
}

.success-msg {
    color: #16a34a;
    font-size: 0.875rem;
}

.auth-toggle {
    font-size: 0.875rem;
    color: #888;
}

.auth-toggle span {
    color: #f59e0b;
    cursor: pointer;
    font-weight: 500;
}

.auth-toggle span:hover {
    color: #d97706;
}
</style>