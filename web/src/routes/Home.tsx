import { useEffect, useState } from 'react'
import axios from 'axios'

type Health = { [k: string]: { status: 'green' | 'yellow' | 'red' } }

export default function Home() {
	const [health, setHealth] = useState<Health>({})
	useEffect(() => {
		axios.get('/api/integrations/health').then(r => setHealth(r.data)).catch(() => setHealth({}))
	}, [])

	const open = (url?: string) => { if (url) window.open(url, '_blank') }
	const env = (name: string) => (import.meta.env[`VITE_${name}` as any] as string | undefined)

	return (
		<div className="tile-grid">
			<div className="tile">
				<h3>Plan (BayWalk)</h3>
				<span className={`badge ${health.baywalk?.status || 'red'}`}>{health.baywalk?.status || 'red'}</span>
				<div style={{ marginTop: 8 }}>
					<button onClick={() => open(env('BAYWALK_BASE_URL'))}>Open BayWalk</button>
				</div>
			</div>
			<div className="tile">
				<h3>Procure & Provision</h3>
				<p>PO Board, Device Vault, Provision Wizard, Camera Discovery</p>
				<div style={{ marginTop: 8 }}>
					<a href="/procure-provision">Open</a>
				</div>
			</div>
			<div className="tile">
				<h3>Prove (PerceptionLab)</h3>
				<span className={`badge ${health.perceptionlab?.status || 'red'}`}>{health.perceptionlab?.status || 'red'}</span>
				<div style={{ marginTop: 8 }}>
					<button onClick={() => open(env('PERCEPTIONLAB_BASE_URL'))}>Open PerceptionLab</button>
				</div>
			</div>
			<div className="tile">
				<h3>Run (EdgeSight-QA)</h3>
				<span className={`badge ${health.edgesight?.status || 'red'}`}>{health.edgesight?.status || 'red'}</span>
				<div style={{ marginTop: 8 }}>
					<button onClick={() => open(env('EDGESIGHT_BASE_URL'))}>Open EdgeSight-QA</button>
				</div>
			</div>
			<div className="tile">
				<h3>Comply (RAINLane)</h3>
				<span className={`badge ${health.rainlane?.status || 'red'}`}>{health.rainlane?.status || 'red'}</span>
				<div style={{ marginTop: 8 }}>
					<button onClick={() => open(env('RAINLANE_BASE_URL'))}>Open RAINLane</button>
				</div>
			</div>
			<div className="tile">
				<h3>Operate (DriftHawk)</h3>
				<span className={`badge ${health.drifthawk?.status || 'red'}`}>{health.drifthawk?.status || 'red'}</span>
				<div style={{ marginTop: 8 }}>
					<button onClick={() => open(env('DRIFTHAWK_BASE_URL'))}>Open DriftHawk</button>
				</div>
			</div>
			<div className="tile">
				<h3>Improve</h3>
				<p>Incidents, CAPA, Re-test, Promote</p>
				<div style={{ marginTop: 8 }}>
					<a href="/improve">Open</a>
				</div>
			</div>
		</div>
	)
}

