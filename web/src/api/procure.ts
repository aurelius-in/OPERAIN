import { api } from './client'

export async function listBOM() {
	const { data } = await api.get('/procure/bom')
	return data
}

export async function createPO(payload: any) {
	const { data } = await api.post('/procure/po', payload)
	return data
}

export async function listAssets() {
	const { data } = await api.get('/procure/assets')
	return data
}

export async function createAsset(payload: any) {
	const { data } = await api.post('/procure/assets', payload)
	return data
}

export async function provisionAsset(id: number) {
	const { data } = await api.post(`/procure/provision/${id}`)
	return data
}

