/*
 * @Description: file content
 * @Author: HaoYang Zuo
 * @Date: 2023-01-17 13:59:33
 * @LastEditors: HaoYang Zuo
 * @LastEditTime: 2023-04-15 01:18:47
 */
import { request } from '@/network'

// 登录
export function logins(id,password) {
  return request({
    url: '/api/login',
    method: 'post',
    data:{
        id,
        password
    }
  })
}

