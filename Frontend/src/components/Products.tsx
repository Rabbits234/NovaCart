import { useEffect, useState } from 'react'
import axios from 'axios'
import ProductCard from './ProductCard'

interface Product {
    id: number
    name: string
    price: number
    image: string
}

function Products() {
    const [products, setProducts] = useState<Product[]>([])

    useEffect(() => {
        const fetchProducts = async () => {
            try {
                const token = localStorage.getItem('token')

                const response = await axios.get(
                    'http://127.0.0.1:8000/products',
                    {
                        headers: {
                            Authorization: `Bearer ${token}`
                        }
                    }
                )

                setProducts(response.data)
            } catch (error) {
                console.error('Error fetching products:', error)
            }
        }

        fetchProducts()
    }, [])

    return (
        <section className="px-8 py-10">
            <div className="max-w-7xl mx-auto">

                <h2 className="text-3xl font-bold mb-2">
                    Featured Products
                </h2>

                <p className="text-gray-600 mb-8">
                    100% Vegetarian
                </p>

                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                    {products.map((product) => (
                        <ProductCard
                            key={product.id}
                            product={product}
                        />
                    ))}
                </div>

            </div>
        </section>
    )
}

export default Products

