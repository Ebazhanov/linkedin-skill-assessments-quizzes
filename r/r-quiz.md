## R (Programming Language)

#### Q1. How does a matrix differ from a data frame?

- [ ] A matrix may contain numeric values only.
- [ ] A matrix must not be singular.
- [x] A data frame may contain variables that have different modes.
- [ ] A data frame may contain variables of different lengths.

#### Q2. What value does this statement return?

`unclass(as.Date("1971-01-01"))`

- [ ] 1
- [x] 365
- [ ] 4
- [ ] 12

#### Q3. What do you use to take an object such as a data frame out of the workspace?

- [x] remove()
- [ ] erase()
- [ ] detach()
- [ ] delete()

#### Q4. Review the following code. What is the result of line 3?

```
xvect<-c(1,2,3)
xvect[2] <- "2"
xvect
```

- [ ] [1] 1 2 3
- [ ] [1] "1" 2 "3"
- [x] [1] "1" "2" "3"
- [ ] [1] 7 9

#### Q5. The variable height is a numeric vector in the code below. Which statement returns the value 35?

- [ ] `height(length(height))`
- [x] `height[length(height)]`
- [ ] `height[length[height]]`
- [ ] `height(5)`

#### Q6. In the image below, the data frame is named rates. The statement `sd(rates[, 2])` returns 39. As what does R regard Ellen's product ratings?

![Image](https://i.ibb.co/jvPPSRk/Captura-de-pantalla-2020-07-14-a-las-20-58-09.png?raw=png)

- [ ] sample with replacement
- [ ] population
- [ ] trimmed sample
- [x] sample <-- not sure

#### Q7. Which choice does R regard as an acceptable name for a variable?

- [ ] `Var_A!`
- [ ] `\_VarA`
- [ ] `.2Var_A`
- [x] `Var2_A`

#### Q8. What is the principal difference between an array and a matrix?

- [x] A matrix has two dimensions, while an array can have three or more dimensions.
- [ ] An array is a subtype of the data frame, while a matrix is a separate type entirely.
- [ ] A matrix can have columns of different lengths, but an array's columns must all be the same length.
- [ ] A matrix may contain numeric values only, while an array can mix different types of values.

#### Q9. Which is not a property of lists and vectors?

- [ ] type
- [ ] length
- [ ] attributes
- [x] scalar

#### Q10. In the image below, the data frame on lines 1 through 4 is named StDf. State and Capital are both factors. Which statement returns the results shown on lines 6 and 7?

![Image](https://i.ibb.co/8DL1HCV/Captura-de-pantalla-2020-07-14-a-las-18-33-34.png?raw=png)

- [ ] StDf[1:2,-3]
- [x] StDf[1:2,1]
- [ ] StDf[1:2,]
- [ ] StDf[1,2,]

#### Q11. Which function displays the first five rows of the data frame named pizza?

- [ ] BOF(pizza, 5)
- [ ] first(pizza, 5)
- [ ] top(pizza, 5)
- [x] head(pizza, 5)

#### Q12. You accidentally display a large data frame on the R console, losing all the statements you entered during the current session. What is the best way to get the prior 25 statements back?

- [ ] console(-25)
- [ ] console(reverse=TRUE)
- [ ] history()
- [x] history(max.show = 25)

#### Q13. d.pizza is a data frame. It's a column named temperature contains only numbers. If you extract temperature using the [] accessors, its class defaults to numeric. How can you access temperature so that it retains the class of data.frame?

```
> class( d.pizza[ , "temperature" ] )
> "numeric"
```

- [ ] `class( d.pizza( , "temperature" ) )`
- [ ] `class( d.pizza[ , "temperature" ] )`
- [ ] `class( d.pizza$temperature )`
- [x] `class( d.pizza[ , "temperature", drop=F ] )`

#### Q14. What does c contain?

```
a <- c(3,3,6.5,8)
b <- c(7,2,5.5,10)
c <- a < b
```

- [ ] [1] NaN
- [ ] [1] -4
- [ ] [1] 4 -1 -1 2
- [x] [1] TRUE FALSE FALSE TRUE

#### Q15. Review the statements below. Does the use of the dim function change the class of y, and if so what is y's new class?

```
> y <- 1:9
> dim(y) <- c(3,3)
```

- [ ] No, y's new class is "array".
- [x] Yes, y's new class is "matrix".
- [ ] No, y's new class is "vector".
- [ ] Yes, y's new class is "integer".

#### Q16. What is `mydf$y` in this code?

`mydf <- data.frame(x=1:3, y=c("a","b","c"), stringAsFactors=FALSE)`

- [ ] list
- [ ] string
- [ ] factor
- [x] character vector

#### Q17. How does a vector differ from a list?

- [ ] Vectors are used only for numeric data, while lists are useful for both numeric and string data.
- [ ] Vectors and lists are the same thing and can be used interchangeably.
- [x] A vector contains items of a single data type, while a list can contain items of different data types.
- [ ] Vectors are like arrays, while lists are like data frames.

#### Q18. What statement shows the objects on your workspace?

- [ ] list.objects()
- [ ] print.objects()
- [ ] getws()
- [x] ls()

#### Q19. What function joins two or more column vectors to form a data frame?

- [ ] rbind()
- [x] cbind()
- [ ] bind()
- [ ] coerce()

#### Q20. Review line 1 below. What does the statement in line 2 return?

```
1 mylist <- list(1,2,"C",4,5)
2 unlist(mylist)
```

- [ ] [1] 1 2 4 5
- [ ] "C"
- [x] [1] "1" "2" "C" "4" "5"
- [ ] [1] 1 2 C 4 5

#### Q21. What is the value of y in this code?

```
x <- NA
y <- x/1
```

- [ ] Inf
- [ ] Null
- [ ] NaN
- [x] NA

#### Q22. Two variable in the mydata data frame are named Var1 and Var2. How do you tell a bivariate function, such as cor.test, which two variables you want to analyze?

- [ ] `cor.test(Var1 ~ Var2)`
- [ ] `cor.test(mydata$(Var1,Var2))`
- [x] `cor.test(mydata$Var1,mydata$Var2)`
- [ ] `cor.test(Var1,Var2, mydata)`

#### Q23. A data frame named d.pizza is part of the DescTools package. A statement is missing from the following R code and an error is therefore likely to occur. Which statement is missing?

```
library(DescTools)
deliver <- aggregate(count,by=list(area,driver), FUN=mean)
print(deliver)
```

- [x] `attach(d.pizza)`
- [ ] `summarize(deliver)`
- [ ] `mean <- rbind(d.pizza,count)`
- [ ] `deliver[!complete.cases(deliver),]`

#### Q24. How to name rows and columns in DataFrames and Matrices F in R?

- [ ] data frame: names() and rownames() matrix: colnames() and row.names()
- [x] data frame: names() and row.names() matrix: dimnames() (not sure)
- [ ] data frame: colnames() and row.names() matrix: names() and rownames()
- [ ] data frame: colnames() and rownames() matrix: names() and row.names()

#### Q25. Which set of two statements-followed by the cbind() function-results in a data frame named vbound?

- [ ] &shy;

```r
v1<-list(1,2,3)
v2<-list(c(4,5,6))
vbound<-cbind(v1,v2)
```

- [ ] &shy;

```r
v1<-c(1,2,3)
v2<-list(4,5,6))
vbound<-cbind(v1,v2)
```

- [x] &shy;

```r
v1<-c(1,2,3)
v2<-c(4,5,6))
vbound<-cbind(v1,v2)
```

- [ ] &shy;
      none

#### Q26. ournames is a character vector. What values does the statement below return to Cpeople?

`Cpeople <- ournames %in% grep("^C", ournames, value=TRUE)`

- [ ] records where the first character is a C
- [ ] any record with a value containing a C
- [ ] TRUE or FALSE, depending on whether any character in ournames is C
- [x] TRUE and FALSE values, depending on whether the first character in an ournames record is C

#### Q27. What is the value of names(v[4])?

```r
v <- 1:3
names(v) <- c("a", "b", "c")
v[4] <- 4
```

- [x] ""
- [ ] d
- [ ] NULL
- [ ] NA

#### Q28. Which of the following statements doesn't yield the code output below. Review the following code. What is the result of line 3?

```r
x <- c(1, 2, 3, 4)
Output: [1] 2 3 4
```

- [ ] x[c(2, 3, 4)]
- [ ] x[-1]
- [ ] x[c(-1, 0, 0, 0)]
- [x] x[c(-1, 2, 3, 4)]

#### Q29. Given DFMerged <- merge(DF1, DF2) and the image below, how many rows are in DFMerged?

![image](https://user-images.githubusercontent.com/52632898/139964478-9806a163-76b2-4f99-97bc-c925fdf6e388.png?raw=png)

- [ ] 6
- [ ] 9
- [ ] 3
- [x] 0

#### Q30. What does R return in response to the final statement?

```r
x<-5:8
names(x)<-letters[5:8]
x
```

- [ ] e f g h
      "5" "6" "7" "8"
- [ ] 5 6 7 8
- [ ] e f g h
- [x] e f g h
      5 6 7 8

#### Q31. How do you return "October" from x in this code?

```r
x<-as.Date("2018-10-01")
```

- [ ] attr()
- [x] months(x)
- [ ] as.month(x)
- [ ] month(x)

#### Q32. How will R respond to the last line of this code?

```r
fact<-factor(c("Rep","Dem","Dem","Rep"))
fact
[1] Rep Dem Dem Rep
Levels: Rep Dem
fact[2]<-"Ind"
```

- [ ] >
- [ ] [,2]Ind
- [x] invalid factor level, NA generated
- [ ] Ind

#### Q33. What does R return?

```r
StartDate<- as.Date("2020/2/28")
StopDate<- as.Date("2020/3/1")
StopDate-StartDate
```

- [ ] "1970-01-02"
- [ ] time difference of one day
- [x] time difference of two days
- [ ] error in x-y: nonnumeric argument to binary operator

#### Q34. What does the expression `mtrx * mtrx` do ?

```r
> mtrx <- matrix( c(3,5,8,4), nrow= 2,ncol=2,byrow=TRUE)
> newmat <- mtrx * mtrx
```

- [ ] it transpose **mtrx**
- [ ] it premultiplies the current **netwmat** row by the **newmat** column.
- [ ] it returns the results of a matrix multiplication
- [x] It squares each cell in **mtrx**

```r
> newmat
     [,1] [,2]
[1,]    9   25
[2,]   64   16

# The `%*%` operator gives matrix multiplication
> mtrx %*% mtrx
     [,1] [,2]
[1,]   49   35
[2,]   56   56
```

#### Q35. Which function in R combines different values into a single object?

- [ ] connect()
- [ ] concat()
- [ ] contact()
- [x] c()

#### Q36. Which file contains settings that R uses for all users of a given installation of R?

- [ ] Rdefaults.site
- [ ] Renviron.site
- [x] Rprofile.site
- [ ] Rstatus.site

#### Q37. If **mdf** is a data frame, which statement is true ?

- [x] **ncol(mdf)** equals **length(mdf)**.
- [ ] The number of rows must equals the number of columns.
- [ ] The legnth of any column in **mdf** may differ from any other column in **mdf**
- [ ] All columns must have the same data type.

#### Q38. A list can contain a list as an element. **MyList** has five columns, and the third column's item is a list of three items. How do you put all seven values in **MyList** into a single vector?

- [ ] vector(MyList, length = 7)
- [ ] coerce(MyList, nrows = 1)
- [x] unlist(MyList)
- [ ] coerce(MyList, nrows = 7)

#### Q39. Which strings could be returned by the function ls(path = "^V")?

- [ ] ANOVAData, anovadata
- [x] VisitPCA, VarX
- [ ] VisitPCA, varx
- [ ] Xvar, Yvar

#### Q40. StDf is a data frame. Based on this knowledge, what does this statement return?

```r
StDf[, -1]
```

- [ ] all but the first row and first column of StDf
- [ ] all but the final column of StDf
- [x] all but the first column of StDf
- [ ] only the first column of StDf

#### Q41. Which statement enables you to interactively open a single file?

- [ ] file.list()
- [ ] file.select()
- [x] file.choose()
- [ ] file.open()

#### Q42. How are these data types alike: logical, integer, numeric, and character?

- [ ] Each is a type of data frame.
- [x] Each is a type of atomic vector.
- [ ] Each is a type of complex vector.
- [ ] Each is a type of raw vector.

#### Q43. What does the `MyMat[ ,3]` subsetting operation return for this code?

```r
MyMat = matrix(c(7, 9, 8, 6, 10, 12),nrow=2,ncol=3, byrow = TRUE)
```

- [ ] :

```
[ ,3]
[1, ] 8
[2, ] 12
```

- [x] :

```
[1] 8 12
```

- [ ] :

```
[1] 10 12
```

- [ ] :

```
[ ,3]
[1, ] 10
[2, ] 12
```

#### Q44. What does the function `power.anova.test` return?

- [ ] the probability of making a Type I error
- [x] the probability of not making a Type II error
- [ ] the probability of making a Type II error
- [ ] the probability of not making a Type I error

#### Q45. Review the statement below. What is the effect of `covariate:factor` on the analysis?

```r
result <- lm(outcome ~ covariate + factor + covariate:factor, data = testcoef)
```

- [ ] It forces the intercepts of the individual regressions to zero.
- [x] It calls for the effect of the covariate **within each level of the factor**.
- [ ] It calls for the effect of each variable from covariate to factor in testcoef.
- [ ] It forces the covariate to enter the equation before the factor levels.

```r
# Example call to demonstrate.  `Species` is a Factor.  Petal.Length, Petal.Width are numeric.
# see `help(formula)` for more details on the formula specification.  `:` is "effect modification" or "interaction"

> summary(lm(Petal.Length ~ Petal.Width + Species + Petal.Width:Species, data = iris))
...
Petal.Width:Speciesversicolor   1.3228     0.5552   2.382   0.0185 *
Petal.Width:Speciesvirginica    0.1008     0.5248   0.192   0.8480
...
```

#### Q46. A variable whose type is numeric can contain which items?

- [ ] integers and real values
- [ ] integers, real, and raw values
- [x] real values only
- [ ] integers, real, and logical values

#### Q47. What is the legitimate name of a data class in R?

- [ ] property
- [x] integer
- [ ] number
- [ ] variant

#### Q48. How do you extract the values above the main diagonal from a square matrix named `Rmat`?

- [x] `Rmat[upper.tri(Rmat)]`
- [ ] `upper.triangular(Rmat)`
- [ ] `upper.tri(Rmat)`
- [ ] `upper.diag(Rmat)`

#### Q49. `x` is a vector of type integer, as shown on line 1 below. What is the type of the result returned by the statement > median(x)?

`x <- c(12L, 6L, 10L, 8L, 15L, 14L, 19L, 18L, 23L, 59L)`

- [ ] numeric
- [ ] integer
- [ ] single
- [x] double

#### Q50. A list named `a` is created using the statement below. Which choice returns TRUE?

`a <- list("10", TRUE, 5.6)`

- [x] is.list(a[1])
- [ ] is.numeric(a[1])
- [ ] is.logical(a[1])
- [ ] is.character(a[1])

#### Q51. How do you obtain the row numbers in a data frame named `pizza` for which the value of `pizza$delivery_min` is greater than or equal to 30?

- [ ] :

```r
late_delivery <- pizza$delivery_min >= 30
index_late <- index(late_delivery)
index_late
```

- [ ] :

```r
late_delivery <- pizza$delivery_min >= 30
rownum_late <- rownum(late_delivery)
rownum_late
```

- [x] :

```r
late_delivery <- pizza$delivery_min >= 30
which_late <- which(late_delivery)
which_late
```

- [ ] :

```r
late_delivery <- pizza$delivery_min >= 30
late <- piza$late_delivery
pizza$late
```

#### Q52. Which function returns `[1] TRUE FALSE TRUE`?

`indat <- c("Ash Rd","Ash Cir","Ash St")`

- [ ] grepl("[Rd|Ave|Dr|St]", indat)
- [x] grepl("Rd|Ave|Dr|St", indat)
- [ ] grepl("Rd,Ave,Dr,St", indat)
- [ ] grepl("[Rd],[Ave],[Dr],[St]", indat)

#### Q53. Which statement returns the fourth row of a data frame named _fish_?

- [x] fish[4, ]
- [ ] fish( ,4)
- [ ] fish(4, )
- [ ] fish{4, }

#### Q54. What is the value of _csum_?

```
a <- c(1.2, 2, 3.5, 4)
b <- c(1.2, 2.2, 3.5, 4)
csum <-sum(a == b)
```

- [ ] 8
- [x] 3
- [ ] 0.2
- [ ] 21.6

#### Q54. A list named _a_ is created using the statement below. Which choice returns TRUE?

```
a <- list("10", TRUE, 5.6)
```

- [x] is.list(a[1])
- [ ] is.numeric(a[1])
- [ ] is.logical(a[1])
- [ ] is.character(a[1])

#### Q55. What is the result of these three lines of code?

```r
vect1 <- c(1:4)
vect2 <- c(1:2)
vect1 * vect2
```

- [x] [1] 1 4 3 8
- [ ] ERROR
- [ ] [1] 1 2 3 4 1 2
- [ ] [1] 1 2 3 4 2 4 6 8

#### Q56. Which choice returns [1] "2019-09-28"?

- [ ] format(as.POSIXct("Sep-28-2019 07:54:31 AM",format='%b%d%Y'))
- [ ] as.POSIXlt("Sep-28-2019 07:54:31 AM",format='%b-%d-%Y')
- [ ] as.POSIXct("Sep-28-2019 07:54:31 AM UTC")
- [x] format(as.POSIXct("Sep-28-2019 07:54:31 AM UTC",format='%b-%d-%Y'))

#### Q57. The variable potus is a character vector, as shown in line 1 below. Wich statement returns the results shown?

```r
1 potus <- c("GHW Bush", "Clinton", "GW Bush", "Obama")

Results: [1] "GHW BUsh" "Clinton" "Obama"
```

- [ ] potus[-"GW Bush"]
- [ ] potus[1:2 4]
- [x] potus[-3]
- [ ] potus[1,2,4]

#### Q58. A data frame contains two factor -fact1 and fact2- and a numerical outcome variable. Which statement returns results that do NOT include an interaction term?

- [x] anova(lm(outcome ~ fact1 : fact2))
- [ ] anova(lm(outcome ~ fact1 \* fact2))
- [ ] anova(lm(outcome ~ fact1 + fact2))
- [ ] anova(lm(outcome ~ fact1 + fact2 + fact1 : fact2))

#### Q59. Review line 1 below. What does the statement on line 2 return?

```r
1 myvect <- c(-2,-1,0)
2 as.logical(myvect)
```

- [ ] [1]-2 -1 0
- [x] [1]TRUE TRUE FALSE
- [ ] [1]FALSE FALSE TRUE
- [ ] [1]NA NA NA

#### Q60. Which option setting can cause difficulty if you want to add to a variable's possible values after you have designed an object's initial data structure?

- [ ] ()OPTIONS(colnames(x)<-NULL)
- [ ] ()OPTIONS(max.print=5)
- [ ] ()OPTIONS(continue="... ",
- [x] ()OPTIONS(stringAsFactors=TRUE

#### Q61. In this image below, the data frame on lines 1 through 4 is named StDf. StDf contains no factors. Why does statement on line 6 return "character" while the statement on line 7 returns "data.frame"?

![image](https://drive.google.com/uc?export=view&id=16KtAh4dhn2fyImFbcX8KLDgRqNHIFtKm)

- [ ] Each value in the first row is a character value, but the values in the third column include both character and numeric values.
- [ ] By specifying the final row, 3, and no column specified, StDf[3, ] calls for the complete structure.
- [x] Columns in a data frame are vectors generally containing a single type of data. Rows in a data frame are lists, but they belong to a structure that has multiple rows: the data frame.
- [ ] Each value in the first column is a character value, but the values in the third row include both character and numeric values.

#### Q62. Review line 1. What does the statement on line 3 return?

```r
mtrx <- matrix(1:6, 3, 2)

mtrx[, -1]
```

![image](https://drive.google.com/uc?export=view&id=1ntrHVnNfCRvXfKjbpavh7CiIsv7izsJr)

- [ ] &shy;

- [ ] &shy;

- [ ] &shy;

- [x] [1] 4 5 6

#### Q63. Why does sum(!is.na(pizza$week)) return the number of rows with valid, non-NA values in the column named week?

- [x] The exclamation point in !is.na(pizza$week) reverses the meaning of the test it precedes.
- [ ] !is.na(pizza$week) counts the number of NA values in the column.
- [ ] !is.na(pizza$week) returns a vector of TRUE/FALSE values, in which TRUE is treated as a 0 and FALSE as a 1.
- [ ] !is.na(pizza$week) counts the number of non-missing values in the column.

#### Q64. How do you get documentation of an installed and loaded R package named dplyr and packages with dplyr as an alias?

- [ ] help(dplyr)
- [ ] ? dplyr
- [x] ?? dplyr
- [ ] Press the F1 key.

#### Q65. In the image below, the data frame named iris includes a numeric vector named Petal.Length. Do the functions labeled Pair 1 and Pair 2 return the same information?

![image](https://github.com/ManchurianMan/images/blob/main/petals.png?raw=true)

- [x] No, both the length and the class of the returned structures are different.
- [ ] Yes, both pairs of statements return an object with the same length and class.
- [ ] No, the length is the same but the class is different.
- [ ] No, the class is the same but the length is different.

#### Q66. The **\_** for R are the main feature that make it different from the original S language.

- [ ] closure rules
- [x] scoping rules
- [ ] environment rules
- [ ] None of the above

[reference](https://bookdown.org/rdpeng/rprogdatascience/scoping-rules-of-r.html)

#### Q67. Which of the following is a base package for R programming ?

- [x] tools
- [ ] util
- [ ] lang
- [ ] All of the above

[reference](https://www.geeksforgeeks.org/packages-in-r-programming/)

#### Q68. What is the primary purpose of the `apply()` function family in R?

- [ ] To create new data frames from existing ones
- [x] To apply a function to the margins of an array or matrix
- [ ] To filter data based on conditions
- [ ] To merge multiple datasets

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/apply)

#### Q69. Which function is used to read CSV files in R?

- [x] read.csv()
- [ ] load.csv()
- [ ] import.csv()
- [ ] get.csv()

[reference](https://www.rdocumentation.org/packages/utils/versions/3.6.2/topics/read.table)

#### Q70. What does the `str()` function do in R?

- [ ] Converts objects to strings
- [x] Displays the internal structure of an R object compactly
- [ ] Calculates string length
- [ ] Searches for patterns in strings

[reference](https://www.rdocumentation.org/packages/utils/versions/3.6.2/topics/str)

#### Q71. In R, what is the difference between `<-` and `=` for assignment?

- [ ] There is no difference; they are completely interchangeable
- [ ] `=` is deprecated and should never be used
- [x] `<-` is preferred for assignment; `=` is primarily for function arguments
- [ ] `<-` only works with numeric values

[reference](https://stackoverflow.com/questions/1741820/what-are-the-differences-between-and-assignment-operators-in-r)

#### Q72. What does the `library()` function do?

- [ ] Creates a new library of functions
- [x] Loads and attaches add-on packages
- [ ] Lists all installed packages
- [ ] Removes packages from memory

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/library)

#### Q73. Which of the following statements about factors in R is TRUE?

- [ ] Factors can only contain numeric values
- [x] Factors are used to represent categorical data with a fixed set of possible values
- [ ] Factors cannot be converted to character vectors
- [ ] Factors automatically sort data alphabetically

[reference](https://www.stat.berkeley.edu/~s133/factors.html)

#### Q74. What does the `subset()` function return?

- [x] A subset of vectors, matrices, or data frames that meet specified conditions
- [ ] Only the first 10 rows of a dataset
- [ ] A random sample from the data
- [ ] The dimensions of a data structure

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/subset)

#### Q75. In R, what is the purpose of the `with()` function?

- [ ] To combine multiple data frames
- [ ] To create conditional statements
- [x] To evaluate an expression in an environment constructed from data
- [ ] To generate random numbers with specific parameters

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/with)

#### Q76. What is the output of `typeof(5L)` in R?

- [ ] numeric
- [ ] double
- [x] integer
- [ ] single

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/typeof)

#### Q77. Which function is used to calculate the standard deviation in R?

- [ ] stdev()
- [ ] std()
- [x] sd()
- [ ] stddev()

[reference](https://www.rdocumentation.org/packages/stats/versions/3.6.2/topics/sd)

#### Q78. What does the `na.omit()` function do?

- [ ] Replaces NA values with zeros
- [x] Removes rows containing NA values
- [ ] Counts the number of NA values
- [ ] Converts NA to NULL

[reference](https://www.rdocumentation.org/packages/stats/versions/3.6.2/topics/na.fail)

#### Q79. In R, what is a tibble?

- [ ] A base R data structure for 3D arrays
- [x] A modern reimagining of the data frame from the tidyverse
- [ ] A function for creating time series objects
- [ ] A type of list used for nested data

[reference](https://tibble.tidyverse.org/)

#### Q80. What does the `seq()` function generate?

- [ ] Random numbers
- [x] Regular sequences of numbers
- [ ] Unique identifiers
- [ ] Fibonacci sequences

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/seq)

#### Q81. Which operator is used for matrix multiplication in R?

- [ ] -
- [x] %\*%
- [ ] \*\*
- [ ] %x%

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/matmult)

#### Q82. What is the purpose of `set.seed()` in R?

- [ ] To plant random seeds in datasets
- [x] To set the random number generator to produce reproducible results
- [ ] To initialize a new R session
- [ ] To create seed values for machine learning models

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/Random)

#### Q83. What does `nrow()` return for a vector?

- [ ] The length of the vector
- [ ] 1
- [x] NULL
- [ ] An error

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/nrow)

#### Q84. Which function is used to transpose a matrix in R?

- [x] t()
- [ ] transpose()
- [ ] trans()
- [ ] flip()

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/t)

#### Q85. What is the default behavior of `read.csv()` regarding string columns?

- [ ] Converts all strings to factors (in R >= 4.0.0, default is FALSE)
- [x] Keeps strings as character vectors (in R >= 4.0.0)
- [ ] Removes all string columns
- [ ] Converts strings to numeric where possible

[reference](https://www.rdocumentation.org/packages/utils/versions/3.6.2/topics/read.table)

#### Q86. What does the `%>%` operator do in R?

- [ ] Performs modulo division
- [x] Pipes the output of one function to the input of another (from magrittr/dplyr)
- [ ] Compares two values for greater than or equal to
- [ ] Performs matrix multiplication

[reference](https://magrittr.tidyverse.org/reference/pipe.html)

#### Q87. Which function converts a character string to a Date object in R?

- [ ] to.Date()
- [x] as.Date()
- [ ] date()
- [ ] make.Date()

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/as.Date)

#### Q88. What is the result of `rep(1:3, times=2)`?

- [ ] [1] 1 1 2 2 3 3
- [x] [1] 1 2 3 1 2 3
- [ ] [1] 2 4 6
- [ ] [1] 1 2 3 4 5 6

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/rep)

#### Q89. What does `names()` function return for a vector?

- [ ] The data type of the vector
- [ ] The length of the vector
- [x] The names attribute of the vector elements
- [ ] The first element of the vector

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/names)

#### Q90. Which function is used to sort a vector in descending order?

- [ ] sort(x, desc=TRUE)
- [ ] sort.desc(x)
- [x] sort(x, decreasing=TRUE)
- [ ] sort(x, order="desc")

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/sort)

#### Q91. What does the `table()` function do in R?

- [ ] Creates data frames from vectors
- [x] Builds a contingency table of counts
- [ ] Generates HTML tables
- [ ] Formats data in tabular form

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/table)

#### Q92. In R, what is the purpose of the `ifelse()` function?

- [x] Returns a value based on a conditional test
- [ ] Tests if two objects are equal
- [ ] Loops through conditions
- [ ] Handles error conditions

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/ifelse)

#### Q93. What does `length(NULL)` return?

- [x] 0
- [ ] NULL
- [ ] NA
- [ ] 1

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/length)

#### Q94. Which function is used to calculate the correlation between two variables?

- [ ] corr()
- [x] cor()
- [ ] correlation()
- [ ] correlate()

[reference](https://www.rdocumentation.org/packages/stats/versions/3.6.2/topics/cor)

#### Q95. What is the output of `class(matrix(1:6, 2, 3))`?

- [ ] "array"
- [x] "matrix" "array"
- [ ] "numeric"
- [ ] "table"

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/matrix)

#### Q96. Which function is used to find unique elements in a vector?

- [ ] distinct()
- [x] unique()
- [ ] different()
- [ ] single()

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/unique)

#### Q97. What does `lapply()` return?

- [ ] A vector
- [ ] A matrix
- [x] A list
- [ ] A data frame

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/lapply)

#### Q98. In R, what is the purpose of the `aggregate()` function?

- [ ] To combine multiple data frames
- [x] To compute summary statistics for subsets of data
- [ ] To remove duplicate rows
- [ ] To sort data by multiple columns

[reference](https://www.rdocumentation.org/packages/stats/versions/3.6.2/topics/aggregate)

#### Q99. What does `is.na(c(1, NA, 3))` return?

- [ ] [1] NA
- [ ] [1] 1
- [x] [1] FALSE TRUE FALSE
- [ ] [1] TRUE FALSE TRUE

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/NA)

#### Q100. Which function is used to calculate the mean of each column in a data frame?

- [ ] mean(df)
- [ ] apply(df, 1, mean)
- [x] colMeans(df)
- [ ] rowMeans(df)

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/colSums)

#### Q101. What does the `paste()` function do?

- [ ] Copies data from clipboard
- [x] Concatenates strings together
- [ ] Pastes data into a data frame
- [ ] Duplicates objects

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/paste)

#### Q102. In R, what is the difference between `sapply()` and `lapply()`?

- [ ] sapply() is faster than lapply()
- [x] sapply() simplifies the result to a vector or matrix when possible; lapply() always returns a list
- [ ] sapply() works only on lists; lapply() works on any object
- [ ] There is no difference

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/lapply)

#### Q103. What does `dim()` return for a vector of length 10?

- [ ] [1] 10 1
- [ ] [1] 1 10
- [x] NULL
- [ ] [1] 10

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/dim)

#### Q104. Which function is used to read an R script file?

- [ ] read()
- [ ] load()
- [x] source()
- [ ] import()

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/source)

#### Q105. What is the output of `all(c(TRUE, TRUE, FALSE))`?

- [x] FALSE
- [ ] TRUE
- [ ] NA
- [ ] Error

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/all)

#### Q106. Which function creates a sequence from 1 to 10 with increments of 0.5?

- [ ] seq(1, 10, 0.5)
- [x] seq(1, 10, by=0.5)
- [ ] sequence(1, 10, 0.5)
- [ ] series(1:10, step=0.5)

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/seq)

#### Q107. What does `match(c("a", "b"), c("b", "c", "a"))` return?

- [ ] [1] 1 2
- [ ] [1] 2 1
- [x] [1] 3 1
- [ ] [1] FALSE TRUE

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/match)

#### Q108. In R, what is the purpose of the `merge()` function?

- [ ] To combine vectors into a matrix
- [x] To merge two data frames by common columns or row names
- [ ] To concatenate strings
- [ ] To combine multiple plots

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/merge)

#### Q109. What does `range(c(5, 2, 8, 1, 9))` return?

- [ ] [1] 8
- [x] [1] 1 9
- [ ] [1] 2 5 8
- [ ] [1] 5 2 8 1 9

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/range)

#### Q110. Which function is used to calculate the median in R?

- [ ] mid()
- [x] median()
- [ ] middle()
- [ ] med()

[reference](https://www.rdocumentation.org/packages/stats/versions/3.6.2/topics/median)

#### Q111. What is the result of `any(c(FALSE, FALSE, TRUE))`?

- [ ] FALSE
- [x] TRUE
- [ ] NA
- [ ] Error

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/any)

#### Q112. What does `head(df, n=-5)` return?

- [ ] The first 5 rows of df
- [x] All rows except the last 5 rows
- [ ] The last 5 rows of df
- [ ] An error

[reference](https://www.rdocumentation.org/packages/utils/versions/3.6.2/topics/head)

#### Q113. Which function is used to split data into groups in R?

- [ ] divide()
- [ ] separate()
- [x] split()
- [ ] group()

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/split)

#### Q114. What does `rev(1:5)` return?

- [ ] [1] 1 2 3 4 5
- [x] [1] 5 4 3 2 1
- [ ] [1] 5
- [ ] Error

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/rev)

#### Q115. In R, what is the purpose of `attach()`?

- [x] To make the variables in a data frame accessible without using the $ operator
- [ ] To combine two data frames
- [ ] To save a data frame to disk
- [ ] To load a package

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/attach)

#### Q116. What does `nchar("Hello")` return?

- [ ] 6
- [x] 5
- [ ] "Hello"
- [ ] 1

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/nchar)

#### Q117. Which function is used to calculate the sum of each row in a matrix?

- [ ] colSums()
- [x] rowSums()
- [ ] apply(x, 1, sum)
- [ ] Both B and C are correct

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/colSums)

#### Q118. What does `duplicated(c(1, 2, 2, 3))` return?

- [ ] [1] TRUE TRUE TRUE TRUE
- [x] [1] FALSE FALSE TRUE FALSE
- [ ] [1] 2
- [ ] [1] FALSE TRUE FALSE FALSE

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/duplicated)

#### Q119. What is the output of `toupper("hello")`?

- [ ] "hello"
- [x] "HELLO"
- [ ] "Hello"
- [ ] Error

[reference](https://www.rdocumentation.org/packages/base/versions/3.6.2/topics/chartr)

#### Q120. Which function is used to create a histogram in base R?

- [ ] plot()
- [x] hist()
- [ ] histogram()
- [ ] bar()

[reference](https://www.rdocumentation.org/packages/graphics/versions/3.6.2/topics/hist)
