import axios from 'axios'

export const api = axios.create({ baseURL: '/api' })

export function setToken(token?: string) {
	if (token) {
		api.defaults.headers.common['Authorization'] = `Bearer ${token}`
		localStorage.setItem('operain_token', token)
	} else {
		delete api.defaults.headers.common['Authorization']
		localStorage.removeItem('operain_token')
	}
}

// Load token on module import
const saved = typeof window !== 'undefined' ? localStorage.getItem('operain_token') : null
if (saved) setToken(saved)

