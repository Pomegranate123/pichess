import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'menu',
    component: () => import('@/App.vue'),
    children: [
      {
        path: '/play',
        name: 'play',
        component: () => import('@/views/play.vue')
      },
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
        path: '/game/:white/:black/:time/:inc',
        name: 'game',
        component: () => import('@/views/game.vue')
      },
      {
        path: '/profile',
        name: 'profile',
        component: () => import('@/views/profile.vue')
      },
      {
        path: '/help',
        name: 'help',
        component: () => import('@/views/help.vue')
      },
    ],
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
