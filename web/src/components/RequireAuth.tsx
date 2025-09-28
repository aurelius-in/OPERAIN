import { ReactNode, useEffect, useState } from 'react'
import { me } from '../api/auth'

export default function RequireAuth({ children }: { children: ReactNode }) {
	const [ok, setOk] = useState<boolean | null>(null)
	useEffect(() => { me().then(()=>setOk(true)).catch(()=>setOk(false)) }, [])
	if (ok === null) return <p>Checking access…</p>
	if (!ok) return <p>Not authorized. Please <a href="/auth">login</a>.</p>
	return <>{children}</>
}

