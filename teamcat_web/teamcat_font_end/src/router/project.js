
// import EnvServiceWebpart from '../components/APIMockWebpart.vue'
import ProjectHead from '../views/project/Head.vue'
import PortalHead from '../views/project/PortalHead.vue'
// import EmptyHead from '../components/layout/EmptyBodyHead.vue'

const projectRouter = [
  {
    name: 'projectRoot',
    path: '/project',
    components: {
      default: function () {
        return import('../views/project/ProjectList.vue')
      },
      bodyhead: PortalHead
    },
    meta: ''
  },
  {
    name: 'projectTask',
    path: '/project/:projectID/task',
    components: {
      default: function () {
        return import('../views/project/projecttask/ProjectTask.vue')
      },
      bodyhead: ProjectHead
    },
    props: {default: true,bodyhead: true},
    meta: ''
  },
  {
    name: 'projectFortesting',
    path: '/project/:projectID/fortesting',
    components: {
      default: function () {
        return import('../views/project/project-fortesting/ProjectFortesting.vue')
      },
      bodyhead: ProjectHead
    },
    props: {default: true,bodyhead: true},
    meta: ''
  },


  {
    name: 'projectFortestingReport',
    path: '/project/:projectID/fortesting/:fortestingID/report/:reportName',
    components: {
      default: function () {
        return import('../views/project/project-fortesting/report/Report.vue')
      },
      bodyhead: ProjectHead
    },
    props: {default: true,bodyhead: true},
    meta: ''
  }
]

export {
  projectRouter
}
