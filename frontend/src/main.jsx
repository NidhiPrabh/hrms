import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import App from './pages/App'
import Departments from './pages/Departments'
import Employees from './pages/Employees'

ReactDOM.createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <nav>
      <Link to="/">Home</Link> | <Link to="/departments">Departments</Link> | <Link to="/employees">Employees</Link>
    </nav>
    <Routes>
      <Route path="/" element={<App />} />
      <Route path="/departments" element={<Departments />} />
      <Route path="/employees" element={<Employees />} />
    </Routes>
  </BrowserRouter>
)
