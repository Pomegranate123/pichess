import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/login.vue')
  },
  {
    path: '/aanmelden',
    name: 'aanmelden',
    component: () => import('@/views/aanmelden.vue')
  },
  {
    path: '/game',
    name: 'game',
    component: () => import('@/views/game.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
