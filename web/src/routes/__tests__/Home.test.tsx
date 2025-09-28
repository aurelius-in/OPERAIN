import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen } from '@testing-library/react'
import { BrowserRouter } from 'react-router-dom'
import Home from '../Home'

vi.mock('axios', () => ({
  default: {
    get: vi.fn((url:string)=> {
      if (url.includes('/integrations/health')) return Promise.resolve({ data: {} })
      if (url.includes('/settings')) return Promise.resolve({ data: {} })
      return Promise.resolve({ data: {} })
    })
  }
}))

describe('Home', () => {
  beforeEach(() => {
    render(<BrowserRouter><Home/></BrowserRouter>)
  })
  it('renders tiles', () => {
    expect(screen.getByText('Procure & Provision')).toBeDefined()
    expect(screen.getByText('Improve')).toBeDefined()
  })
})

