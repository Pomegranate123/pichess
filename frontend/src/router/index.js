import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/login.vue')
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import('@/views/signup.vue')
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
