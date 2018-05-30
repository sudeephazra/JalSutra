WITH azureml AS (
    select 
        cast(temperature as float) temperature, 
        cast(humidity as float) humidity,
        cast(soilMoisture as float) soilMoisture,
        cast(isRaining as float) isRaining,
        azureml(
            temperature, 
            humidity
        ) as result 
    from raspberrypi3
) 
select 
    System.TimeStamp time, 
    cast(temperature as float) as temperature,
    cast(humidity as float) as humidity,
    cast(result.[Scored Probabilities] as float) * 100 as rain_chance,
    result.[Scored Labels]  as scored_label,
    cast(soilMoisture as float) soilMoisture,
    cast(isRaining as float) isRaining
INTO
    CaliberIoT
FROM
    azureml

select 
    System.TimeStamp time, 
    cast(temperature as float) as temperature,
    cast(humidity as float) as humidity,
    cast(result.[Scored Probabilities] as float) * 100 as rain_chance,
    result.[Scored Labels]  as scored_label,
    cast(soilMoisture as float) soilMoisture,
    cast(isRaining as float) isRaining
INTO
    caliberiotreporting
FROM
    azureml

select 
    System.TimeStamp time, 
    cast(temperature as float) as temperature,
    cast(humidity as float) as humidity,
    cast(result.[Scored Probabilities] as float) * 100 as rain_chance,
    result.[Scored Labels]  as scored_label,
    cast(soilMoisture as float) soilMoisture,
    cast(isRaining as float) isRaining
INTO
    caliberioteventhubc2d
FROM
    azureml