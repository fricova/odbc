library(odbc)
con <- dbConnect(odbc::odbc(), "SQLserveR")

{sql connection=con, output.var = data}
```{sql connection=con, output.var = data}
select TOP (1000) *
from database.dbo.dataset
```

data <- 
  dbGetQuery(con,
             'select TOP (1000) *
from database.dbo.dataset')
data
