import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { configDefaults } from 'vitest/config'

export default defineConfig({
	plugins: [react()],
	server: {
		host: true,
		port: 5173
	},
	preview: {
		host: true,
		port: 5173
	},
	test: {
		environment: 'jsdom',
		coverage: { provider: 'v8' },
		exclude: [...configDefaults.exclude]
	}
})

