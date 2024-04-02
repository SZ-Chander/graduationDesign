/*
 * @Description: file content
 * @Author: HaoYang Zuo
 * @Date: 2023-01-17 09:56:52
 * @LastEditors: HaoYang Zuo
 * @LastEditTime: 2023-01-20 18:28:11
 */
import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import router from './router/index'
import store from './store/index'


const app = createApp(App)

app.use(ElementPlus)
app.use(router)
app.use(store)
app.mount('#app')
