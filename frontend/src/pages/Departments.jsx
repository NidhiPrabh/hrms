import { useEffect, useState } from 'react'
import { api, authHeader } from '../api'

export default function Departments() {
  const [deps, setDeps] = useState([])

  useEffect(() => {
    api.get('/departments', { headers: authHeader() })
      .then(res => setDeps(res.data))
      .catch(console.error)
  }, [])

  return (
    <>
      <h2>Departments</h2>
      <ul>
        {deps.map(d => <li key={d.id}>{d.name}</li>)}
      </ul>
    </>
  )
}
