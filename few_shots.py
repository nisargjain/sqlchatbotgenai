few_shots = [
    {
        'Question': "How many Dell laptops with i7 processor and 16GB RAM are in stock?",
        'SQLQuery': "SELECT SUM(stock_quantity) FROM laptops WHERE brand = 'Dell' AND processor = 'i7' AND ram = '16GB';",
        'SQLResult': "Result of the SQL query",
        'Answer': "15"
    },
    {
        'Question': "What is the total value of inventory for all Apple laptops?",
        'SQLQuery': "SELECT SUM(price * stock_quantity) FROM laptops WHERE brand = 'Apple';",
        'SQLResult': "Result of the SQL query",
        'Answer': "853840.59"
    },
    {
        'Question': "How much revenue will be generated if all Lenovo laptops are sold today with discounts applied?",
        'SQLQuery': """
        SELECT SUM(a.total_amount * ((100 - COALESCE(d.pct_discount,0)) / 100)) AS total_revenue
        FROM (
            SELECT SUM(price * stock_quantity) AS total_amount, laptop_id
            FROM laptops
            WHERE brand = 'Lenovo'
            GROUP BY laptop_id
        ) a
        LEFT JOIN discounts d ON a.laptop_id = d.laptop_id;
        """,
        'SQLResult': "Result of the SQL query",
        'Answer': "766426.12000000"
    },
    {
        'Question': "What would be the revenue from selling all HP laptops without any discounts?",
        'SQLQuery': "SELECT SUM(price * stock_quantity) FROM laptops WHERE brand = 'HP';",
        'SQLResult': "Result of the SQL query",
        'Answer': "1518272.73"
    },
    {
        'Question': "How many MSI laptops with 256GB SSD storage are currently in stock?",
        'SQLQuery': "SELECT SUM(stock_quantity) FROM laptops WHERE brand = 'MSI' AND storage = '256GB SSD';",
        'SQLResult': "Result of the SQL query",
        'Answer': "77"
    },
    {
        'Question': "What is the total inventory worth of all laptops that have 32GB RAM?",
        'SQLQuery': "SELECT SUM(price * stock_quantity) FROM laptops WHERE ram = '32GB';",
        'SQLResult': "Result of the SQL query",
        'Answer': "1342423.35"
    },
    {
        'Question': "How much revenue will be generated if all Asus laptops with i5 processor and Laptops with discounts applied are sold?",
        'SQLQuery': """
        SELECT SUM(a.total_amount * ((100 - COALESCE(d.pct_discount,0)) / 100)) AS total_revenue
        FROM (
            SELECT SUM(price * stock_quantity) AS total_amount, laptop_id
            FROM laptops
            WHERE brand = 'Asus' AND processor = 'i5'
            GROUP BY laptop_id
        ) a
        LEFT JOIN discounts d ON a.laptop_id = d.laptop_id;
        """,
        'SQLResult': "Result of the SQL query",
        'Answer': "138711.84"
    }
]
