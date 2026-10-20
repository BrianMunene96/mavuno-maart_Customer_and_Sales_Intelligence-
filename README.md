# mavuno-maart Customer and Sales Intelligence

# Introduction

## Problem framing

Kenya's modern retail sector is growing fast and is highly competitive. Chains such as Naivas, Quickmart and Carrefour keep opening stores across the counties, and customers have more choice than ever. For a growing chain, guesswork about customers and sales is costly. Without evidence, management cannot see which stores and products really drive revenue or which loyal customers are quietly shopping elsewhere. Stock, staffing and promotions are also harder to plan for the coming month.

## Business objectives

This project answers the questions a retail manager asks most often:

1. **Who buys what, where and when?** Customer segments, product categories, stores, counties, days and times of purchase.
2. **What drives revenue?** The products, categories and stores that contribute most to sales.
3. **Which customers are drifting away?** Identifying loyal customers whose buying activity is declining, before they are lost.
4. **What demand should we expect next month?** A forecast to support stock and staffing decisions.
5. **Do promotions work?** Whether discounts produce a real, measurable increase in sales.

## Project goal

The goal is to turn transaction data into evidence a manager can act on. I clean and prepare the data in Python, analyse it with PostgreSQL and statistical tests, and build and evaluate a demand forecast and a churn model. The results come together in a Power BI dashboard that presents clear, actionable insights.

## Data generation

Real transaction data from Kenyan retailers is not publicly available, so I generated a synthetic dataset in Python for a fictional chain, **Mavuno Mart**. The data is designed to reflect real Kenyan figures and shopping behaviour:

- Products are familiar Kenyan grocery items priced in Kenyan shillings, such as maize flour, sukuma wiki, mala and tea leaves.
- Kenyan public holidays are included.
- Purchases follow realistic patterns: month-end payday spending, weekend and December peaks, a January slowdown and back-to-school demand.
- M-Pesa is the dominant payment method, alongside cash, card and loyalty points.

The dataset covers 24 months, from October 2024 to September 2026. It includes 30 stores, 6,000 loyalty customers, 273 products, about 313,000 transactions and about 1.3 million line items.

## What the data contains

| Table                 | Description                                                                                                                     |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `transactions`      | One row per basket: date and time, store, customer (blank for walk-in shoppers), payment method, M-Pesa reference, basket value |
| `transaction_items` | One row per product in a basket: product, quantity, unit price, discount, promotion, line total                                 |
| `customers`         | Loyalty members: gender, age band, home store, county, sign-up date                                                             |
| `stores`            | Store name, town, county, format (hypermarket, supermarket, express), opening date, size, M-Pesa till number                    |
| `products`          | Product name, category, brand tier, price and unit cost                                                                         |
| `promotions`        | Discounted category, discount percentage, start and end dates, participating stores                                             |
| `counties`          | County codes and 2019 Census population                                                                                         |
| `calendar`          | Every date with weekend, payday window and public holiday flags                                                                 |
