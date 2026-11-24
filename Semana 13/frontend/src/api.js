import axios from 'axios'

// La instancia central comparte la dirección y el tiempo límite de la API.
const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',
  timeout: 10000,
})

export default api
