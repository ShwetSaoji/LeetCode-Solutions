# Write your MySQL query statement below

select *, 
CASE
    WHEN dna_sequence like 'ATG%' then 1 else 0
END as has_start,
CASE
    WHEN dna_sequence like '%TAA' or dna_sequence like '%TAG' or dna_sequence like '%TGA' then 1 else 0
END as has_stop,
CASE
    WHEN dna_sequence like '%ATAT%' then 1 else 0
END as has_atat,
CASE
    WHEN dna_sequence like '%GGG%' then 1 else 0
END as has_ggg
from Samples