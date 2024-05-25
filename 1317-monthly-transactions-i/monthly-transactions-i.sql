select SUBSTRING(trans_date, 1, 7) as month, country, COUNT(*) as trans_count,
SUM(if(state="approved",1,0)) as approved_count,
SUM(amount) as trans_total_amount,
SUM(if(state="approved",amount,0)) as approved_total_amount
from 
transactions
group by 1,2