USE restaurant_db;

-- view the order_details table
select *
from order_details;

-- date range of orders
select min(order_date), max(order_date)
from order_details;

-- number of orders made
select count(DISTINCT order_id) as orders_count
from order_details;

-- total number of items ordered
select count(*)
from order_details;

-- order with the most number of items
select order_id, count(item_id) as items_count
from order_details
group by order_id 
order by items_count desc;

-- orders with more than 12 items
select count(*) 
from (select order_id, count(item_id) as items_count
from order_details
group by order_id 
having items_count>12) as num_orders;