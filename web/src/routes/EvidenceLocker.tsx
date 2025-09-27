import { useEffect, useState } from 'react'
import axios from 'axios'

type Item = {
	ref: string
	type: string
	url?: string
	project_id?: number
	sku?: string
	created_at?: string
}

export default function EvidenceLocker() {
	const [items, setItems] = useState<Item[]>([])
	const [projectId, setProjectId] = useState('')
	const [sku, setSku] = useState('')

	const query = () => {
		const params: any = {}
		if (projectId) params.project_id = Number(projectId)
		if (sku) params.sku = sku
		axios.get('/api/evidence/search', { params }).then(r => setItems(r.data))
	}

	useEffect(() => { query() }, [])

	return (
		<div>
			<h2>Evidence Locker</h2>
			<div style={{ display: 'flex', gap: 8, marginBottom: 12 }}>
				<input placeholder="Project ID" value={projectId} onChange={e => setProjectId(e.target.value)} />
				<input placeholder="SKU" value={sku} onChange={e => setSku(e.target.value)} />
				<button onClick={query}>Search</button>
			</div>
			<div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 12 }}>
				{items.map(i => (
					<div key={i.ref} className="tile">
						<div style={{ fontWeight: 600 }}>{i.type}</div>
						<div style={{ fontSize: 12, opacity: 0.8 }}>ref: {i.ref}</div>
						{i.url && <a href={i.url} target="_blank" rel="noreferrer">Open</a>}
						<div style={{ fontSize: 12 }}>{i.created_at}</div>
					</div>
				))}
			</div>
		</div>
	)
}

