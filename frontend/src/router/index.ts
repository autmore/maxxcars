import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CatalogView from '../views/CatalogView.vue'
import OrdersView from '../views/OrdersView.vue'
import ReviewsView from '../views/ReviewsView.vue'
import AboutView from '../views/AboutView.vue'

export const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView,
            meta: {
                title: 'Главная страница'
            }
        },
        {
            path: '/catalog',
            name: 'catalog',
            component: CatalogView,
            meta: {
                title: 'Каталог'
            }
        },
        {
            path: '/orders',
            name: 'orders',
            component: OrdersView,
            meta: {
                title: 'Мои заказы'
            }
        },
        {
            path: '/reviews',
            name: 'reviews',
            component: ReviewsView,
            meta: {
                title: 'Отзывы'
            }
        },
        {
            path: '/about/:id',
            name: 'about',
            component: AboutView,
            meta: {
                title: 'Подробнее'
            }
        }
    ]
})

export const routes: RouteRecordRaw[] = []

export default router