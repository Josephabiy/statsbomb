# CREATE TMP TABLE QUERIES
YELLOW_TAXI_TMP_CREATE_TABLE_QUERY = """
	CREATE TABLE tmp.yellow_taxi (
		`csv_date` varchar(10),
	    `VendorID` int(10),
	    `tpep_pickup_datetime` datetime,
	    `tpep_dropoff_datetime` datetime,
	    `passenger_count` int(10),
	    `trip_distance` decimal,
	    `RatecodeID` int(10),
	    `store_and_fwd_flag` varchar(200),
	    `PULocationID` int(10),
	    `DOLocationID` int(10),
	    `payment_type` int(10),
	    `fare_amount` decimal,
	    `extra` decimal,
	    `mta_tax` decimal,
	    `tip_amount` decimal,
	    `tolls_amount` decimal,
	    `improvement_surcharge` decimal,
	    `total_amount` decimal,
	    `congestion_surcharge` decimal
	)
"""

GREEN_TAXI_TMP_CREATE_TABLE_QUERY = """
	CREATE TABLE tmp.green_taxi (
		`csv_date` varchar(10),
		`VendorID` int(10),
		`lpep_pickup_datetime` datetime,
		`lpep_dropoff_datetime` datetime,
		`store_and_fwd_flag` varchar(200),
		`RatecodeID` int(10),
		`PULocationID` int(10),
		`DOLocationID` int(10),
		`passenger_count` int(10),
		`trip_distance` decimal,
		`fare_amount` decimal,
		`extra` decimal,
		`mta_tax` decimal,
		`tip_amount` decimal,
		`tolls_amount` decimal,
		`ehail_fee` decimal,
		`improvement_surcharge` decimal,
		`total_amount` decimal,
		`payment_type` int(10),
		`trip_type` int(10),
		`congestion_surcharge` decimal
	)
"""

FOR_HIRE_TAXI_TMP_CREATE_TABLE_QUERY = """
	CREATE TABLE tmp.for_hire (
		`csv_date` varchar(10),
		`dispatching_base_num` varchar(200),
		`pickup_datetime` datetime,
		`dropoff_datetime` datetime,
		`PULocationID` int(10),
		`DOLocationID` int(10),
		`SR_Flag` tinyint(1)
	)
"""

HIGH_VOLUME_FOR_HIRE_TAXI_TMP_CREATE_TABLE_QUERY = """
	CREATE TABLE tmp.hv_for_hire (
		`csv_date` varchar(10),
		`hvfhs_license_num` varchar(200),
		`dispatching_base_num` varchar(200),
		`pickup_datetime` datetime,
		`dropoff_datetime` datetime,
		`PULocationID` int(10),
		`DOLocationID` int(10),
		`SR_Flag` tinyint(1)
	)
"""


# CREATE DIMENSION TABLE QUERIES
VENDOR_DIMENSION_CREATE_TABLE_QUERY = """
	CREATE TABLE trips.vendors (
	    `VendorID` int(10),
	    `vendor` varchar(200)
	)
"""

PAYMENT_DIMENSION_CREATE_TABLE_QUERY = """
	CREATE TABLE trips.payment_type (
	    `payment_type_id` int(10),
	    `payment_type` varchar(200)
	)
"""

RATECODE_DIMENSION_CREATE_TABLE_QUERY = """
	CREATE TABLE trips.ratecode (
	    `RateCodeID` int(10),
	    `rate_code` varchar(200)
	)
"""

TRIP_TYPE_DIMENSION_CREATE_TABLE_QUERY = """
	CREATE TABLE trips.trip_type (
	    `Trip_type` int(10),
	    `trip_name` varchar(200)
	)
"""

# CREATE FACT TABLE QUERIES
YELLOW_TAXI_CREATE_TABLE_QUERY = """
	CREATE TABLE trips.yellow_taxi (
		`csv_date` varchar(10) NOT NULL,
	    `VendorID` int(10) NOT NULL,
	    `tpep_pickup_datetime` datetime NOT NULL,
	    `tpep_dropoff_datetime` datetime NOT NULL,
	    `passenger_count` int(10) NOT NULL,
	    `trip_distance` decimal NOT NULL,
	    `RatecodeID` int(10) NOT NULL,
	    `store_and_fwd_flag` varchar(200) NOT NULL,
	    `PULocationID` int(10) NOT NULL,
	    `DOLocationID` int(10) NOT NULL,
	    `payment_type` int(10) NOT NULL,
	    `fare_amount` decimal NOT NULL,
	    `extra` decimal NOT NULL,
	    `mta_tax` decimal NOT NULL,
	    `tip_amount` decimal NOT NULL,
	    `tolls_amount` decimal NOT NULL,
	    `improvement_surcharge` decimal NOT NULL,
	    `total_amount` decimal NOT NULL,
	    `congestion_surcharge` decimal NOT NULL,
	PRIMARY KEY (`csv_date`, `tpep_pickup_datetime`, `tpep_dropoff_datetime`, `PULocationID`, `DOLocationID`, `VendorID`)
    )
"""

GREEN_TAXI_CREATE_TABLE_QUERY = """
	CREATE TABLE trips.green_taxi (
		`csv_date` varchar(10) NOT NULL,
		`VendorID` int(10) NOT NULL,
		`lpep_pickup_datetime` datetime NOT NULL,
		`lpep_dropoff_datetime` datetime NOT NULL,
		`store_and_fwd_flag` varchar(200) NOT NULL,
		`RatecodeID` int(10) NOT NULL,
		`PULocationID` int(10) NOT NULL,
		`DOLocationID` int(10) NOT NULL,
		`passenger_count` int(10) NOT NULL,
		`trip_distance` decimal NOT NULL,
		`fare_amount` decimal NOT NULL,
		`extra` decimal NOT NULL,
		`mta_tax` decimal NOT NULL,
		`tip_amount` decimal NOT NULL,
		`tolls_amount` decimal NOT NULL,
		`ehail_fee` decimal NOT NULL,
		`improvement_surcharge` decimal NOT NULL,
		`total_amount` decimal NOT NULL,
		`payment_type` int(10) NOT NULL,
		`trip_type` int(10) NOT NULL,
		`congestion_surcharge` decimal NOT NULL,
	PRIMARY KEY (`csv_date`, `lpep_pickup_datetime`, `lpep_dropoff_datetime`, `PULocationID`, `DOLocationID`, `VendorID`)
	)
"""

FOR_HIRE_TAXI_CREATE_TABLE_QUERY = """
	CREATE TABLE trips.for_hire (
		`csv_date` varchar(10) NOT NULL,
		`dispatching_base_num` varchar(200) NOT NULL,
		`pickup_datetime` datetime NOT NULL,
		`dropoff_datetime` datetime NOT NULL,
		`PULocationID` int(10) NOT NULL,
		`DOLocationID` int(10) NOT NULL,
		`SR_Flag` tinyint(1),
	PRIMARY KEY (`csv_date`, `pickup_datetime`, `dropoff_datetime`, `PULocationID`, `DOLocationID`, `dispatching_base_num`)
	)
"""

HIGH_VOLUME_FOR_HIRE_TAXI_CREATE_TABLE_QUERY = """
	CREATE TABLE trips.hv_for_hire (
		`csv_date` varchar(10) NOT NULL,
		`hvfhs_license_num` varchar(200) NOT NULL,
		`dispatching_base_num` varchar(200) NOT NULL,
		`pickup_datetime` datetime NOT NULL,
		`dropoff_datetime` datetime NOT NULL,
		`PULocationID` int(10) NOT NULL,
		`DOLocationID` int(10) NOT NULL,
		`SR_Flag` tinyint(1),
	PRIMARY KEY (`csv_date`, `pickup_datetime`, `dropoff_datetime`, `PULocationID`, `DOLocationID`, `hvfhs_license_num`)
	)
"""


# UPSERT TO PRODUCTION QUERIES
YELLOW_TAXI_UPSERT_QUERY = """
    INSERT INTO
        trips.yellow_taxi (
		`csv_date`,
	    `VendorID`,
	    `tpep_pickup_datetime`,
	    `tpep_dropoff_datetime`,
	    `passenger_count`,
	    `trip_distance`,
	    `RatecodeID`,
	    `store_and_fwd_flag`,
	    `PULocationID`,
	    `DOLocationID`,
	    `payment_type`,
	    `fare_amount`,
	    `extra`,
	    `mta_tax`,
	    `tip_amount`,
	    `tolls_amount`,
	    `improvement_surcharge`,
	    `total_amount`,
	    `congestion_surcharge`
        )
	    SELECT
		    *
	    FROM
        tmp.yellow_taxi temp
    ON DUPLICATE KEY UPDATE
		`csv_date` = temp.csv_date,
	    `VendorID` = temp.VendorID,
	    `tpep_pickup_datetime` = temp.tpep_pickup_datetime,
	    `tpep_dropoff_datetime` = temp.tpep_dropoff_datetime,
	    `passenger_count` = temp.passenger_count,
	    `trip_distance` = temp.trip_distance,
	    `RatecodeID` = temp.RatecodeID,
	    `store_and_fwd_flag` = temp.store_and_fwd_flag,
	    `PULocationID` = temp.PULocationID,
	    `DOLocationID` = temp.DOLocationID,
	    `payment_type` = temp.payment_type,
	    `fare_amount` = temp.fare_amount,
	    `extra` = temp.extra,
	    `mta_tax` = temp.mta_tax,
	    `tip_amount` = temp.tip_amount,
	    `tolls_amount` = temp.tolls_amount,
	    `improvement_surcharge` = temp.improvement_surcharge,
	    `total_amount` = temp.total_amount,
	    `congestion_surcharge` = temp.congestion_surcharge
"""

GREEN_TAXI_UPSERT_QUERY = """
    INSERT INTO
        trips.green_taxi (
		`csv_date`,
        `VendorID`,
        `lpep_pickup_datetime`,
        `lpep_dropoff_datetime`,
        `store_and_fwd_flag`,
        `RatecodeID`,
        `PULocationID`,
        `DOLocationID`,
        `passenger_count`,
        `trip_distance`,
        `fare_amount`,
        `extra`,
        `mta_tax`,
        `tip_amount`,
        `tolls_amount`,
        `ehail_fee`,
        `improvement_surcharge`,
        `total_amount`,
        `payment_type`,
        `trip_type`,
        `congestion_surcharge`
        )
	    SELECT
		    *
	    FROM
        tmp.green_taxi temp
    ON DUPLICATE KEY UPDATE
		`csv_date` = temp.csv_date,
        `VendorID` = temp.VendorID,
        `lpep_pickup_datetime` = temp.lpep_pickup_datetime,
        `lpep_dropoff_datetime` = temp.lpep_dropoff_datetime,
        `store_and_fwd_flag` = temp.store_and_fwd_flag,
        `RatecodeID` = temp.RatecodeID,
        `PULocationID` = temp.PULocationID,
        `DOLocationID` = temp.DOLocationID,
        `passenger_count` = temp.passenger_count,
        `trip_distance` = temp.trip_distance,
        `fare_amount` = temp.fare_amount,
        `extra` = temp.extra,
        `mta_tax` = temp.mta_tax,
        `tip_amount` = temp.tip_amount,
        `tolls_amount` = temp.tolls_amount,
        `ehail_fee` = temp.ehail_fee,
        `improvement_surcharge` = temp.improvement_surcharge,
        `total_amount` = temp.total_amount,
        `payment_type` = temp.payment_type,
        `trip_type` = temp.trip_type,
        `congestion_surcharge` = temp.congestion_surcharge
"""

FOR_HIRE_TAXI_UPSERT_QUERY = """
    INSERT INTO
        trips.for_hire (
			`csv_date`,
            `dispatching_base_num`,
            `pickup_datetime`,
            `dropoff_datetime`,
            `PULocationID`,
            `DOLocationID`,
            `SR_Flag`
        )
	    SELECT
		    *
	    FROM
        tmp.for_hire temp
    ON DUPLICATE KEY UPDATE
		`csv_date` = temp.csv_date,
	    `dispatching_base_num` = temp.dispatching_base_num,
	    `pickup_datetime` = temp.pickup_datetime,
	    `dropoff_datetime` = temp.dropoff_datetime,
	    `PULocationID` = temp.PULocationID,
	    `DOLocationID` = temp.DOLocationID,
	    `SR_Flag` = temp.SR_Flag
"""


HIGH_VOLUME_FOR_HIRE_TAXI_UPSERT_QUERY = """
    INSERT INTO
        trips.hv_for_hire (
			`csv_date`,
            `hvfhs_license_num`,
            `dispatching_base_num`,
            `pickup_datetime`,
            `dropoff_datetime`,
            `PULocationID`,
            `DOLocationID`,
            `SR_Flag`
        )
	    SELECT
		    *
	    FROM
        tmp.hv_for_hire temp
    ON DUPLICATE KEY UPDATE
		`csv_date` = temp.csv_date,
        `hvfhs_license_num` = temp.hvfhs_license_num,
        `dispatching_base_num` = temp.dispatching_base_num,
        `pickup_datetime` = temp.pickup_datetime,
        `dropoff_datetime` = temp.dropoff_datetime,
        `PULocationID` = temp.PULocationID,
        `DOLocationID` = temp.DOLocationID,
        `SR_Flag` = temp.SR_Flag
"""

# CREATE BADROWS TABLES QUERIES
YELLOW_TAXI_BADROWS_CREATE_TABLE_QUERY = """
	CREATE TABLE badrows.yellow_taxi (
		`csv_date` varchar(10),
	    `VendorID` int(10),
	    `tpep_pickup_datetime` datetime,
	    `tpep_dropoff_datetime` datetime,
	    `passenger_count` int(10),
	    `trip_distance` decimal,
	    `RatecodeID` int(10),
	    `store_and_fwd_flag` varchar(200),
	    `PULocationID` int(10),
	    `DOLocationID` int(10),
	    `payment_type` int(10),
	    `fare_amount` decimal,
	    `extra` decimal,
	    `mta_tax` decimal,
	    `tip_amount` decimal,
	    `tolls_amount` decimal,
	    `improvement_surcharge` decimal,
	    `total_amount` decimal,
	    `congestion_surcharge` decimal,
		`insertion_date` datetime
	)
"""

GREEN_TAXI_BADROWS_CREATE_TABLE_QUERY = """
	CREATE TABLE badrows.green_taxi (
		`csv_date` varchar(10),
		`VendorID` int(10),
		`lpep_pickup_datetime` datetime,
		`lpep_dropoff_datetime` datetime,
		`store_and_fwd_flag` varchar(200),
		`RatecodeID` int(10),
		`PULocationID` int(10),
		`DOLocationID` int(10),
		`passenger_count` int(10),
		`trip_distance` decimal,
		`fare_amount` decimal,
		`extra` decimal,
		`mta_tax` decimal,
		`tip_amount` decimal,
		`tolls_amount` decimal,
		`ehail_fee` decimal,
		`improvement_surcharge` decimal,
		`total_amount` decimal,
		`payment_type` int(10),
		`trip_type` int(10),
		`congestion_surcharge` decimal,
		`insertion_date` datetime
	)
"""

FOR_HIRE_TAXI_BADROWS_CREATE_TABLE_QUERY = """
	CREATE TABLE badrows.for_hire (
		`csv_date` varchar(10),
		`dispatching_base_num` varchar(200),
		`pickup_datetime` datetime,
		`dropoff_datetime` datetime,
		`PULocationID` int(10),
		`DOLocationID` int(10),
		`SR_Flag` tinyint(1),
		`insertion_date` datetime		
	)
"""

HIGH_VOLUME_FOR_HIRE_TAXI_BADROWS_CREATE_TABLE_QUERY = """
	CREATE TABLE badrows.hv_for_hire (
		`csv_date` varchar(10),
		`hvfhs_license_num` varchar(200),
		`dispatching_base_num` varchar(200),
		`pickup_datetime` datetime,
		`dropoff_datetime` datetime,
		`PULocationID` int(10),
		`DOLocationID` int(10),
		`SR_Flag` tinyint(1),
		`insertion_date` datetime
	)
"""

DROPPED_ROWS_BADROWS_CREATE_TABLE_QUERY = """
	CREATE TABLE badrows.dropped_rows (
	    `taxi` varchar(200) NOT NULL,
		`csv_date` varchar(10) NOT NULL,
	    `dropped_rows` int(10) NOT NULL,
	PRIMARY KEY (`taxi`, `csv_date`)
    )
"""

# DIMENSION INSERT QUERY
INSERT_VENDOR_QUERY = """
	INSERT INTO trips.vendors
		(`VendorID`,`vendor`)
	VALUES
		(1, 'Creative Mobile Technologies, LLC'),
		(2, 'VeriFone Inc.')
"""

INSERT_RATECODE_QUERY = """
	INSERT INTO trips.ratecode
		(`RateCodeID`,`rate_code`)
	VALUES
		(1, 'Standard rate'),
		(2, 'JFK'),
		(3, 'Newark'),
		(4, 'Nassau or Westchester'),
		(5, 'Negotiated fare'),
		(6, 'Group ride')
"""

INSERT_PAYMENT_TYPE_QUERY = """
	INSERT INTO trips.payment_type
		(`payment_type_id`,`payment_type`)
	VALUES
		(1, 'Credit card'),
		(2, 'Cash'),
		(3, 'No charge'),
		(4, 'Dispute'),
		(5, 'Unknown'),
		(6, 'Voided trip')
"""

INSERT_TRIP_TYPE_QUERY = """
	INSERT INTO trips.trip_type
		(`Trip_type`,`trip_name`)
	VALUES
		(1, 'Street-hail'),
		(2, 'Dispatch')
"""

# DYNAMIC ETL QUERIES
TRUNCATE_TMP_QUERY = "TRUNCATE TABLE {db}.{table}"

NULLS_TO_BADROWS_QUERY = "INSERT INTO badrows.{table} SELECT *, NOW() FROM {db}.{table} WHERE CONCAT({columns}) is NULL"

COUNT_UPSERT_BADROWS_QUERY = """
	INSERT INTO badrows.dropped_rows(
	      `taxi`,
	      `csv_date`,
	      `dropped_rows`
	      )
	      SELECT
	            "{name}" AS taxi,
	            "{csv_date}" AS csv_date,
	            COUNT(*) AS dropped_rows  
	      FROM
	            tmp.yellow_taxi
	      WHERE
	            CONCAT({columns}) is NULL
	ON DUPLICATE KEY UPDATE
	      `taxi` = taxi,
	      `csv_date` = csv_date,
	      `dropped_rows` = dropped_rows
"""

REMOVE_NULLS_QUERY = "DELETE FROM {db}.{table} WHERE CONCAT({columns}) is NULL"
