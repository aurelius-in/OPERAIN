import { api } from './client'

export async function listIncidents() {
	const { data } = await api.get('/improve/incidents')
	return data
}

export async function createIncident(payload: any) {
	const { data } = await api.post('/improve/incidents', payload)
	return data
}

export async function updateIncident(id: number, payload: any) {
	const { data } = await api.patch(`/improve/incidents/${id}`, payload)
	return data
}

export async function createCapa(payload: any) {
	const { data } = await api.post('/improve/capa', payload)
	return data
}

export async function updateCapa(id: number, payload: any) {
	const { data } = await api.patch(`/improve/capa/${id}`, payload)
	return data
}

export async function retest(incidentId: number) {
	const { data } = await api.post(`/improve/retest/${incidentId}`)
	return data
}

export async function promote(payload: any) {
	const { data } = await api.post('/improve/promote', payload)
	return data
}

