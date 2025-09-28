import { useState } from 'react'
import { loginDev } from '../api/auth'

export default function AuthCallback() {
	const [email, setEmail] = useState('user@example.com')
	const [password, setPassword] = useState('dev')
	const [msg, setMsg] = useState('')
	return (
		<div>
			<h2>Login</h2>
			<p>Local-only login for development (set ALLOW_LOCAL_LOGIN=true).</p>
			<div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8, maxWidth: 400 }}>
				<input placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} />
				<input placeholder="Password" type="password" value={password} onChange={e => setPassword(e.target.value)} />
				<button onClick={async () => { await loginDev(email, password); setMsg('Logged in. Refresh or navigate.'); }}>Login</button>
			</div>
			{msg && <p>{msg}</p>}
		</div>
	)
}

