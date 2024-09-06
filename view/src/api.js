import axios from './axios.js'
export const get_user_list =async (params)=>{
    return  await axios({
        method: 'get',
        url: '/get_user_list',
        params
    });
}

export const add_user = async (data)=>{
    return await axios({
        method: 'post',
        url: '/add_user',
        data: data
    });
}

export const edit_user = async (data)=>{
    return await axios({
        method: 'post',
        url: '/edit_user',
        data: data
    });
}