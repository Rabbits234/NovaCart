function Hero(){
    return(
        <section className="min-h-[80vh] flex items-center justify-center px-8">
            <div className="text-center max-w-3xl">
                <p className="mb-4 text-sm font-semibold uppercase tracking-widest text-emerald-700">
                    100% Vegetarian.Fast.Fresh.
                </p>
                <h1 className="text-5xl md:text-7xl font-bold tracking-tight">
                    Everything you love,
                    <br />
                    <span className="text-emerald-700">
                        100% Vegetarian.
                    </span>
                    <br />
                    Delivered Fast
                </h1>
                <p className="mt-6 text-lg text-grey-600 max-w-2xl mx-auto">
                    Shop groceries,essentials,and everyday Products
                    from the comfort of your home.
                </p>
                <button className="mt-8 rounded-full bg-emerald-900 px-8 py-4 text-white font-semibold hover:bg-emerald-800 transition">
                    Shop Now
                </button>
            </div>
        </section>
    )
}

export default Hero