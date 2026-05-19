-- 查询当前表的所有父子关系
SELECT
    tc.table_name      AS child_table,
    kcu.column_name    AS child_column,
    ccu.table_name     AS parent_table,
    ccu.column_name    AS parent_column,
    rc.delete_rule
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu USING (constraint_name)
JOIN information_schema.constraint_column_usage ccu USING (constraint_name)
JOIN information_schema.referential_constraints rc USING (constraint_name)
WHERE tc.constraint_type = 'FOREIGN KEY'
ORDER BY child_table, child_column;
