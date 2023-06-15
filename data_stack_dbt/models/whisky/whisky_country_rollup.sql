select 
	country,
	sum(cast(whiskybase_votes as integer)) as total_votes,
	sum(cast(whiskybase_whiskies as integer)) as total_whiskies,
	count(*) as num_distilleries,
	avg(cast(whiskybase_whiskies as integer)) as avg_num_whiskies_per_distillery,
	max(cast(whiskybase_rating as float)) as highest_rating,
	avg(cast(whiskybase_rating as float)) as average_rating
from 
        {{ source("postgres", "distilleries_info") }}
group by 
        country