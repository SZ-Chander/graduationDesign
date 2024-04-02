<!--
 * @Description: file content
 * @Author: HaoYang Zuo
 * @Date: 2023-01-17 09:56:52
 * @LastEditors: HaoYang Zuo
 * @LastEditTime: 2023-01-17 11:32:50
-->
<template>
  <div id="app">
    <router-view v-slot="{ Component }">
      <keep-alive include="Home">
        <component :is="Component" v-if="$route.meta.keepAlive" />
      </keep-alive>
      <component :is="Component" v-if="!$route.meta.keepAlive" />
    </router-view>
  </div>
</template>

<script setup>
  import Home from '@/views/home.vue'
</script>
<script>
export default {
  name: 'App',
}
</script>

<style>
#app {
}
</style>
