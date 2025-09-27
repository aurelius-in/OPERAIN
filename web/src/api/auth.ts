import { api, setToken } from './client'

export async function loginDev(email: string, password: string) {
	const params = new URLSearchParams()
	params.append('username', email)
	params.append('password', password)
	const { data } = await api.post('/auth/login', params, { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } })
	setToken(data.access_token)
	return data
}

export async function me() {
	const { data } = await api.get('/auth/me')
	return data
}

