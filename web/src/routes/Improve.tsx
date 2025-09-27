import { useEffect, useState } from 'react'
import { listIncidents, createCapa, retest, promote } from '../api/improve'

type Incident = { id: number; source: string; sku: string }

export default function Improve() {
	const [tab, setTab] = useState<'incidents'|'capa'|'retest'|'promote'>('incidents')
	const [incidents, setIncidents] = useState<Incident[]>([])
	const [selected, setSelected] = useState<number | null>(null)
	const [promoteData, setPromoteData] = useState({ project_id: 1, model_version_id: 1 })
	const [result, setResult] = useState<any>(null)

	useEffect(() => { listIncidents().then(setIncidents) }, [])

	return (
		<div>
			<h2>Improve</h2>
			<div style={{ display: 'flex', gap: 8, marginBottom: 12 }}>
				<button onClick={() => setTab('incidents')}>Incident Inbox</button>
				<button onClick={() => setTab('capa')}>CAPA Board</button>
				<button onClick={() => setTab('retest')}>Re-test</button>
				<button onClick={() => setTab('promote')}>Promote</button>
			</div>

			{tab === 'incidents' && (
				<div>
					<table>
						<thead><tr><th>ID</th><th>Source</th><th>SKU</th><th /></tr></thead>
						<tbody>
							{incidents.map(i => (
								<tr key={i.id}><td>{i.id}</td><td>{i.source}</td><td>{i.sku}</td><td><button onClick={async () => { await createCapa({ incident_id: i.id, owner: 'User' }); setSelected(i.id) }}>Create CAPA</button></td></tr>
							))}
						</tbody>
					</table>
				</div>
			)}

			{tab === 'retest' && (
				<div>
					<p>Select an incident and request re-test in PerceptionLab.</p>
					<select value={selected ?? ''} onChange={e => setSelected(Number(e.target.value))}>
						<option value="">Select incident</option>
						{incidents.map(i => <option key={i.id} value={i.id}>{i.id} - {i.sku}</option>)}
					</select>
					<button disabled={!selected} onClick={async () => setResult(await retest(selected!))}>Re-test</button>
					{result && <pre>{JSON.stringify(result, null, 2)}</pre>}
				</div>
			)}

			{tab === 'promote' && (
				<div>
					<p>Promote model via DriftHawk.</p>
					<input placeholder="Project ID" value={promoteData.project_id} onChange={e => setPromoteData(p => ({ ...p, project_id: Number(e.target.value) }))} />
					<input placeholder="Model Version ID" value={promoteData.model_version_id} onChange={e => setPromoteData(p => ({ ...p, model_version_id: Number(e.target.value) }))} />
					<button onClick={async () => setResult(await promote(promoteData))}>Promote</button>
					{result && <pre>{JSON.stringify(result, null, 2)}</pre>}
				</div>
			)}
		</div>
	)
}

