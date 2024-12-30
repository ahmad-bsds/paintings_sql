# Advanced SQL Analytics: Museum Paintings Dataset

A comprehensive SQL analysis project demonstrating data-driven insights in the art museum domain using PostgreSQL. The analysis covers pricing optimization, museum operations, artist performance metrics, and collection management.

## Business Questions Addressed

### Revenue Optimization
- Price elasticity analysis identifying paintings priced below 50% of regular price
- Premium canvas size identification for pricing strategy
- Most valuable painting locations and characteristics
- Sales price vs regular price variance analysis

### Museum Operations
- Operating hours optimization through peak timing analysis
- Museum capacity utilization via painting distribution
- Cross-museum collection comparison
- Invalid data identification and cleanup processes

### Collection Analytics
- Popular painting styles impact on museum traffic
- Subject matter popularity trends
- Artist popularity metrics across countries
- Museum collection diversity analysis

## Key SQL Techniques Demonstrated

### Advanced SQL Features
```sql
-- Window Functions for Ranking
WITH pop_style AS (
    SELECT style,
           RANK() OVER(ORDER BY COUNT(1) DESC) as rnk
    FROM work
    GROUP BY style
)

-- Complex CTEs for Multi-level Analysis
WITH cte_country AS (
    SELECT country, COUNT(1),
           RANK() OVER(ORDER BY COUNT(1) DESC) as rnk
    FROM museum
    GROUP BY country
)

-- Data Quality Checks
SELECT * FROM museum 
WHERE city ~ '^[0-9]'

-- Time-based Analysis
SELECT museum_name, state, day, 
       TO_TIMESTAMP(close,'HH:MI PM') - TO_TIMESTAMP(open,'HH:MI AM') as duration
FROM museum_hours
```

### Performance Optimization
- Subquery optimization using EXISTS clause
- Efficient duplicate removal strategies
- Proper indexing recommendations
- Query execution plan analysis

## Data Model
- 8 interconnected tables with referential integrity
- Covers artists, museums, paintings, and sales data
- Temporal data for museum operations
- Geographic distribution analysis capability

## Technical Implementation

### Data Loading Process
- Automated ETL using Python
- Data validation and error handling
- Transaction management
- Data quality verification

## Key Findings

1. Museum Performance
   - Peak operation hours identification
   - Correlation between collection size and visitor metrics
   - Geographic concentration analysis

2. Artist Analytics
   - Cross-border artist popularity metrics
   - Style influence on museum placement
   - Collection value distribution

3. Pricing Intelligence
   - Canvas size impact on pricing
   - Museum location influence on valuations
   - Seasonal pricing patterns
