import { useEffect, useState } from 'react'
import { listBOM, listAssets, createPO, createAsset, provisionAsset } from '../api/procure'

type BomItem = { id: number; sku: string; description: string; qty: number; alt_sku?: string }
type Asset = { id: number; type: string; serial: string; status: string }

export default function ProcureProvision() {
	const [tab, setTab] = useState<'po'|'vault'|'provision'|'discovery'>('po')
	const [bom, setBom] = useState<BomItem[]>([])
	const [assets, setAssets] = useState<Asset[]>([])
	const [newAsset, setNewAsset] = useState<Partial<Asset>>({ type: 'edge', serial: '' })

	useEffect(() => {
		listBOM().then(setBom)
		listAssets().then(setAssets)
	}, [])

	return (
		<div>
			<h2>Procure & Provision</h2>
			<div style={{ display: 'flex', gap: 8, marginBottom: 12 }}>
				<button onClick={() => setTab('po')}>PO Board</button>
				<button onClick={() => setTab('vault')}>Device Vault</button>
				<button onClick={() => setTab('provision')}>Provision Wizard</button>
				<button onClick={() => setTab('discovery')}>Camera Discovery</button>
			</div>

			{tab === 'po' && (
				<div>
					<h3>PO Board</h3>
					<table>
						<thead>
							<tr><th>SKU</th><th>Description</th><th>Qty</th><th /></tr>
						</thead>
						<tbody>
							{bom.map(i => (
								<tr key={i.id}><td>{i.sku}</td><td>{i.description}</td><td>{i.qty}</td><td><button onClick={() => createPO({ project_id: 1, items: [i] })}>Add to PO</button></td></tr>
							))}
						</tbody>
					</table>
				</div>
			)}

			{tab === 'vault' && (
				<div>
					<h3>Device Vault</h3>
					<div style={{ display: 'flex', gap: 8, margin: '8px 0' }}>
						<select value={newAsset.type} onChange={e => setNewAsset(a => ({ ...a, type: e.target.value }))}>
							<option value="edge">edge</option>
							<option value="camera">camera</option>
						</select>
						<input placeholder="Serial" value={newAsset.serial || ''} onChange={e => setNewAsset(a => ({ ...a, serial: e.target.value }))} />
						<button onClick={async () => { await createAsset({ project_id: 1, type: newAsset.type, serial: newAsset.serial, status: 'new' }); setAssets(await listAssets()) }}>Add</button>
					</div>
					<table>
						<thead>
							<tr><th>ID</th><th>Type</th><th>Serial</th><th>Status</th><th /></tr>
						</thead>
						<tbody>
							{assets.map(a => (
								<tr key={a.id}><td>{a.id}</td><td>{a.type}</td><td>{a.serial}</td><td>{a.status}</td><td><button onClick={async () => { await provisionAsset(a.id); setAssets(await listAssets()) }}>Mark Provisioned</button></td></tr>
							))}
						</tbody>
					</table>
				</div>
			)}

			{tab === 'provision' && (
				<div>
					<h3>Provision Wizard</h3>
					<p>Fill host/user/agent/cert fields as needed (stubbed).</p>
				</div>
			)}

			{tab === 'discovery' && (
				<div>
					<h3>Camera Discovery</h3>
					<p>Add RTSP endpoints and credentials (stubbed).</p>
				</div>
			)}
		</div>
	)
}

