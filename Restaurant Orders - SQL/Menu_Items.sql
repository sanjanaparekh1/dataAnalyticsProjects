USE restaurant_db;

-- View the menu items table
select *
from menu_items;

-- Find the number of items on the menu
select count(*) as total_number
from menu_items;

-- Least expensive item on the menu
select *
from menu_items
order by price
limit 1;

-- Most expensive item on the menu
select *, price
from menu_items
order by price desc
limit 1;

-- Number of Italian dishes are there on the menu
select count(*) as count
from menu_items
where category ='Italian';

-- Least expensive Italian dish
select *
from menu_items
where category ='Italian'
order by price
limit 1;

-- Most expensive Italian dish
select *
from menu_items
where category ='Italian'
order by price desc
limit 1;

-- Number of dishes in each category
select category, count(menu_item_id) as number_of_items
from menu_items
group by category;

-- Average dish price within each category
select category,avg(price)
from menu_items
group by category;