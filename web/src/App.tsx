import { Routes, Route, Link } from 'react-router-dom'
import Home from './routes/Home'
import ProcureProvision from './routes/ProcureProvision'
import Improve from './routes/Improve'
import EvidenceLocker from './routes/EvidenceLocker'
import Settings from './routes/Settings'

export default function App() {
	return (
		<div>
			<nav style={{ padding: 12, borderBottom: '1px solid #1f2124' }}>
				<Link to="/">Home</Link>
				<span style={{ margin: '0 8px' }} />
				<Link to="/procure-provision">Procure & Provision</Link>
				<span style={{ margin: '0 8px' }} />
				<Link to="/improve">Improve</Link>
				<span style={{ margin: '0 8px' }} />
				<Link to="/evidence">Evidence</Link>
				<span style={{ margin: '0 8px' }} />
				<Link to="/settings">Settings</Link>
			</nav>
			<div style={{ padding: 16 }}>
				<Routes>
					<Route path="/" element={<Home />} />
					<Route path="/procure-provision" element={<ProcureProvision />} />
					<Route path="/improve" element={<Improve />} />
					<Route path="/evidence" element={<EvidenceLocker />} />
					<Route path="/settings" element={<Settings />} />
				</Routes>
			</div>
		</div>
	)
}

