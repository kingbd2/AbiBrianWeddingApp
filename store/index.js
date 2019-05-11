import Vuex from 'vuex'

import session from './api/session';

const createStore = () => {
  return new Vuex.Store({
    state: () => ({
      uuid: [],
    }),
    mutations: {
      SET_POSTS ( state, data ) {
        state.posts = data;
      },
    },
    actions: {
      // Get all guests
      async GET_GUESTS({
        commit
      }) {
        const {
          data
        } = await session.get('/posts/')
        commit('SET_POSTS', data)
      },
      async GET_SAMPLE({
        commit
      }) {
        const {
          data
        } = await session.get('/sample/')
        commit('SET_SAMPLE', data)
      },
    }
  })
}

export default createStore