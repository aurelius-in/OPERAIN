import { useEffect, useState } from 'react'
import { loginDev } from '../api/auth'
import axios from 'axios'

export default function AuthCallback() {
	const [email, setEmail] = useState('user@example.com')
	const [password, setPassword] = useState('dev')
	const [msg, setMsg] = useState('')
	useEffect(() => {
		const params = new URLSearchParams(window.location.search)
		const code = params.get('code')
		if (code) {
			axios.get('/api/auth/oidc/callback?code=' + encodeURIComponent(code)).then(r => {
				setMsg('Logged in via SSO. You may navigate now.')
			}).catch(()=>{})
		}
	}, [])
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

