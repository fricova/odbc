library(odbc)
con <- dbConnect(odbc::odbc(), "SQLserveR")

{sql connection=con, output.var = data}
```{sql connection=con, output.var = data}
select TOP (1000) *
from Autotracer.dbo.at_dotaz
```

data <- 
  dbGetQuery(con,
             'select TOP (1000) *
from Autotracer.dbo.at_dotaz')
data