/*
 * @Description: file content
 * @Author: HaoYang Zuo
 * @Date: 2023-01-17 09:56:52
 * @LastEditors: HaoYang Zuo
 * @LastEditTime: 2023-01-20 12:21:07
 */
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,

  // scss配置
  pluginOptions: {
    'style-resources-loader': {
      preProcessor: 'scss',
      patterns: []
    }
  },

  //根目录配置 
  lintOnSave: false,
  publicPath: '',
  runtimeCompiler: true,
  configureWebpack:{
    resolve:{
      alias:{
        'assets':'@/assets',
        'common':'@/common',
        'components':'@/components',
        'network':'@/network',
        'api':'@/api',
        'views':'@/views',
      }
    }
  },

  // 跨域
  devServer: {
    proxy:{
      '/api':{
        target:`http://127.0.0.1:5000/api`,
        changeOrigin:true,
        ws:true,
        secure:true,
        // pathRewrite:{
        //   '^/api': ''
        // }
      },
    }  
  },
})
