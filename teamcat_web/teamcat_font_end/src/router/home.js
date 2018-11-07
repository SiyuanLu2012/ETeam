
const homeRouter = [
  {
    name: 'homeRoot',
    path: '/home/summary',
    components: {
      default: function () {
        return import('../views/home/HomeSummary.vue')
      },
      bodyhead: function () {
        return import('../views/home/Head.vue')
      }
    },
    meta: ''
  },
  {
    name: 'homeTask',
    path: '/home/my/task',
    components: {
      default: function () {
        return import('../views/project/projecttask/ProjectTask.vue')
      },
      bodyhead: function () {
        return import('../views/home/Head.vue')
      }
    },
    props: {bodyhead: true, default: true},
    meta: ''
  },

  {
    name: 'homeFortesting',
    path: '/home/my/fortesting',
    components: {
      default: function () {
        return import('../views/project/project-fortesting/ProjectFortesting.vue')
      },
      bodyhead: function () {
        return import('../views/home/Head.vue')
      }
    },
    props: {bodyhead: true, default: true},
    meta: ''
  },

  { path: '/', redirect: '/home/summary' },
  { path: '/home', redirect: '/home/summary' },
  { path: '/home/task/all', redirect: '/home/my/task' },
  { path: '/home/task/', redirect: '/home/my/task' }
]

export {
  homeRouter
}
