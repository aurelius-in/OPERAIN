import { api } from './client'

export async function listBOM() {
	const { data } = await api.get('/procure/bom')
	return data
}

export async function importBOM(file: File) {
	const form = new FormData()
	form.append('file', file)
	const { data } = await api.post('/procure/import-bom', form, { headers: { 'Content-Type': 'multipart/form-data' } })
	return data
}

export function exportBOMCsvUrl() {
	return '/api/procure/export-bom.csv'
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

export async function discoverCameras(endpoints: Array<{ url: string; user?: string; pass?: string }>) {
	const { data } = await api.post('/procure/discover-cameras', endpoints)
	return data
}

