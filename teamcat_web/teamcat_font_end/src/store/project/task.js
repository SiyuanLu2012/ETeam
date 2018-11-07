import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  taskChange: false
}
const getters = {
  taskChange (state) {
    return state.taskChange
  }

}
const mutations = {

  setTaskChange (state, isChange) {
    state.taskChange = isChange
  }
}
const actions = {
  setTaskChangeAction (context, isChanged) {
    context.commit('setTaskChange', isChanged)
  }
}
const modules = {}

export default {
  namespaced: true,
  actions,
  getters,
  state,
  mutations,
  modules
}
