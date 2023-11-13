# Write your MySQL query statement below
select distinct(page_id) as recommended_page from likes 
where
user_id in 
(
 select 
 (
  CASE
    WHEN user1_id=1 then user2_id
    WHEN user2_id=1 then user1_id
  END
 ) as user_id from Friendship
)
and 
page_id not in (
  select page_id from likes where user_id=1
)
