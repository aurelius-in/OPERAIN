import { useEffect, useState } from 'react'
import axios from 'axios'

export default function Settings() {
	const [s, setS] = useState<any>(null)
	useEffect(() => { axios.get('/api/settings').then(r => setS(r.data)) }, [])
	return (
		<div>
			<h2>Settings</h2>
			{s ? (
				<div style={{ display: 'grid', gridTemplateColumns: '1fr 2fr', gap: 8 }}>
					<div>BayWalk</div><div>{s.baywalk_base_url}</div>
					<div>PerceptionLab</div><div>{s.perceptionlab_base_url}</div>
					<div>EdgeSight-QA</div><div>{s.edgesight_base_url}</div>
					<div>RAINLane</div><div>{s.rainlane_base_url}</div>
					<div>DriftHawk</div><div>{s.drifthawk_base_url}</div>
					<div>Use Redis</div><div>{String(s.use_redis)}</div>
					<div>Allow Local Login</div><div>{String(s.allow_local_login)}</div>
				</div>
			) : <p>Loading...</p>}
		</div>
	)
}

