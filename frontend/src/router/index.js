import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CollectionView from '../views/CollectionView.vue'
import ThemesView from '../views/ThemesView.vue'
import StatsView from '../views/StatsView.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: HomeView },
        { path: '/collection', component: CollectionView },
        { path: '/themes', component: ThemesView },
        { path: '/stats', component: StatsView }
    ]
})

export default router
