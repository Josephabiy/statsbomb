"""
Yellow taxi data has been ingested from 2018-01 till 2020-06
"""

Q1 = """
	SELECT -- Get average most profitable Pickup location
	    t1.PULocationID as PULocationID,
	    t1.DOLocationID as DOLocationID,
	    z.Borough as PULocation_Borough,
	    z.Zone as PULocation_Zone,
	    MAX(t1.highest_avg_revenue) as profit
	FROM
	    (SELECT -- Get avg total and tip per route
	        PULocationID,
	        DOLocationID,
	        SUM(AVG(total_amount) + AVG(tip_amount)) OVER (PARTITION BY PULocationID, DOLocationID) AS highest_avg_revenue
	    FROM 
	        trips.taxi
	    GROUP BY 1, 2
	        ) t1
	LEFT JOIN trips.zones z
	ON t1.PULocationID = z.LocationID
	GROUP BY 1,2,3,4
	ORDER BY profit desc
	LIMIT 1
"""


Q2 = """
	SELECT -- Routes where route_time is higher than average
	    t2.PULocationID as PULocationID,
	    t2.DOLocationID as DOLocationID,
	    t2.route_time as route_time,
	    t2.avg_route_time as avg_route_time
	    FROM
	        (SELECT -- Get avg route times per route
	            t1.PULocationID as PULocationID,
	            t1.DOLocationID as DOLocationID,
	            t1.route_time as route_time,
	            AVG(t1.route_time) OVER(partition by PULocationID, DOLocationID) avg_route_time
	        FROM
	            (SELECT -- Get route times in seconds
	                PULocationID,
	                DOLocationID,
	                UNIX_TIMESTAMP(tpep_dropoff_datetime) - UNIX_TIMESTAMP(tpep_pickup_datetime) as route_time
	            FROM 
	                trips.taxi) as t1
	        ) as t2
	WHERE
	    route_time > avg_route_time
"""

Q3 = """
	SELECT -- Average tip by location (high to low)
	    t.PULocationID as PULocationID,
	    MAX(z.Borough) as Borough,
	    MAX(z.Zone) as Zone,
	    AVG(tip_amount) as avg_tip_amount
	FROM
	    trips.taxi t
	LEFT JOIN
	    trips.zones z
	ON t.PULocationID = z.LocationID
	GROUP BY 1
	ORDER BY avg_tip_amount desc
"""

Q4 = """
	SELECT
	    t2.date_ymd as date_ymd,
	    COUNT(*) as potential_shared_rides
	FROM (
	    SELECT 
	        *
	    FROM (
	        SELECT -- Ride share opportunities per route and time
	            tpep_pickup_datetime,
	            PULocationID,
	            DOLocationId,
	            COUNT(passenger_count) OVER(partition by PULocationID, DOLocationID, tpep_pickup_datetime) as share_opportunities,
	            date_format(tpep_pickup_datetime, '%Y-%m-%d') as date_ymd
	        FROM
	            trips.taxi
	        WHERE
	            passenger_count = 1 -- where there is only 1 person per ride
	        ) t1
	    WHERE   
	        share_opportunities > 1 -- where 2 people trying to get on same taxi per route
	    AND 
	        tpep_pickup_datetime
	    BETWEEN -- 5min before and after window
	    	DATE_ADD(tpep_pickup_datetime, INTERVAL -5 MINUTE) 
	    AND
	        DATE_ADD(tpep_pickup_datetime, INTERVAL 5 MINUTE) 
	    GROUP BY 1,2,3,4,5
	) t2
	GROUP BY 1
	ORDER BY 1 ASC
"""