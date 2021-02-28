import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        user: {}
    },
    mutations: {
        setLoggedInUser(state, user) {
            state.user = user
        }
    },
    actions: {
    },
    modules: {
    }
})
