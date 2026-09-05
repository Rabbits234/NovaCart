import axios from 'axios'

interface Product {
    id: number
    name: string
    price: number
    image: string
}

interface ProductCardProps {
    product: Product
}

function ProductCard({ product }: ProductCardProps) {

    const handleAddToCart = async () => {
        try {
            const token = localStorage.getItem('token')

            if (!token) {
                alert('Please login first')
                return
            }

            await axios.post(
                'http://127.0.0.1:8000/cart/items',
                {
                    product_id: product.id,
                    quantity: 1
                },
                {
                    headers: {
                        Authorization: `Bearer ${token}`
                    }
                }
            )

            alert(`${product.name} added to cart!`)

        } catch (error) {
            console.error('Add to cart failed:', error)
            alert('Could not add product to cart')
        }
    }

    return (
        <div className="rounded-2xl border bg-white p-5 hover:shadow-md transition">

            <div className="h-40 rounded-xl bg-gray-100 flex items-center justify-center">
                <img
                    src={product.image}
                    alt={product.name}
                    className="h-full w-full object-cover rounded-xl"
                />
            </div>

            <h3 className="mt-4 font-semibold text-lg">
                {product.name}
            </h3>

            <p className="mt-2 text-emerald-700 font-bold">
                ₹{product.price}
            </p>

            <button
                onClick={handleAddToCart}
                className="mt-4 w-full rounded-xl bg-emerald-900 py-3 text-white font-semibold hover:bg-emerald-800 transition"
            >
                Add to Cart
            </button>

        </div>
    )
}

export default ProductCard

