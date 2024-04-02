/*
 * @Description: file content
 * @Author: HaoYang Zuo
 * @Date: 2023-01-17 10:52:00
 * @LastEditors: HaoYang Zuo
 * @LastEditTime: 2023-04-15 01:55:56
 */
import { ElMessage } from 'element-plus'
import {createRouter, createWebHashHistory} from "vue-router"

const Home = () => import ('views/home.vue')
const Main = () => import ('views/main/Main.vue')
const Execute = () => import('views/main/components/execute.vue')

const routes =[
  {
    path:'',
    redirect:'/Home'
  },
  {
    path:'/Home',
    name:'Home',
    meta:{
      keepAlive:true
    },
    component:Home
  },
  {
    path:'/Main',
    name:'Main',
    meta:{
      keepAlive:true
    },
    component:Main,
    children:[
      // {
      //   path:'/execute',
      //   name:'execute',
      //   meta:{
      //     keepAlive:true
      //   },
      //   component:Execute
      // },
      
    ]
  },
  {
    path:'/execute',
    name:'execute',
    meta:{
      keepAlive:true
    },
    component:Execute
  },
]

// 创建router
const router = createRouter({
  routes,
  // mode:'history',
  history: createWebHashHistory(),
  base: process.env.BASE_URL
})

export default router