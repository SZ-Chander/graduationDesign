/*
 * @Description: file content
 * @Author: HaoYang Zuo
 * @Date: 2023-01-17 12:59:49
 * @LastEditors: HaoYang Zuo
 * @LastEditTime: 2023-01-20 18:52:46
 */
import axios from 'axios'
import { useStore } from 'vuex'

// 创建vuex实例
const store = useStore()

export function request(config){
    // 1.创建axios的实例
    const instance = axios.create({
        // baseURL: '/api',
        timeout: 5000
    })

    // 2.axios的拦截器
    // 2.1.请求拦截的作用 
        // 1.比如config中的一些不符合服务器的要求
        // 2.比如每次发送网络请求时，都希望在界面中显示一个请求的图标
        // 3.某些网络请求（比如登录），必须携带一些特殊的信息
    
    instance.interceptors.request.use(config => {
        if (store.state.token) {  // 判断是否存在token，如果存在的话，则每个http header都加上token
            config.headers['Auth-Token'] = `${store.state.token}`;
        }
        return config
    },err =>{
        // console.log(err);
    })

    // 2.2.响应拦截
    instance.interceptors.response.use(res =>{
        return res.data
    },err => {
        console.log(err);
    })

    return instance(config)
}
