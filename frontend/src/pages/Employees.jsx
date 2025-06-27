import { useEffect, useState } from 'react'
import { api, authHeader } from '../api'

export default function Employees() {
  const [emps, setEmps] = useState([])

  useEffect(() => {
    api.get('/employees', { headers: authHeader() })
      .then(res => setEmps(res.data))
      .catch(console.error)
  }, [])

  return (
    <>
      <h2>Employees</h2>
      <ul>
        {emps.map(e => <li key={e.id}>{e.first_name} {e.last_name}</li>)}
      </ul>
    </>
  )
}
