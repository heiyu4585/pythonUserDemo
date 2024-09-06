<template>

<div class="p-3">
  <!-- Modal toggle -->
  <button @click="handleOpen" data-modal-target="default-modal" data-modal-toggle="default-modal" class="block text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 m-2" type="button">
    add user
  </button>
  <div class="relative overflow-x-auto mb-2.5">
    <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
      <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
      <tr >
        <th scope="col" class="px-6 py-3">
          id
        </th>
        <th scope="col" class="px-6 py-3">
          name
        </th>
        <th scope="col" class="px-6 py-3">
          gender
        </th>
        <th scope="col" class="px-6 py-3">
          edit
        </th>
      </tr>
      </thead>
      <tbody>
      <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700" v-for="(item, index) in userList" :key="item.id">
        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
          {{item.id}}
        </th>
        <td class="px-6 py-4">
          {{item.name}}
        </td>
        <td class="px-6 py-4">
          {{item.gender}}
        </td>
        <td class="px-6 py-4">
          <button type="button" @click="()=>{handleOpen(item)}" class="py-2.5 px-5 me-2 mb-2 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">edit</button>
        </td>
      </tr>
      </tbody>
    </table>
  </div>

  <nav aria-label="Page navigation example">
    <ul class="flex items-center -space-x-px h-8 text-sm">
      <li @click="handlePre">
        <a href="#" class="flex items-center justify-center px-3 h-8 ms-0 leading-tight text-gray-500 bg-white border border-e-0 border-gray-300 rounded-s-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
          <span class="sr-only">Previous</span>
          <svg class="w-2.5 h-2.5 rtl:rotate-180" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 1 1 5l4 4"/>
          </svg>
        </a>
      </li>
      <template v-for="page in pageTotal" :key="page">
        <li @click="()=>pageChange(page)" v-if="(pageIndex<5 && page<=10) ||( page >= pageIndex-5 && page<= pageIndex+5 )">
          <a href="#"  :class="page === pageIndex?'bg-blue-200 hover:bg-blue-100':''" class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">{{page}}</a>
        </li>
      </template>


      <li @click="handleNext">
        <a href="#" class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 rounded-e-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
          <span class="sr-only">Next</span>
          <svg class="w-2.5 h-2.5 rtl:rotate-180" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 9 4-4-4-4"/>
          </svg>
        </a>
      </li>
    </ul>
  </nav>

  <!-- Main modal -->
  <div id="default-modal" tabindex="-1"  class=" overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full" :class="isOpen?'':'hidden'">
    <div class="relative p-4 w-full max-w-2xl max-h-full my-0 mx-auto mt-12">
      <!-- Modal content -->
      <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
        <!-- Modal header -->
        <div class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600">
          <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
            {{!!curUser.id ? "edit user": "add user"}}
          </h3>
          <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-hide="default-modal">
            <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
            </svg>
            <span class="sr-only">Close modal</span>
          </button>
        </div>
        <!-- Modal body -->
        <div class="p-4 md:p-5 space-y-4">
          <form>
            <div class="grid gap-6 mb-6 md:grid-cols-2">
              <div>
                <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">name</label>
                <input type="text" :value="curUser.name" @input="event => curUser.name = event.target.value"  id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="" required />
              </div>
            </div>
            <label for="gender" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Select an option</label>
            <select id="gender" v-model="curUser.gender" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
              <option selected>Choose a gender</option>
              <option value="male">male</option>
              <option value="female">female</option>
            </select>
          </form>
        </div>
        <!-- Modal footer -->
        <div class="flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600">
          <button @click="isOpen=false" data-modal-hide="default-modal" type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">cancel</button>
          <button @click="handleOk" data-modal-hide="default-modal" type="button" class="py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">ok</button>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<style scoped>

</style>

<script setup>
import {ref,reactive,onMounted} from 'vue';
import {get_user_list,add_user,edit_user} from '../api.js'
const isOpen = ref(false)

// 用户列表
const userList = ref([])
// 当前页
let pageIndex = ref(1)
// 每页的数量
const pageSize = 1;
// 总页数
let pageTotal = 0;

// 当前编辑的用户
const curUser = reactive({
  id:"",
  name:"",
  gender:""
})

const handleOpen = (detail)=>{
  if(detail){
    curUser.id = detail.id;
    curUser.name = detail.name;
    curUser.gender = detail.gender;
  }else{
    curUser.id=""
    curUser.name = "";
    curUser.gender = "";
  }
  isOpen.value = true
}

const handleOk = async ()=>{
  isOpen.value = false;
  if(!curUser.name ){
    return alert("Please enter name")
  }
  if(curUser.id){
    await edit_user(curUser)
  }else{
    await add_user(curUser)
  }
  await getList(pageIndex,pageSize)
}

const getList = async (pageIndex,pageSize)=>{
  const res = await get_user_list({pageIndex:pageIndex.value,pageSize})
  userList.value = res.data;
  pageTotal = Math.ceil(res.total/pageSize);
}

const pageChange = async(targetPage)=>{
  pageIndex.value = targetPage
  await getList(pageIndex,pageSize)
}

const handlePre = ()=>{
  if(pageIndex.value=== 1) return;
  pageIndex.value--;
  getList(pageIndex,pageSize)
}

const handleNext = ()=>{
  if(pageIndex.value === pageTotal) return;
  pageIndex.value++;
  getList(pageIndex,pageSize)
}

onMounted(() => {
  getList(pageIndex,pageSize)
})
</script>