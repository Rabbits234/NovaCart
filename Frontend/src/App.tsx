import Navbar from './components/Navbar'
import Hero from './components/Hero'
import Categories from './components/Catergories'
import Products from './components/Products'
import Login from './components/Login'

function App() {
  return (
    <div className="min-h-screen">
      <Navbar />
      <Hero />
      <Categories />
      <Login />
      <Products />
    </div>
  )
}

export default App