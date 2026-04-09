import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import HomeView from '../views/HomeView.vue'
import CollectionView from '../views/CollectionView.vue'
import ThemesView from '../views/ThemesView.vue'
import StatsView from '../views/StatsView.vue'
import LoginView from '../views/LoginView.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: HomeView },
        { path: '/login', component: LoginView },
        {
            path: '/collection', 
            component: CollectionView,
            meta: { requiresAuth: true }
        },
        {
            path: '/themes',
            component: ThemesView,
            meta: { requiresAuth: true }
        },
        {
            path: '/stats',
            component: StatsView,
            meta: { requiresAuth: true }
        },
    ]
})

router.beforeEach(async (to) => {
    const authStore = useAuthStore()
    if (to.meta.requiresAuth && !authStore.isAuthenticated) {
        return '/login'
    }
})

export default router
