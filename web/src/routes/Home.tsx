import { useEffect, useState } from 'react'
import axios from 'axios'

type Health = { [k: string]: { status: 'green' | 'yellow' | 'red' } }

export default function Home() {
	const [health, setHealth] = useState<Health>({})
	const [settings, setSettings] = useState<any>({})
	useEffect(() => {
		let done = false
		axios.get('/api/integrations/health').then(r => !done && setHealth(r.data)).catch(() => !done && setHealth({}))
		axios.get('/api/settings').then(r => !done && setSettings(r.data)).catch(() => !done && setSettings({}))
		return () => { done = true }
	}, [])

	const open = (url?: string) => { if (url) window.open(url, '_blank') }

	return (
		<div className="tile-grid">
			<div className="tile">
				<h3>Plan (BayWalk) <span title="Open the planning tool to create BOM and coverage">?</span></h3>
				<span className={`badge ${health.baywalk?.status || 'red'}`}>{health.baywalk?.status || 'red'}</span>
				<div style={{ marginTop: 8 }}>
					<button onClick={() => open(settings.baywalk_base_url)}>Open BayWalk</button>
				</div>
			</div>
			<div className="tile">
				<h3>Procure & Provision <span title="Manage POs, devices, and enrollment">?</span></h3>
				<p>PO Board, Device Vault, Provision Wizard, Camera Discovery</p>
				<div style={{ marginTop: 8 }}>
					<a href="/procure-provision">Open</a>
				</div>
			</div>
			<div className="tile">
				<h3>Prove (PerceptionLab) <span title="Request and view evaluation reports">?</span></h3>
				<span className={`badge ${health.perceptionlab?.status || 'red'}`}>{health.perceptionlab?.status || 'red'}</span>
				<div style={{ marginTop: 8 }}>
					<button onClick={() => open(settings.perceptionlab_base_url)}>Open PerceptionLab</button>
				</div>
			</div>
			<div className="tile">
				<h3>Run (EdgeSight-QA) <span title="Monitor pass/fail on the line">?</span></h3>
				<span className={`badge ${health.edgesight?.status || 'red'}`}>{health.edgesight?.status || 'red'}</span>
				<div style={{ marginTop: 8 }}>
					<button onClick={() => open(settings.edgesight_base_url)}>Open EdgeSight-QA</button>
				</div>
			</div>
			<div className="tile">
				<h3>Comply (RAINLane) <span title="Get SOP answers with citations">?</span></h3>
				<span className={`badge ${health.rainlane?.status || 'red'}`}>{health.rainlane?.status || 'red'}</span>
				<div style={{ marginTop: 8 }}>
					<button onClick={() => open(settings.rainlane_base_url)}>Open RAINLane</button>
				</div>
			</div>
			<div className="tile">
				<h3>Operate (DriftHawk) <span title="Promote signed releases safely">?</span></h3>
				<span className={`badge ${health.drifthawk?.status || 'red'}`}>{health.drifthawk?.status || 'red'}</span>
				<div style={{ marginTop: 8 }}>
					<button onClick={() => open(settings.drifthawk_base_url)}>Open DriftHawk</button>
				</div>
			</div>
			<div className="tile">
				<h3>Improve <span title="Incidents → CAPA → Re-test → Promote">?</span></h3>
				<p>Incidents, CAPA, Re-test, Promote</p>
				<div style={{ marginTop: 8 }}>
					<a href="/improve">Open</a>
				</div>
			</div>
		</div>
	)
}

