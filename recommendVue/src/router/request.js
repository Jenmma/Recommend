import axios from 'axios'

export function get(config) {

    const instance = axios.create({
        method: 'get',
        baseURL: 'http://localhost:8000/',
        timeout: 100000,
        headers: { 'Content-Type': 'application/x-www-form-urlencoded', }
    })
    console.log("我请求了一个数据")
    console.log(instance((config)))
    return instance(config)
}

export function post(config) {

    const instance = axios.create({
        method: 'post',
        baseURL: 'http://localhost:8000/',
        timeout: 100000,
        headers: { 'Content-Type': 'application/x-www-form-urlencoded', }
    })

    return instance(config)
}
export function get1(config) {

    const instance = axios.create({
        method: 'get',
        baseURL: 'http://localhost:8000/',
        timeout: 100000,
        headers: { 'Content-Type': 'application/x-www-form-urlencoded', }
    })

    return instance(config)
}