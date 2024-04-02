/*
 * @Description: file content
 * @Author: HaoYang Zuo
 * @Date: 2023-01-17 13:59:33
 * @LastEditors: HaoYang Zuo
 * @LastEditTime: 2023-04-15 01:18:47
 */
import { request } from '@/network'

// 主页面
export function mains(departId) {
  return request({
    url: ' /api/vitalTask',
    method: 'post',
    data:{
        departId
    }
  })
}

// 查询执行记录单
export function execute(departId) {
  return request({
    url: ' /api/checkExecute',
    method: 'post',
    data:{
        departId
    }
  })
}