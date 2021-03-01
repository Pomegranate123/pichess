import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/game',
    name: 'start',
    component: () => import('@/views/game.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
