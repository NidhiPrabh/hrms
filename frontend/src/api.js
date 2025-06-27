import axios from 'axios'

export const api = axios.create({
  baseURL: 'http://localhost:8000/api/v1'
})

export function authHeader() {
  const token = localStorage.getItem('token')
  return token ? { Authorization: `Bearer ${token}` } : {}
}
