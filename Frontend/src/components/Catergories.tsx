const categories = [
  { name: 'Fresh Fruits & Vegetables', emoji: '🥬' },
  { name: 'Dairy & Paneer', emoji: '🥛' },
  { name: 'Bakery', emoji: '🍞' },
  { name: 'Snacks', emoji: '🍿' },
  { name: 'Staples & Grains', emoji: '🌾' },
  { name: 'Sweets & Desserts', emoji: '🍰' },
  { name: 'Beverages', emoji: '🥤' },
  { name: 'Vegan', emoji: '🌱' },
]

function Categories() {
  return (
    <section className="px-8 py-16">
      <div className="max-w-6xl mx-auto">

        <h2 className="text-3xl font-bold">
          Shop by Category
        </h2>

        <p className="mt-2 text-gray-600">
          Explore our range of 100% vegetarian products.
        </p>

        <div className="mt-8 grid grid-cols-2 md:grid-cols-4 gap-5">
          {categories.map((category) => (
            <div
              key={category.name}
              className="rounded-2xl border bg-white p-6 text-center hover:shadow-md transition cursor-pointer"
            >
              <div className="text-5xl">
                {category.emoji}
              </div>

              <h3 className="mt-4 font-semibold">
                {category.name}
              </h3>
            </div>
          ))}
        </div>

      </div>
    </section>
  )
}

export default Categories

