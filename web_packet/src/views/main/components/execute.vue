<!--
 * @Description: file content
 * @Author: HaoYang Zuo
 * @Date: 2023-01-17 09:56:52
 * @LastEditors: HaoYang Zuo
 * @LastEditTime: 2023-04-15 03:08:27
-->
<template>
  <div class="all">1111111</div>
</template>


<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { ElMessage } from 'element-plus'
import { executes } from '@/api/main'


// 创建路由
const router = useRouter()
// 创建vuex实例
const store = useStore()

// 执行记录单数据
const executeList = ref()

// 表单数据
const formRef = ref(null)
const form = ref({
	privacy: 0
})

// 接口
const execute = () =>{
  
  executes(departId.index).then((res) => {
    executeList.value = res.data.dict.executeList
  })
  console.log(executeList.value)
}
onMounted(() => {
  execute()
  // this.activeIndex = this.$route.path.substring(1,this.$route.path.length); 
})


</script>
<script>
export default {
  name:'Execute'
}
</script>

<style lang="scss" scoped>
</style>