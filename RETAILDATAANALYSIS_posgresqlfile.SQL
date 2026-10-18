CREATE TABLE retail_sales (
    order_id VARCHAR(20),
    order_date DATE,
    customer_id VARCHAR(20),
    region VARCHAR(50),
    state VARCHAR(100),
    category VARCHAR(50),
    product VARCHAR(100),
    quantity INT,
    unit_price NUMERIC(12,2),
    discount NUMERIC(5,2),
    sales NUMERIC(12,2),
    profit NUMERIC(12,2),
    payment_mode VARCHAR(50),
    ship_mode VARCHAR(50)
);

select*from retail_sales;

SELECT *
FROM retail_sales
LIMIT 10;

-- business analysis 
SELECT
    category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity
FROM retail_sales
GROUP BY category
ORDER BY total_sales DESC;


-- Monthly sales trend
SELECT
    DATE_TRUNC('month', order_date)::date AS month,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM retail_sales
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY month;

-- TOP 5 products by sales
SELECT
    product,
    SUM(quantity) AS units_sold,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit
FROM retail_sales
GROUP BY product
ORDER BY total_sales DESC
LIMIT 5;

-- Regional performance
SELECT
    region,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    SUM(quantity) AS total_quantity
FROM retail_sales
GROUP BY region
ORDER BY total_sales DESC;


-- profit margin by category 
SELECT
    category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(
        100.0 * SUM(profit) / NULLIF(SUM(sales), 0),
        2
    ) AS profit_margin_pct
FROM retail_sales
GROUP BY category
ORDER BY profit_margin_pct DESC;

