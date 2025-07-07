/* On veut vérifier que pour chaque client, il y a une commande associée */
SELECT o.customer_id
FROM  {{ ref('stg_customers') }} c 
LEFT JOIN {{ ref('stg_orders') }} o
  ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL