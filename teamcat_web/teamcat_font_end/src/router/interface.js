

const apiRouter = [
  {
    name: 'envRoot',
    path: '/interface/mock',
    components: {
      default: function () {
        return import('../views/interface/mock/APIMockWebpart.vue')
      },
      bodyhead: function () {
        return import('../views/interface/Head.vue')
      }
    },
    meta: ''
  },
  { path: '/interface', redirect: '/interface/mock' }
]

export {
  apiRouter
}
