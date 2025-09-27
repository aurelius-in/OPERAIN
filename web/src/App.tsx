import { Routes, Route, Link } from 'react-router-dom'
import { useEffect, useState } from 'react'
import { me } from './api/auth'
import Home from './routes/Home'
import ProcureProvision from './routes/ProcureProvision'
import Improve from './routes/Improve'
import EvidenceLocker from './routes/EvidenceLocker'
import Settings from './routes/Settings'
import RequireAuth from './components/RequireAuth'

export default function App() {
	const [user, setUser] = useState<any>(null)
	useEffect(() => { me().then(setUser).catch(()=>setUser(null)) }, [])
	return (
		<div>
			<nav style={{ padding: 12, borderBottom: '1px solid #1f2124', display: 'flex', alignItems: 'center', gap: 12 }}>
				<div style={{ display: 'flex', gap: 8 }}>
					<Link to="/">Home</Link>
					<Link to="/procure-provision">Procure & Provision</Link>
					<Link to="/improve">Improve</Link>
					<Link to="/evidence">Evidence</Link>
					<Link to="/settings">Settings</Link>
				</div>
				<div style={{ marginLeft: 'auto' }}>
					{user ? <span>{user.name} · {user.role}</span> : <Link to="/auth">Login</Link>}
				</div>
			</nav>
			<div style={{ padding: 16 }}>
				<Routes>
					<Route path="/" element={<Home />} />
					<Route path="/procure-provision" element={<RequireAuth><ProcureProvision /></RequireAuth>} />
					<Route path="/improve" element={<RequireAuth><Improve /></RequireAuth>} />
					<Route path="/evidence" element={<EvidenceLocker />} />
					<Route path="/settings" element={<Settings />} />
					<Route path="/auth" element={<AuthCallback />} />
				</Routes>
			</div>
		</div>
	)
}

