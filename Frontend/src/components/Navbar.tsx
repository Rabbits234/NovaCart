function Navbar() {
  return (
    <nav className="w-full px-8 py-5 flex items-center justify-between border-b">
      <h1 className="text-2xl font-bold">
        NovaCart
      </h1>

      <div className="flex items-center gap-6">
        <button>Home</button>
        <button>Products</button>
        <button>Cart</button>
        <button>Login</button>
      </div>
    </nav>
  )
}

export default Navbar