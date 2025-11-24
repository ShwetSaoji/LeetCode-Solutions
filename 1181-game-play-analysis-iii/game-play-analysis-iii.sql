# Write your MySQL query statement below
select player_id, event_date,
SUM(games_played) OVER(PARTITION BY player_id ORDER by event_date) as games_played_so_far
from Activity