USE restaurant_db;

-- Combine the menu_items and order_details table
select *
from order_details od LEFT JOIN menu_items mi
ON od.item_id = mi.menu_item_id;

-- least ordered item and category
select item_name, count(order_details_id) as num_purchases
from order_details od LEFT JOIN menu_items mi
ON od.item_id = mi.menu_item_id
group by item_name
order by num_purchases
limit 1;

-- most ordered item and category
select item_name, count(order_details_id) as num_purchases
from order_details od LEFT JOIN menu_items mi
ON od.item_id = mi.menu_item_id
group by item_name
order by num_purchases desc
limit 1;

-- top 5 orders that spent the most money
select order_id, sum(price) as total_price
from order_details od LEFT JOIN menu_items mi
ON od.item_id = mi.menu_item_id
group by order_id
order by total_price desc
limit 5;

-- details of the highest spend order
select order_id,category, item_name, price
from order_details od LEFT JOIN menu_items mi
ON od.item_id = mi.menu_item_id
where order_id=440;

-- details of the 5 highest spend orders
select order_id,category, count(item_id) as num_items
from order_details od LEFT JOIN menu_items mi
ON od.item_id = mi.menu_item_id
where order_id in(440,2075,1957,330,2675)
group by order_id,category;