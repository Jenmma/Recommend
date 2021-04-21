import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [{
        path: '/',
        name: 'Default',
        redirect: '/home',
    },
    {
        path: '/home',
        name: 'Home',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import ('../views/Home.vue'),
        children: [{
                path: '/',
                name: 'MenuDefault',
                redirect: 'menu1',
            },
            {
                path: 'menu1',
                component: () =>
                    import ('../views/Menu1Demo.vue'),
            },
            {
                path: 'menu2',
                component: () =>
                    import ('../views/About.vue'),
            }
        ]
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router