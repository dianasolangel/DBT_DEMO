with source as (
    select * from {{ source('my_dbt_db', 'raw_orders') }}
),
renamed as (
    select
        id as customer_id,
        customer as customer_name
    from source
)
select * from renamed