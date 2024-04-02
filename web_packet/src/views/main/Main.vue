<!--
 * @Description: file content
 * @Author: HaoYang Zuo
 * @Date: 2023-01-19 22:51:36
 * @LastEditors: HaoYang Zuo
 * @LastEditTime: 2023-04-15 03:07:13
-->
<template>
  <div class="all">
    <!-- 总体盒子 -->
    <div class="content">
      <!-- 顶部导航栏 -->
      <div class="top">
        <!-- 参数为：默认页面、菜单展示模式（是否水平）、菜单激活回调 -->
        <el-menu
          :default-active="$route.path"
          class="el-menu-demo"
          mode="horizontal"
          @select="handleSelect"
          router
        >
          <template v-for="item in departId">
            <!-- <el-menu-item index="1">当前科室</el-menu-item> -->
            <el-sub-menu :index="item.index" v-if="item.child">
              <template #title>{{ item.name }}</template>
              <template v-for="item2 in item.child">
                <el-menu-item :index="item2.index">{{
                  item2.name
                }}</el-menu-item>
              </template>
            </el-sub-menu>

            <el-menu-item :index="item.index" disabled>{{
              item.name
            }}</el-menu-item>
            <el-menu-item index="execute">执行记录单</el-menu-item>
            <el-menu-item index="nursingPlan">护理计划单</el-menu-item>
            <el-menu-item index="nursingRecord">护理记录单</el-menu-item>
            <el-menu-item index="temperature">体温单</el-menu-item>
          </template>
        </el-menu>

        <!-- 床位一览 -->
        <div class="main">
          <div class="item" v-for="item in departBed">
            <div class="item-left">
              <div>{{ item.patient.bedNo }}</div>
              <div>{{ item.patient.patientAge }}</div>
              <div>{{ item.patient.patientName }}</div>
            </div>
            <div class="item-right">
              <img src="../../assets/灰床.png" alt="" />
            </div>
          </div>
        </div>
        <div>
          {{ departId }}
        </div>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue'
import { useRoute,useRouter } from 'vue-router'
import { useStore } from "vuex"
import { ElMessage } from 'element-plus'
import { mains } from '@/api/main'


const route = useRoute()
const router = useRouter()
const store = useStore()
// 表单数据
// const formRef = ref(null)
// const form = ref({
// 	privacy: 0
// })

// 科室id
const departId = ref([
  {
    id:"null",
    name:"当前科室",
    child:[
      {id:"001",name:"内科"},
      // {index:"002",name:"外科"},
      // {index:"003",name:"妇科"},
      // {index:"004",name:"儿科"},
    ]
  },
  // {
  //   index:"execute",
  //   name:'执行记录单'
  // },
  // {
  //   index:"nursingPlan",
  //   name:'护理计划单'
  // },
  // {
  //   index:"nursingRecord",
  //   name:'护理记录单'
  // },
  // {
  //   index:"temperature",
  //   name:'体温单'
  // }
])
// 科室名字
const departName = ref()

// 员工
const staff = ref()

// 当前科室
const activeIndex  = ref("Main")

// 科室按钮回调
// index:选中菜单栏的index、 item: 选中菜单项
const handleSelect = (index,item) => {
  console.log(index);
  // departId.index = index
  // console.log(departId.index)
  console.log(item)
}

// 假设图
const departBed = ref([
  // {
  //   bedNo:"1",
  //   departid:"001",
  //   patient:{
  //     bedNo:"1",
  //     patientAge:"24岁",
  //     patientName:"李田所"
  //   }
  // },
  // {
  //   bedNo:"2",
  //   departid:"001",
  //   patient:{
  //     bedNo:"2",
  //     patientAge:"24岁",
  //     patientName:"李田所"
  //   }
  // },
  // {
  //   bedNo:"3",
  //   departid:"001",
  //   patient:{
  //     bedNo:"3",
  //     patientAge:"24岁",
  //     patientName:"李田所"
  //   }
  // }
]
)



// 主页信息
const form = ref(null)
// 接口
const main = () =>{
  store.state.departId = departId.value[0].id
  mains(departId.id).then((res) => {
    departBed.value = res.data.dict.departBed
    departName.value = res.data.dict.departName
    staff.value = res.data.dict.staff
  })
  console.log(departBed.value,departName.value,staff.value)
//   console.log(departId.value)
}
onMounted(() => {
  main()
  // this.activeIndex = this.$route.path.substring(1,this.$route.path.length); 
})



</script>

<script>
export default {
  name:'Main'
}
</script>

<style lang="scss" scoped>
.all {
  // background-color: aqua;
  display: flex;
  flex-direction: column;
  // justify-content: center;
  align-items: center;
  width: 100%;
  height: 45.5rem;

  .content {
    // background-color: red;
    width: 100%;
    height: 500px;

    .main {
      display: flex;
      align-items: center;
      justify-content: space-between;

      // background-color: blue;
      width: 100%;
      height: 300px;

      .item {
        display: flex;
        align-items: center;
        justify-content: space-between;
        // background-color: red;
        width: 10%;
        height: 100px;
        border: 0.5px solid black;
        border-radius: 5%;
        box-shadow: 2px 2px 2px 1px rgba(0, 0, 0, 0.2);

        .item-left {
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
          width: 50%;
          height: 100%;
        }
        .item-right {
          display: flex;
          align-items: center;
          justify-content: center;
          width: 50%;
          height: 100%;
          img {
            width: 75%;
            // height: 68%;
          }
        }
      }
    }
  }
}
</style>