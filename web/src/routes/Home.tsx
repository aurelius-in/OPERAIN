import { useEffect, useState } from 'react'
import axios from 'axios'

type Health = { [k: string]: { status: 'green' | 'yellow' | 'red' } }

export default function Home() {
	const [health, setHealth] = useState<Health>({})
	const [settings, setSettings] = useState<any>({})
	useEffect(() => {
		axios.get('/api/integrations/health').then(r => setHealth(r.data)).catch(() => setHealth({}))
		axios.get('/api/settings').then(r => setSettings(r.data)).catch(() => setSettings({}))
	}, [])

	const open = (url?: string) => { if (url) window.open(url, '_blank') }

	return (
		<div className="tile-grid">
			<div className="tile">
				<h3>Plan (BayWalk)</h3>
				<span className={`badge ${health.baywalk?.status || 'red'}`}>{health.baywalk?.status || 'red'}</span>
				<div style={{ marginTop: 8 }}>
					<button onClick={() => open(settings.baywalk_base_url)}>Open BayWalk</button>
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
					<button onClick={() => open(settings.perceptionlab_base_url)}>Open PerceptionLab</button>
				</div>
			</div>
			<div className="tile">
				<h3>Run (EdgeSight-QA)</h3>
				<span className={`badge ${health.edgesight?.status || 'red'}`}>{health.edgesight?.status || 'red'}</span>
				<div style={{ marginTop: 8 }}>
					<button onClick={() => open(settings.edgesight_base_url)}>Open EdgeSight-QA</button>
				</div>
			</div>
			<div className="tile">
				<h3>Comply (RAINLane)</h3>
				<span className={`badge ${health.rainlane?.status || 'red'}`}>{health.rainlane?.status || 'red'}</span>
				<div style={{ marginTop: 8 }}>
					<button onClick={() => open(settings.rainlane_base_url)}>Open RAINLane</button>
				</div>
			</div>
			<div className="tile">
				<h3>Operate (DriftHawk)</h3>
				<span className={`badge ${health.drifthawk?.status || 'red'}`}>{health.drifthawk?.status || 'red'}</span>
				<div style={{ marginTop: 8 }}>
					<button onClick={() => open(settings.drifthawk_base_url)}>Open DriftHawk</button>
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

